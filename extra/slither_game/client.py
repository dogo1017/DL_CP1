import pygame
import math
import random
import asyncio
import websockets
import json
import threading

# --- Initialize Pygame FIRST ---
pygame.init()

# --- Configuration ---
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Slither.io Multiplayer")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# --- Network Manager ---
class NetworkManager:
    def __init__(self):
        self.websocket = None
        self.player_id = None
        self.connected = False
        self.game_state = {'players': [], 'foods': []}
        self.loop = None
        self.thread = None
        
    def start(self, server_url, player_name):
        self.thread = threading.Thread(target=self._run_client, args=(server_url, player_name), daemon=True)
        self.thread.start()
    
    def _run_client(self, server_url, player_name):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._connect(server_url, player_name))
    
    async def _connect(self, server_url, player_name):
        try:
            async with websockets.connect(server_url, max_size=10**7) as websocket:
                self.websocket = websocket
                
                # Send join message
                await websocket.send(json.dumps({
                    'type': 'join',
                    'name': player_name
                }))
                
                # Receive init message
                init_msg = await websocket.recv()
                init_data = json.loads(init_msg)
                self.player_id = init_data['player_id']
                self.connected = True
                print(f"Connected! Player ID: {self.player_id}")
                
                # Listen for game state updates
                async for message in websocket:
                    data = json.loads(message)
                    if data['type'] == 'state':
                        self.game_state = data
        except Exception as e:
            print(f"Connection error: {e}")
            self.connected = False
    
    def send_update(self, player_data):
        if self.websocket and self.connected:
            asyncio.run_coroutine_threadsafe(
                self.websocket.send(json.dumps({
                    'type': 'update',
                    'x': player_data['x'],
                    'y': player_data['y'],
                    'positions': player_data['positions'],
                    'radius': player_data['radius'],
                    'length': player_data['length'],
                    'score': player_data['score'],
                    'shed_food': player_data.get('shed_food')
                })),
                self.loop
            )
    
    def send_eat(self, food_id):
        if self.websocket and self.connected:
            asyncio.run_coroutine_threadsafe(
                self.websocket.send(json.dumps({
                    'type': 'eat',
                    'food_id': food_id
                })),
                self.loop
            )

# --- Classes ---
class Player:
    def __init__(self, x, y, is_local=False):
        self.pos = pygame.math.Vector2(x, y)
        self.radius = INITIAL_PLAYER_RADIUS
        self.score = 0
        self.color = PLAYER_COLOR if is_local else (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
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
        if self.boosting and self.length > 50:
            mass_lost = BOOST_COST_RATE * dt
            self.length -= mass_lost
            self.score -= mass_lost * 0.1
            if len(self.positions) > 10:
                shed_pos = self.positions[-10]
                shed_food_item = {'x': shed_pos.x, 'y': shed_pos.y}
        
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
        
        # Draw name above player
        if self.name:
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
        if -self.radius < screen_x < SCREEN_WIDTH + self.radius and -self.radius < screen_y < SCREEN_HEIGHT + self.radius:
            pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), self.radius)

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
        
        # Title
        title = title_font.render('SLITHER.IO MULTIPLAYER', True, (0, 255, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        # Instructions
        inst1 = font.render('Enter Server Address', True, (255, 255, 255))
        inst2 = font.render('Example: abc123.ngrok-free.app', True, (200, 200, 200))
        inst3 = small_font.render('Press TAB to switch fields, ENTER to connect, ESC to quit', True, (150, 150, 150))
        
        screen.blit(inst1, (SCREEN_WIDTH // 2 - inst1.get_width() // 2, SCREEN_HEIGHT // 2 - 180))
        screen.blit(inst2, (SCREEN_WIDTH // 2 - inst2.get_width() // 2, SCREEN_HEIGHT // 2 - 140))
        screen.blit(inst3, (SCREEN_WIDTH // 2 - inst3.get_width() // 2, SCREEN_HEIGHT - 100))
        
        # Server input
        server_label = small_font.render('Server:', True, (255, 255, 255))
        screen.blit(server_label, (input_box.x, input_box.y - 25))
        pygame.draw.rect(screen, color_active if active_box == 'server' else color_inactive, input_box, 2)
        server_surface = font.render(server_text, True, (255, 255, 255))
        screen.blit(server_surface, (input_box.x + 5, input_box.y + 5))
        
        # Name input
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

# --- Main Game ---
def main():
    # Connection screen
    server_address, player_name = show_connection_screen()
    if not server_address:
        pygame.quit()
        return
    
    # Setup network
    network = NetworkManager()
    # Use wss:// for ngrok, ws:// for direct IP connections
    if '.ngrok' in server_address or '.playit' in server_address:
        server_url = f"wss://{server_address}"
    else:
        server_url = f"ws://{server_address}"
    network.start(server_url, player_name)
    
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
        
        if elapsed > 10:
            screen.fill(BG_COLOR)
            msg = font.render('Connection failed. Press any key to exit.', True, (255, 0, 0))
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            return
        
        pygame.time.wait(100)
    
    # Initialize local player
    local_player = Player(MAP_SIZE // 2, MAP_SIZE // 2, is_local=True)
    local_player.name = player_name
    other_players = {}
    foods = []
    
    # Main game loop
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
        
        # Send update to server
        network.send_update({
            'x': local_player.pos.x,
            'y': local_player.pos.y,
            'positions': [[p.x, p.y] for p in local_player.positions],
            'radius': local_player.radius,
            'length': local_player.length,
            'score': local_player.score,
            'shed_food': shed_food
        })
        
        # Update from server state
        game_state = network.game_state
        
        # Update foods
        foods = [Food(f) for f in game_state.get('foods', [])]
        
        # Check food collisions
        for food in foods:
            distance = local_player.pos.distance_to(food.pos)
            if distance < local_player.radius + food.radius:
                local_player.grow(food.value)
                network.send_eat(food.id)
        
        # Update other players
        other_players.clear()
        for player_data in game_state.get('players', []):
            if player_data['id'] != network.player_id:
                other = Player(player_data['x'], player_data['y'])
                other.pos.x = player_data['x']
                other.pos.y = player_data['y']
                other.radius = player_data['radius']
                other.score = player_data['score']
                other.color = tuple(player_data['color'])
                other.name = player_data['name']
                other.positions = [pygame.math.Vector2(p[0], p[1]) for p in player_data['positions']]
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
        
        players_text = small_font.render(f'Players: {len(other_players) + 1}', True, (255, 255, 255))
        screen.blit(players_text, (10, 50))
        
        # Draw leaderboard
        all_players_scores = [(local_player.name, int(local_player.score))] + \
                            [(p.name, int(p.score)) for p in other_players.values()]
        all_players_scores.sort(key=lambda x: x[1], reverse=True)
        
        leaderboard_y = 100
        leaderboard_title = small_font.render('Leaderboard:', True, (255, 255, 0))
        screen.blit(leaderboard_title, (10, leaderboard_y))
        for i, (name, score) in enumerate(all_players_scores[:5]):
            text = small_font.render(f'{i+1}. {name}: {score}', True, (255, 255, 255))
            screen.blit(text, (10, leaderboard_y + 30 + i * 25))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()