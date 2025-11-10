import asyncio
import websockets
import json
import random
import time
from collections import defaultdict
from pyngrok import ngrok
import os

# Server Configuration
MAP_SIZE = 3000
INITIAL_FOOD_COUNT = 300
MIN_FOOD_SIZE = 5
MAX_FOOD_SIZE = 15
TICK_RATE = 60  # Server updates per second

class GameServer:
    def __init__(self):
        self.clients = {}  # websocket -> player_data
        self.players = {}  # player_id -> player_state
        self.foods = []
        self.next_player_id = 1
        self.running = True
        self.generate_initial_food()
    
    def generate_initial_food(self):
        for _ in range(INITIAL_FOOD_COUNT):
            self.foods.append(self.create_food())
    
    def create_food(self, is_shed=False, x=None, y=None):
        if x is None or y is None:
            x = random.randint(MAX_FOOD_SIZE, MAP_SIZE - MAX_FOOD_SIZE)
            y = random.randint(MAX_FOOD_SIZE, MAP_SIZE - MAX_FOOD_SIZE)
        
        if is_shed:
            return {
                'id': f'food_{time.time()}_{random.randint(0, 99999)}',
                'x': x,
                'y': y,
                'radius': 4,
                'value': 5,
                'color': [150, 150, 150]
            }
        else:
            radius = random.randint(MIN_FOOD_SIZE, MAX_FOOD_SIZE)
            return {
                'id': f'food_{time.time()}_{random.randint(0, 99999)}',
                'x': x,
                'y': y,
                'radius': radius,
                'value': radius * 2,
                'color': [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)]
            }
    
    def create_player(self, player_id, name):
        return {
            'id': player_id,
            'name': name,
            'x': random.randint(200, MAP_SIZE - 200),
            'y': random.randint(200, MAP_SIZE - 200),
            'radius': 10,
            'score': 0,
            'length': 150,
            'positions': [],
            'color': [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)],
            'alive': True
        }
    
    async def handle_client(self, websocket): # Important note need additional parameter path for older versions of python 
        player_id = None
        try:
            # Wait for initial connection message
            message = await websocket.recv()
            data = json.loads(message)
            
            if data['type'] == 'join':
                player_id = self.next_player_id
                self.next_player_id += 1
                player_name = data.get('name', f'Player {player_id}')
                
                player = self.create_player(player_id, player_name)
                self.players[player_id] = player
                self.clients[websocket] = player_id
                
                # Send player their ID and initial game state
                await websocket.send(json.dumps({
                    'type': 'init',
                    'player_id': player_id,
                    'map_size': MAP_SIZE
                }))
                
                print(f"Player {player_id} ({player_name}) joined")
                
                # Game loop for this client
                async for message in websocket:
                    data = json.loads(message)
                    await self.handle_message(websocket, player_id, data)
        
        except websockets.exceptions.ConnectionClosed:
            pass
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            # Clean up on disconnect
            if player_id and player_id in self.players:
                print(f"Player {player_id} disconnected")
                del self.players[player_id]
            if websocket in self.clients:
                del self.clients[websocket]
    
    async def handle_message(self, websocket, player_id, data):
        if data['type'] == 'update':
            # Update player position and state
            player = self.players.get(player_id)
            if player and player['alive']:
                player['x'] = data['x']
                player['y'] = data['y']
                player['positions'] = data['positions']
                player['radius'] = data['radius']
                player['length'] = data['length']
                player['score'] = data['score']
                
                # Handle shed food
                if 'shed_food' in data and data['shed_food']:
                    shed = data['shed_food']
                    self.foods.append(self.create_food(True, shed['x'], shed['y']))
        
        elif data['type'] == 'eat':
            # Server validates eating
            food_id = data['food_id']
            self.foods = [f for f in self.foods if f['id'] != food_id]
            
            # Spawn new food to maintain count
            if len(self.foods) < INITIAL_FOOD_COUNT + 50:
                self.foods.append(self.create_food())
    
    async def broadcast_game_state(self):
        while self.running:
            if self.clients:
                # Prepare game state
                state = {
                    'type': 'state',
                    'players': list(self.players.values()),
                    'foods': self.foods
                }
                
                message = json.dumps(state)
                
                # Broadcast to all clients
                disconnected = []
                for websocket in self.clients.keys():
                    try:
                        await websocket.send(message)
                    except:
                        disconnected.append(websocket)
                
                # Clean up disconnected clients
                for ws in disconnected:
                    if ws in self.clients:
                        player_id = self.clients[ws]
                        if player_id in self.players:
                            del self.players[player_id]
                        del self.clients[ws]
            
            await asyncio.sleep(1.0 / TICK_RATE)
    
    async def start_server(self, port=8765):
        print("=" * 60)
        print("SLITHER.IO MULTIPLAYER SERVER")
        print("=" * 60)
        
        # Start ngrok tunnel with HTTP (free, no card required!)
        print("\n🔧 Starting ngrok tunnel...")
        try:
            # Kill any existing ngrok processes
            ngrok.kill()
            
            # Use HTTP tunnel instead of TCP (free!)
            public_url = ngrok.connect(port, "http")
            ngrok_address = public_url.public_url.replace("https://", "").replace("http://", "")
            
            print(f"✅ ngrok tunnel established!")
            print(f"\n📡 SERVER ADDRESS: {ngrok_address}")
            print(f"\n👥 Share this address with your friends!")
            print(f"   They should enter: {ngrok_address}")
            print("\n💡 This tunnel will stay active as long as this program runs.")
            print("   You can start/stop it anytime - no need to keep it on 24/7!")
            print("\n⚠️  Note: Free ngrok URLs change each time you restart.")
            print("   (Sign up at ngrok.com for a persistent URL)\n")
            print("=" * 60)
            print("🎮 Server is running! Waiting for players...\n")
            
        except Exception as e:
            print(f"❌ Failed to start ngrok: {e}")
            print("\n💡 Make sure you have ngrok installed:")
            print("   pip install pyngrok")
            print("\n   Or download from: https://ngrok.com/download")
            return
        
        # Start game state broadcast task
        broadcast_task = asyncio.create_task(self.broadcast_game_state())
        
        # Start WebSocket server
        try:
            async with websockets.serve(self.handle_client, 'localhost', port, max_size=10**7):
                print(f"🚀 WebSocket server listening on localhost:{port}")
                print("Press Ctrl+C to stop the server\n")
                await asyncio.Future()  # Run forever
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down server...")
            ngrok.disconnect(public_url.public_url)
            ngrok.kill()
            print("✅ Server stopped successfully!")

if __name__ == "__main__":
    print("\n🎮 Starting Slither.io Multiplayer Server with ngrok...\n")
    server = GameServer()
    try:
        asyncio.run(server.start_server())
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")