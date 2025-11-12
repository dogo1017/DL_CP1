"""
Pygbag-compatible Slither.io client with WebSocket support.
- In browser (pygbag/pyodide) it uses the browser WebSocket API via `js.WebSocket`.
- On desktop it falls back to the `websockets` Python library.

Usage (browser):
  pygbag client_pygbag_ws.py
Open the address printed by pygbag (usually http://localhost:8000) 
Use cd /workspaces/DL_CP1/extra/slither_game pygbag client_pygbag_ws.py for browser

This keeps the original game UI and sends/receives a minimal protocol:
- send: {'type':'join','name':...} -> server returns {'player_id': id}
- server sends periodic {'type':'state','players': [...], 'foods': [...]} updates
- client sends {'type':'update', ...} when local player moves
- client sends {'type':'eat','food_id': id} when eating

If server isn't reachable within 10s it falls back to local simulated mode so you can still test UI.
"""

import pygame
import math
import random
import asyncio
import json
import time

# Try to import browser js WebSocket
BROWSER = False
try:
    from js import WebSocket  # available in pyodide/pygbag
    BROWSER = True
except Exception:
    BROWSER = False

# Desktop fallback
try:
    import websockets
except Exception:
    websockets = None

# --- Initialize Pygame ---
pygame.init()

# --- Configuration ---
infoObject = pygame.display.Info()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

PLAYER_BASE_SPEED = 200
BOOST_SPEED_MULTIPLIER = 1.6
BOOST_COST_RATE = 100
MIN_FOOD_SIZE = 5
MAX_FOOD_SIZE = 15
INITIAL_PLAYER_RADIUS = 10
BG_COLOR = (20, 20, 20)
PLAYER_COLOR = (0, 200, 0)
MAP_SIZE = 3000

# --- Setup Display ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slither.io Multiplayer (pygbag+ws)")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# --- Network Manager ---
class NetworkManager:
    def __init__(self):
        self.ws = None
        self.player_id = None
        self.connected = False
        self.game_state = {'players': [], 'foods': []}
        self.loop = None
        self._browser = BROWSER

    def start(self, server_url, player_name):
        """Start connection. Non-blocking: returns immediately and updates self.connected when ready."""
        if self._browser:
            self._start_browser(server_url, player_name)
        else:
            # desktop fallback uses an asyncio task
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.loop.create_task(self._connect_desktop(server_url, player_name))
            # run loop in background via asyncio.ensure_future in new thread would be complex; keep non-blocking
            # We'll run the loop in a background thread so the pygame main thread isn't blocked.
            import threading
            t = threading.Thread(target=self.loop.run_forever, daemon=True)
            t.start()

    # Browser WebSocket implementation
    def _start_browser(self, server_url, player_name):
        try:
            ws = WebSocket.new(server_url)
        except Exception:
            # pyodide's WebSocket may be exposed either as WebSocket or WebSocket.new; try alternate
            ws = WebSocket(server_url)
        self.ws = ws

        def onopen(evt):
            try:
                join_msg = json.dumps({'type': 'join', 'name': player_name})
                ws.send(join_msg)
            except Exception as e:
                print('ws send error onopen', e)

        def onmessage(evt):
            try:
                data_text = str(evt.data)
                data = json.loads(data_text)
                if data.get('type') == 'init':
                    self.player_id = data.get('player_id')
                    self.connected = True
                    print('Connected (browser). player_id=', self.player_id)
                elif data.get('type') == 'state':
                    self.game_state = data
            except Exception as e:
                print('ws onmessage error', e)

        def onclose(evt):
            self.connected = False
            print('WebSocket closed')

        def onerror(evt):
            print('WebSocket error', evt)

        # attach handlers
        try:
            ws.onopen = onopen
            ws.onmessage = onmessage
            ws.onclose = onclose
            ws.onerror = onerror
        except Exception:
            # some pyodide/pygbag bridges expose addEventListener
            try:
                ws.addEventListener('open', onopen)
                ws.addEventListener('message', onmessage)
                ws.addEventListener('close', onclose)
                ws.addEventListener('error', onerror)
            except Exception as e:
                print('Failed to attach WS handlers', e)

    async def _connect_desktop(self, server_url, player_name):
        if websockets is None:
            print('websockets package missing on desktop; network disabled')
            return
        try:
            async with websockets.connect(server_url, max_size=10**7) as websocket:
                self.ws = websocket
                await websocket.send(json.dumps({'type': 'join', 'name': player_name}))
                init_msg = await websocket.recv()
                init_data = json.loads(init_msg)
                self.player_id = init_data.get('player_id')
                self.connected = True
                print('Connected (desktop). player_id=', self.player_id)
                async for message in websocket:
                    data = json.loads(message)
                    if data.get('type') == 'state':
                        self.game_state = data
        except Exception as e:
            print('Connection error (desktop):', e)
            self.connected = False

    def send_update(self, player_data):
        if not self.ws or not self.connected:
            return
        try:
            payload = json.dumps({
                'type': 'update',
                'x': player_data['x'],
                'y': player_data['y'],
                'positions': player_data['positions'],
                'radius': player_data['radius'],
                'length': player_data['length'],
                'score': player_data['score'],
                'shed_food': player_data.get('shed_food')
            })
            if self._browser:
                self.ws.send(payload)
            else:
                # desktop: schedule send on event loop
                asyncio.run_coroutine_threadsafe(self.ws.send(payload), self.loop)
        except Exception as e:
            print('send_update error', e)

    def send_eat(self, food_id):
        if not self.ws or not self.connected:
            return
        try:
            payload = json.dumps({'type': 'eat', 'food_id': food_id})
            if self._browser:
                self.ws.send(payload)
            else:
                asyncio.run_coroutine_threadsafe(self.ws.send(payload), self.loop)
        except Exception as e:
            print('send_eat error', e)

# --- Classes (player/food) ---
class Player:
    def __init__(self, x, y, is_local=False):
        self.pos = pygame.math.Vector2(x, y)
        self.radius = INITIAL_PLAYER_RADIUS
        self.score = 0
        self.color = PLAYER_COLOR if is_local else (random.randint(50,255), random.randint(50,255), random.randint(50,255))
        self.length = 150
        self.base_speed = PLAYER_BASE_SPEED
        self.speed = self.base_speed
        self.positions = [self.pos.copy()] * int(self.length)
        self.boosting = False
        self.is_local = is_local
        self.name = ""

    def update(self, dt):
        if not self.is_local:
            return None
        speed_multiplier = BOOST_SPEED_MULTIPLIER if self.boosting else 1.0
        size_multiplier = (INITIAL_PLAYER_RADIUS / self.radius)
        self.speed = max(100, self.base_speed * size_multiplier * speed_multiplier)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        target = pygame.math.Vector2(mouse_x - SCREEN_WIDTH // 2, mouse_y - SCREEN_HEIGHT // 2)
        if target.length_squared() > 0:
            direction = target.normalize()
            self.pos += direction * self.speed * dt
        self.pos.x = max(self.radius, min(MAP_SIZE - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(MAP_SIZE - self.radius, self.pos.y))
        shed_food_item = None
        self.positions.insert(0, self.pos.copy())
        self.positions = self.positions[:int(self.length)]
        self.update_radius()
        return shed_food_item

    def update_radius(self):
        self.radius = INITIAL_PLAYER_RADIUS + math.sqrt(self.length / 10.0)

    def grow(self, mass_gained):
        self.length += mass_gained
        self.score += mass_gained
        self.update_radius()

    def draw(self, surface, camera_x, camera_y):
        offset_x = -camera_x + SCREEN_WIDTH // 2
        offset_y = -camera_y + SCREEN_HEIGHT // 2
        for i, pos in enumerate(self.positions):
            taper_factor = 1 - (i / len(self.positions)) * 0.7
            segment_radius = max(1, self.radius * taper_factor)
            screen_x = pos.x + offset_x
            screen_y = pos.y + offset_y
            pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), int(segment_radius))
        if self.name:
            name_surface = small_font.render(self.name, True, (255,255,255))
            surface.blit(name_surface, (self.pos.x + offset_x - name_surface.get_width()//2, self.pos.y + offset_y - self.radius - 20))

class Food:
    def __init__(self, x, y, radius, value, color, fid):
        self.pos = pygame.math.Vector2(x, y)
        self.radius = radius
        self.value = value
        self.color = color
        self.id = fid
    def draw(self, surface, camera_x, camera_y):
        screen_x = self.pos.x - camera_x + SCREEN_WIDTH // 2
        screen_y = self.pos.y - camera_y + SCREEN_HEIGHT // 2
        if -self.radius < screen_x < SCREEN_WIDTH + self.radius and -self.radius < screen_y < SCREEN_HEIGHT + self.radius:
            pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), int(self.radius))

# --- UI / Connection screen (same as original) ---
def show_connection_screen():
    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 100, 600, 40)
    name_box = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 30, 600, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    server_text = ''
    name_text = ''
    active_box = 'server'
    title_font = pygame.font.Font(None, 72)
    while True:
        screen.fill(BG_COLOR)
        title = title_font.render('SLITHER.IO MULTIPLAYER', True, (0,255,0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width()//2, 100))
        inst1 = font.render('Enter Server Address', True, (255,255,255))
        inst2 = small_font.render('Example: abc123.ngrok-free.app', True, (200,200,200))
        inst3 = small_font.render('Press TAB to switch fields, ENTER to connect, ESC to quit', True, (150,150,150))
        screen.blit(inst1, (SCREEN_WIDTH//2 - inst1.get_width()//2, SCREEN_HEIGHT//2 - 180))
        screen.blit(inst2, (SCREEN_WIDTH//2 - inst2.get_width()//2, SCREEN_HEIGHT//2 - 140))
        screen.blit(inst3, (SCREEN_WIDTH//2 - inst3.get_width()//2, SCREEN_HEIGHT - 100))
        server_label = small_font.render('Server:', True, (255,255,255))
        screen.blit(server_label, (input_box.x, input_box.y - 25))
        pygame.draw.rect(screen, color_active if active_box=='server' else color_inactive, input_box, 2)
        server_surface = font.render(server_text, True, (255,255,255))
        screen.blit(server_surface, (input_box.x + 5, input_box.y + 5))
        name_label = small_font.render('Your Name:', True, (255,255,255))
        screen.blit(name_label, (name_box.x, name_box.y - 25))
        pygame.draw.rect(screen, color_active if active_box=='name' else color_inactive, name_box, 2)
        name_surface = font.render(name_text, True, (255,255,255))
        screen.blit(name_surface, (name_box.x + 5, name_box.y + 5))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None, None
                elif event.key == pygame.K_TAB:
                    active_box = 'name' if active_box=='server' else 'server'
                elif event.key == pygame.K_RETURN:
                    if server_text and name_text:
                        return server_text, name_text
                elif event.key == pygame.K_BACKSPACE:
                    if active_box=='server':
                        server_text = server_text[:-1]
                    else:
                        name_text = name_text[:-1]
                else:
                    if active_box=='server' and len(server_text)<100:
                        server_text += event.unicode
                    elif active_box=='name' and len(name_text)<20:
                        name_text += event.unicode

# --- Main game (uses network if available) ---
def main():
    server_addr, player_name = show_connection_screen()
    if not server_addr:
        pygame.quit(); return

    # If server string appears to be ngrok/playit use wss, else ws
    if '.ngrok' in server_addr or '.playit' in server_addr:
        server_url = f"wss://{server_addr}"
    elif server_addr.startswith('ws://') or server_addr.startswith('wss://'):
        server_url = server_addr
    else:
        server_url = f"ws://{server_addr}"

    network = NetworkManager()
    network.start(server_url, player_name)

    # Wait up to 10s for connection, otherwise fall back to simulation
    wait_start = time.time()
    while not network.connected and time.time() - wait_start < 10:
        # show connecting screen and allow cancel
        screen.fill(BG_COLOR)
        elapsed = int(time.time() - wait_start)
        msg = font.render(f'Connecting to server... ({elapsed}s)', True, (255,255,255))
        screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, SCREEN_HEIGHT//2))
        inst = small_font.render('Press ESC to cancel and run in local test mode', True, (200,200,200))
        screen.blit(inst, (SCREEN_WIDTH//2 - inst.get_width()//2, SCREEN_HEIGHT//2 + 40))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                network = None
                break
        time.sleep(0.1)

    # Initialize players & foods
    local_player = Player(MAP_SIZE//2, MAP_SIZE//2, is_local=True)
    local_player.name = player_name
    other_players = {}
    foods = []

    # If connected, we'll use network.game_state; otherwise simulate
    simulated = (network is None) or (not network.connected)
    if simulated:
        # spawn bots & foods for local testing
        for i in range(3):
            p = Player(random.randint(100, MAP_SIZE-100), random.randint(100, MAP_SIZE-100))
            p.name = f'Bot{i+1}'
            other_players[i] = p
        for fid in range(200):
            foods.append(Food(random.randint(50, MAP_SIZE-50), random.randint(50, MAP_SIZE-50), random.randint(MIN_FOOD_SIZE, MAX_FOOD_SIZE), random.randint(1,5), (random.randint(50,255), random.randint(50,255), random.randint(50,255)), fid))

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    local_player.boosting = True
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    local_player.boosting = False

        # Update local player
        shed_food = local_player.update(dt)

        # If connected, send update and use server state
        if network and network.connected:
            # send local update
            try:
                network.send_update({
                    'x': local_player.pos.x,
                    'y': local_player.pos.y,
                    'positions': [[p.x, p.y] for p in local_player.positions],
                    'radius': local_player.radius,
                    'length': local_player.length,
                    'score': local_player.score,
                    'shed_food': shed_food
                })
            except Exception:
                pass

            # apply server state
            gs = network.game_state
            foods = [Food(f['x'], f['y'], f['radius'], f['value'], tuple(f['color']), f['id']) for f in gs.get('foods', [])]
            other_players = {}
            for pdata in gs.get('players', []):
                if pdata.get('id') != network.player_id:
                    p = Player(pdata['x'], pdata['y'])
                    p.pos.x = pdata['x']
                    p.pos.y = pdata['y']
                    p.radius = pdata['radius']
                    p.score = pdata['score']
                    p.color = tuple(pdata['color'])
                    p.name = pdata['name']
                    p.positions = [pygame.math.Vector2(xx, yy) for xx, yy in pdata.get('positions', [])]
                    other_players[pdata['id']] = p
        else:
            # local simulation
            local_player.update(dt)
            for p in other_players.values():
                p.update(dt)

            # food collisions (local)
            for food in foods[:]:
                if local_player.pos.distance_to(food.pos) < local_player.radius + food.radius:
                    local_player.grow(food.value)
                    foods.remove(food)
                    foods.append(Food(random.randint(50, MAP_SIZE-50), random.randint(50, MAP_SIZE-50), random.randint(MIN_FOOD_SIZE, MAX_FOOD_SIZE), random.randint(1,5), (random.randint(50,255), random.randint(50,255), random.randint(50,255)), random.randint(1000,9999)))

        # Drawing
        camera_x = local_player.pos.x
        camera_y = local_player.pos.y
        screen.fill(BG_COLOR)
        map_left = -camera_x + SCREEN_WIDTH // 2
        map_top = -camera_y + SCREEN_HEIGHT // 2
        pygame.draw.rect(screen, (100,100,100), (map_left, map_top, MAP_SIZE, MAP_SIZE), 5)
        for x in range(0, MAP_SIZE, 100):
            start_x = x - camera_x + SCREEN_WIDTH // 2
            pygame.draw.line(screen, (40,40,40), (start_x, map_top), (start_x, map_top + MAP_SIZE), 1)
        for y in range(0, MAP_SIZE, 100):
            start_y = y - camera_y + SCREEN_HEIGHT // 2
            pygame.draw.line(screen, (40,40,40), (map_left, start_y), (map_left + MAP_SIZE, start_y), 1)

        for food in foods:
            food.draw(screen, camera_x, camera_y)
        for other in other_players.values():
            other.draw(screen, camera_x, camera_y)
        local_player.draw(screen, camera_x, camera_y)

        score_text = font.render(f'Score: {int(local_player.score)}', True, (255,255,255))
        screen.blit(score_text, (10,10))
        players_text = small_font.render(f'Players: {len(other_players) + 1}', True, (255,255,255))
        screen.blit(players_text, (10,50))

        all_players_scores = [(local_player.name, int(local_player.score))] + [(p.name, int(p.score)) for p in other_players.values()]
        all_players_scores.sort(key=lambda x: x[1], reverse=True)
        leaderboard_title = small_font.render('Leaderboard:', True, (255,255,0))
        screen.blit(leaderboard_title, (10,100))
        for i, (name, score) in enumerate(all_players_scores[:5]):
            text = small_font.render(f'{i+1}. {name}: {score}', True, (255,255,255))
            screen.blit(text, (10,130 + i*25))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
