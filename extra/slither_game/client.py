import pygame
import math
import random
import asyncio
import websockets
import json
import threading
import time


pygame.init()


infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

PLAYER_BASE_SPEED = 200
BOOST_SPEED_MULTIPLIER = 1.6
BOOST_COST_RATE = 100
MIN_FOOD_SIZE = 5
MAX_FOOD_SIZE = 15
INITIAL_PLAYER_RADIUS = 10
INITIAL_LENGTH = 150
MAX_LENGTH = 1500
GROWTH_SLOWDOWN_FACTOR = 0.5
BG_COLOR = (20, 20, 20)
MAP_SIZE = 3000


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slither.io Multiplayer")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)


class NetworkManager:
    def __init__(self):
        self.websocket = None
        self.player_id = None
        self.connected = False
        self.game_state = {'players': [], 'foods': [], 'timestamp': 0}
        self.loop = None
        self.thread = None
        self.last_state_time = 0
        
    def start(self, server_url, player_name, player_color):
        self.player_name = player_name
        self.player_color = player_color
        self.server_url = server_url
        self.thread = threading.Thread(target=self._run_client, daemon=True)
        self.thread.start()
    
    def _run_client(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._connect())
    
    async def _connect(self):
        print(f"[CLIENT] Attempting to connect to {self.server_url}")
        try:
            ### Add extra headers for ngrok
            ###extra_headers = {}
            ###if 'ngrok' in self.server_url:
            ###    extra_headers = {
            ###        'User-Agent': 'Python/Slither-Client',
            ###        'ngrok-skip-browser-warning': 'true'
            ###    }
            
            async with websockets.connect(
                self.server_url, 
                max_size=10**7, 
                ping_interval=20, 
                ping_timeout=10,
                ###extra_headers=extra_headers
            ) as websocket:
                self.websocket = websocket
                print(f"[CLIENT] WebSocket connected!")
                

                join_msg = {
                    'type': 'join',
                    'name': self.player_name,
                    'color': self.player_color
                }
                print(f"[CLIENT] Sending join: {join_msg}")
                await websocket.send(json.dumps(join_msg))
                

                print(f"[CLIENT] Waiting for init message...")
                init_msg = await websocket.recv()
                init_data = json.loads(init_msg)
                print(f"[CLIENT] Received init: {init_data}")
                
                if init_data['type'] == 'init':
                    self.player_id = init_data['player_id']
                    self.connected = True
                    print(f"[CLIENT] Connected! Player ID: {self.player_id}")
                

                message_count = 0
                async for message in websocket:
                    try:
                        data = json.loads(message)
                        if data['type'] == 'state':
                            self.game_state = data
                            self.last_state_time = time.time()
                            message_count += 1

                            if message_count % 30 == 0:
                                print(f"[CLIENT] State received: {len(data.get('players', []))} players, {len(data.get('foods', []))} food")
                    except json.JSONDecodeError:
                        print(f"[CLIENT] Invalid JSON received")
                        
        except Exception as e:
            print(f"[CLIENT] Connection error: {e}")
            import traceback
            traceback.print_exc()
            self.connected = False
    
    def send_update(self, player_data):
        if self.websocket and self.connected and self.loop:
            try:
                msg = {
                    'type': 'update',
                    'x': player_data['x'],
                    'y': player_data['y'],
                    'positions': player_data['positions'],
                    'radius': player_data['radius'],
                    'length': player_data['length'],
                    'score': player_data['score'],
                    'alive': player_data['alive'],
                    'shed_food': player_data.get('shed_food')
                }
                future = asyncio.run_coroutine_threadsafe(
                    self.websocket.send(json.dumps(msg)),
                    self.loop
                )

                future.result(timeout=0.01)
            except Exception as e:

                pass
    
    def send_eat(self, food_id):
        if self.websocket and self.connected and self.loop:
            try:
                future = asyncio.run_coroutine_threadsafe(
                    self.websocket.send(json.dumps({
                        'type': 'eat',
                        'food_id': food_id
                    })),
                    self.loop
                )
                future.result(timeout=0.01)
            except Exception as e:
                pass
    
    def send_respawn(self, color):
        if self.websocket and self.connected and self.loop:
            try:
                future = asyncio.run_coroutine_threadsafe(
                    self.websocket.send(json.dumps({
                        'type': 'respawn',
                        'color': color
                    })),
                    self.loop
                )
                future.result(timeout=0.01)
                print(f"[CLIENT] Sent respawn request")
            except Exception as e:
                print(f"[CLIENT] Error sending respawn: {e}")


class Player:
    def __init__(self, x, y, color, is_local=False):
        self.pos = pygame.math.Vector2(x, y)
        self.radius = INITIAL_PLAYER_RADIUS
        self.score = 0
        self.color = color
        self.length = INITIAL_LENGTH
        self.base_speed = PLAYER_BASE_SPEED
        self.speed = self.base_speed
        self.positions = [self.pos.copy()] * int(self.length)
        self.boosting = False
        self.is_local = is_local
        self.name = ""
        self.alive = True
    
    def update(self, dt):
        if not self.is_local or not self.alive:
            return None
        
        # Speed calculation with size penalty
        speed_multiplier = BOOST_SPEED_MULTIPLIER if self.boosting else 1.0
        size_multiplier = max(0.3, (INITIAL_PLAYER_RADIUS / self.radius) ** 0.8)
        self.speed = self.base_speed * size_multiplier * speed_multiplier
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        target = pygame.math.Vector2(mouse_x - SCREEN_WIDTH // 2, mouse_y - SCREEN_HEIGHT // 2)
        
        if target.length_squared() > 0:
            direction = target.normalize()
            self.pos += direction * self.speed * dt
        
        self.pos.x = max(self.radius, min(MAP_SIZE - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(MAP_SIZE - self.radius, self.pos.y))
        
        shed_food_item = None
        if self.boosting and self.length > 50:
            mass_lost = BOOST_COST_RATE * dt
            self.length -= mass_lost
            self.score = max(0, self.score - mass_lost * 0.1)
            if len(self.positions) > 10:
                shed_pos = self.positions[-10]
                shed_food_item = {'x': shed_pos.x, 'y': shed_pos.y}
        
        # Update positions - smooth body movement
        self.positions.insert(0, self.pos.copy())
        target_length = int(self.length)
        if len(self.positions) > target_length:
            self.positions = self.positions[:target_length]
        elif len(self.positions) < target_length:
            while len(self.positions) < target_length:
                self.positions.append(self.positions[-1].copy())
        
        self.update_radius()
        return shed_food_item
    
    def update_radius(self):
        self.radius = INITIAL_PLAYER_RADIUS + math.sqrt(self.length / 10.0)
    
    def grow(self, mass_gained):
        effective_gain = mass_gained * GROWTH_SLOWDOWN_FACTOR
        self.length = min(MAX_LENGTH, self.length + effective_gain)
        self.score += effective_gain
        self.update_radius()
    
    def draw(self, surface, camera_x, camera_y):
        offset_x = -camera_x + SCREEN_WIDTH // 2
        offset_y = -camera_y + SCREEN_HEIGHT // 2
        
        # Draw body segments
        for i, pos in enumerate(self.positions):
            taper_factor = 1 - (i / len(self.positions)) * 0.7
            segment_radius = max(1, self.radius * taper_factor)
            screen_x = pos.x + offset_x
            screen_y = pos.y + offset_y
            
            if -segment_radius < screen_x < SCREEN_WIDTH + segment_radius and \
               -segment_radius < screen_y < SCREEN_HEIGHT + segment_radius:
                pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), int(segment_radius))
        
        # Draw name above player head
        if self.name and self.alive:
            name_surface = small_font.render(self.name, True, (255, 255, 255))
            name_x = self.pos.x + offset_x - name_surface.get_width() // 2
            name_y = self.pos.y + offset_y - self.radius - 20
            surface.blit(name_surface, (name_x, name_y))

class Food:
    def __init__(self, food_data):
        self.pos = pygame.math.Vector2(food_data['x'], food_data['y'])
        self.radius = food_data['radius']
        self.value = food_data['value']
        self.color = tuple(food_data['color'])
        self.id = food_data['id']
    
    def draw(self, surface, camera_x, camera_y):
        screen_x = self.pos.x - camera_x + SCREEN_WIDTH // 2
        screen_y = self.pos.y - camera_y + SCREEN_HEIGHT // 2
        if -self.radius < screen_x < SCREEN_WIDTH + self.radius and \
           -self.radius < screen_y < SCREEN_HEIGHT + self.radius:
            pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), self.radius)

# --- Color Picker Screen ---
def show_color_picker():
    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (255, 0, 255), (0, 255, 255),
        (255, 128, 0), (128, 0, 255), (0, 255, 128),
        (255, 192, 203), (128, 128, 128), (255, 255, 255)
    ]
    
    selected_color = colors[1]
    color_boxes = []
    
    start_x = SCREEN_WIDTH // 2 - 300
    start_y = SCREEN_HEIGHT // 2 - 50
    for i, color in enumerate(colors):
        x = start_x + (i % 6) * 100
        y = start_y + (i // 6) * 100
        color_boxes.append((pygame.Rect(x, y, 80, 80), color))
    
    while True:
        screen.fill(BG_COLOR)
        
        title = font.render('Choose Your Color', True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, start_y - 100))
        
        for box, color in color_boxes:
            pygame.draw.rect(screen, color, box)
            if color == selected_color:
                pygame.draw.rect(screen, (255, 255, 255), box, 5)
            else:
                pygame.draw.rect(screen, (100, 100, 100), box, 2)
        
        inst = small_font.render('Click a color, then press ENTER to continue', True, (200, 200, 200))
        screen.blit(inst, (SCREEN_WIDTH // 2 - inst.get_width() // 2, start_y + 230))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for box, color in color_boxes:
                    if box.collidepoint(mouse_pos):
                        selected_color = color
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return list(selected_color)
                if event.key == pygame.K_ESCAPE:
                    return None

# --- Connection Screen ---
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
        
        title = title_font.render('SLITHER.IO MULTIPLAYER', True, (0, 255, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        inst1 = font.render('Enter Server Address', True, (255, 255, 255))
        inst2 = font.render('Example: abc123.ngrok-free.app', True, (200, 200, 200))
        inst3 = small_font.render('Press TAB to switch fields, ENTER to connect, ESC to quit', True, (150, 150, 150))
        
        screen.blit(inst1, (SCREEN_WIDTH // 2 - inst1.get_width() // 2, SCREEN_HEIGHT // 2 - 180))
        screen.blit(inst2, (SCREEN_WIDTH // 2 - inst2.get_width() // 2, SCREEN_HEIGHT // 2 - 140))
        screen.blit(inst3, (SCREEN_WIDTH // 2 - inst3.get_width() // 2, SCREEN_HEIGHT - 100))
        
        server_label = small_font.render('Server:', True, (255, 255, 255))
        screen.blit(server_label, (input_box.x, input_box.y - 25))
        pygame.draw.rect(screen, color_active if active_box == 'server' else color_inactive, input_box, 2)
        server_surface = font.render(server_text, True, (255, 255, 255))
        screen.blit(server_surface, (input_box.x + 5, input_box.y + 5))
        
        name_label = small_font.render('Your Name:', True, (255, 255, 255))
        screen.blit(name_label, (name_box.x, name_box.y - 25))
        pygame.draw.rect(screen, color_active if active_box == 'name' else color_inactive, name_box, 2)
        name_surface = font.render(name_text, True, (255, 255, 255))
        screen.blit(name_surface, (name_box.x + 5, name_box.y + 5))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None, None
                elif event.key == pygame.K_TAB:
                    active_box = 'name' if active_box == 'server' else 'server'
                elif event.key == pygame.K_RETURN:
                    if server_text and name_text:
                        return server_text, name_text
                elif event.key == pygame.K_BACKSPACE:
                    if active_box == 'server':
                        server_text = server_text[:-1]
                    else:
                        name_text = name_text[:-1]
                else:
                    if active_box == 'server' and len(server_text) < 100:
                        server_text += event.unicode
                    elif active_box == 'name' and len(name_text) < 20:
                        name_text += event.unicode

def show_death_screen(score, respawn_time):
    """Show death screen with countdown"""
    while respawn_time > 0:
        screen.fill(BG_COLOR)
        
        death_text = font.render('YOU DIED!', True, (255, 0, 0))
        score_text = font.render(f'Final Score: {int(score)}', True, (255, 255, 255))
        respawn_text = small_font.render(f'Respawning in {int(respawn_time)} seconds...', True, (200, 200, 200))
        
        screen.blit(death_text, (SCREEN_WIDTH // 2 - death_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(respawn_text, (SCREEN_WIDTH // 2 - respawn_text.get_width() // 2, SCREEN_HEIGHT // 2 + 30))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        pygame.time.wait(100)
        respawn_time -= 0.1
    
    return True

# --- Main Game ---
def main():
    # Connection screen
    server_address, player_name = show_connection_screen()
    if not server_address:
        pygame.quit()
        return
    
    # Color picker
    player_color = show_color_picker()
    if not player_color:
        pygame.quit()
        return
    
    print(f"[CLIENT] Selected color: {player_color}")
    
    # Setup network
    network = NetworkManager()
    if '.ngrok' in server_address or '.playit' in server_address:
        server_url = f"wss://{server_address}"
    else:
        server_url = f"ws://{server_address}"
    
    print(f"[CLIENT] Starting network connection to {server_url}")
    network.start(server_url, player_name, player_color)
    
    # Wait for connection
    waiting_start = pygame.time.get_ticks()
    while not network.connected:
        screen.fill(BG_COLOR)
        elapsed = (pygame.time.get_ticks() - waiting_start) // 1000
        msg = font.render(f'Connecting to server... ({elapsed}s)', True, (255, 255, 255))
        screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return
        
        if elapsed > 15:
            screen.fill(BG_COLOR)
            msg = font.render('Connection failed. Check server address.', True, (255, 0, 0))
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            return
        
        pygame.time.wait(100)
    
    print(f"[CLIENT] Connected successfully! Player ID: {network.player_id}")
    
    # Initialize local player
    local_player = Player(MAP_SIZE // 2, MAP_SIZE // 2, player_color, is_local=True)
    local_player.name = player_name
    other_players = {}
    foods = []
    
            # Main game loop
    running = True
    update_counter = 0
    last_debug_time = time.time()
    
    while running:
        dt = clock.tick(60) / 1000.0
        update_counter += 1
        
        # Debug output every 2 seconds
        if time.time() - last_debug_time > 2.0:
            game_state = network.game_state.copy()
            print(f"[CLIENT GAME] Players in state: {len(game_state.get('players', []))}, Foods: {len(game_state.get('foods', []))}")
            print(f"[CLIENT GAME] Connected: {network.connected}, Player ID: {network.player_id}")
            last_debug_time = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and local_player.alive:
                    local_player.boosting = True
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    local_player.boosting = False
        
        # Update local player
        if local_player.alive:
            shed_food = local_player.update(dt)
            
            # Send update to server
            network.send_update({
                'x': local_player.pos.x,
                'y': local_player.pos.y,
                'positions': [[p.x, p.y] for p in local_player.positions],
                'radius': local_player.radius,
                'length': local_player.length,
                'score': local_player.score,
                'alive': local_player.alive,
                'shed_food': shed_food
            })
        
        # Get game state from server
        game_state = network.game_state.copy()
        
        # Check if local player died on server
        for player_data in game_state.get('players', []):
            if player_data['id'] == network.player_id and not player_data['alive'] and local_player.alive:
                local_player.alive = False
                if show_death_screen(local_player.score, 5.0):
                    new_color = show_color_picker()
                    if new_color:
                        network.send_respawn(new_color)
                        pygame.time.wait(500)
                        local_player = Player(MAP_SIZE // 2, MAP_SIZE // 2, new_color, is_local=True)
                        local_player.name = player_name
                else:
                    running = False
        
        # Update foods from server
        foods = [Food(f) for f in game_state.get('foods', [])]
        
        # Check food collisions
        if local_player.alive:
            for food in foods[:]:
                distance = local_player.pos.distance_to(food.pos)
                if distance < local_player.radius + food.radius:
                    local_player.grow(food.value)
                    network.send_eat(food.id)
        
        # Update other players from server
        other_players.clear()
        for player_data in game_state.get('players', []):
            if player_data['id'] != network.player_id and player_data.get('alive', True):
                other = Player(player_data['x'], player_data['y'], tuple(player_data['color']))
                other.pos.x = player_data['x']
                other.pos.y = player_data['y']
                other.radius = player_data['radius']
                other.score = player_data['score']
                other.name = player_data['name']
                other.alive = player_data.get('alive', True)
                if player_data.get('positions'):
                    other.positions = [pygame.math.Vector2(p[0], p[1]) for p in player_data['positions']]
                else:
                    other.positions = [other.pos.copy()] * int(player_data.get('length', 150))
                other_players[player_data['id']] = other
        
        # Camera
        camera_x = local_player.pos.x
        camera_y = local_player.pos.y
        
        # Drawing
        screen.fill(BG_COLOR)
        
        # Draw map boundary
        map_left = -camera_x + SCREEN_WIDTH // 2
        map_top = -camera_y + SCREEN_HEIGHT // 2
        pygame.draw.rect(screen, (100, 100, 100), (map_left, map_top, MAP_SIZE, MAP_SIZE), 5)
        
        # Draw grid
        for x in range(0, MAP_SIZE, 100):
            start_x = x - camera_x + SCREEN_WIDTH // 2
            pygame.draw.line(screen, (40, 40, 40), (start_x, map_top), (start_x, map_top + MAP_SIZE), 1)
        for y in range(0, MAP_SIZE, 100):
            start_y = y - camera_y + SCREEN_HEIGHT // 2
            pygame.draw.line(screen, (40, 40, 40), (map_left, start_y), (map_left + MAP_SIZE, start_y), 1)
        
        # Draw food
        for food in foods:
            food.draw(screen, camera_x, camera_y)
        
        # Draw other players
        for other in other_players.values():
            other.draw(screen, camera_x, camera_y)
        
        # Draw local player
        local_player.draw(screen, camera_x, camera_y)
        
        # Draw HUD
        score_text = font.render(f'Score: {int(local_player.score)}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        total_players = len(other_players) + (1 if local_player.alive else 0)
        players_text = small_font.render(f'Players: {total_players}', True, (255, 255, 255))
        screen.blit(players_text, (10, 50))
        
        length_text = small_font.render(f'Length: {int(local_player.length)}/{MAX_LENGTH}', True, (255, 255, 255))
        screen.blit(length_text, (10, 80))
        
        # Connection indicator
        time_since_state = time.time() - network.last_state_time
        if time_since_state > 2:
            conn_text = small_font.render('Connection Lost!', True, (255, 0, 0))
        else:
            conn_text = small_font.render('Connected', True, (0, 255, 0))
        screen.blit(conn_text, (SCREEN_WIDTH - 150, 10))
        
        # Draw leaderboard
        all_players_scores = [(local_player.name, int(local_player.score))] + \
                            [(p.name, int(p.score)) for p in other_players.values()]
        all_players_scores.sort(key=lambda x: x[1], reverse=True)
        
        leaderboard_y = 120
        leaderboard_title = small_font.render('Leaderboard:', True, (255, 255, 0))
        screen.blit(leaderboard_title, (10, leaderboard_y))
        for i, (name, score) in enumerate(all_players_scores[:5]):
            text = small_font.render(f'{i+1}. {name}: {score}', True, (255, 255, 255))
            screen.blit(text, (10, leaderboard_y + 30 + i * 25))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()