# DL 1st, final project - Refactored without global variables

import json
import os
import time
import random
import sys
from io import StringIO

class GameState:
    """Holds all game state to avoid global variables"""
    def __init__(self):
        # Scene management
        self.captured_output = StringIO()
        self.current_scene_log = []
        
        # Game progress
        self.defeated_trainers = []
        self.collected_items = {}
        self.gym_badges = []
        self.player_money = 500
        self.player_inv = []
        self.current_location = "Pallet Town"
        
        # Player's pokemon
        self.player_pokemon = {
            1: {
                "nickname": "Flamey",
                "species_name": "Charmander",
                "level": 5,
                "type": ["fire"],
                "hp": 20,
                "max_hp": 20,
                "atk": 8,
                "defense": 5,
                "speed": 7,
                "exp": 0,
                "exp_to_next": 100,
                "moves": ["Scratch","Ember"],
                "gender": "male",
                "pokedex_inv_id": 1
            }
        }
        
        # Discovered locations
        self.discovered_locations = {
            "Pallet Town": True,
            "Route 1": False,
            "Viridian City": False,
            "Route 2": False,
            "Pewter City": False,
            "Route 3": False,
            "Cerulean City": False,
            "Route 4": False,
            "Vermilion City": False,
            "Route 5": False,
            "Lavender Town": False,
            "Route 6": False,
            "Celadon City": False,
            "Route 7": False,
            "Fuchsia City": False,
            "Route 8": False,
            "Saffron City": False,
            "Route 9": False,
            "Cinnabar Island": False,
        }

# Static data (these can remain as module-level constants since they don't change)
title_ascii = """ _____   ____  _  ________ __  __  ____  _   _                     
|  __ \\ / __ \\| |/ /  ____|  \\/  |/ __ \\| \\ | |_                   
| |__) | |  | | ' /| |__  | \\  / | |  | |  \\| (_)                  
|  ___/| |  | |  < |  __| | |\\/| | |  | | . ` |                    
| |    | |__| | . \\| |____| |  | | |__| | |\\  |_                   
|_|     \\____/|_|\\_\\______|_| _|_|\\____/|_| \\_(_)_   _             
| |             | |          | |            | (_) | (_)            
| |__  _   _  __| | __ _  ___| |_    ___  __| |_| |_ _  ___  _ __  
| '_ \\| | | |/ _` |/ _` |/ _ \\ __|  / _ \\/ _` | | __| |/ _ \\| '_ \\ 
| |_) | |_| | (_| | (_| |  __/ |_  |  __/ (_| | | |_| | (_) | | | |
|_.__/ \\__,_|\\__,_|\\__, |\\___|\\__|  \\___|\\__,_|_|\\__|_|\\___/|_| |_|
                    __/ |                                          
                   |___/                                           """

original_pokemon_data = {
    "Charmander": {
        "species_name": "Charmander",
        "type": ["fire"],
        "base_hp": 20,
        "base_atk": 8,
        "base_defense": 5,
        "base_speed": 7,
        "evolutions": [{"to":"Charmeleon","level":16}],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "1",
        "possible_moves": ["Scratch","Ember","Flamethrower"]
    },
    "Bulbasaur": {
        "species_name": "Bulbasaur",
        "type": ["grass"],
        "base_hp": 21,
        "base_atk": 7,
        "base_defense": 6,
        "base_speed": 6,
        "evolutions": [{"to":"Ivysaur","level":16}],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "2",
        "possible_moves": ["Tackle","Vine Whip","Growl"]
    },
    "Squirtle": {
        "species_name": "Squirtle",
        "type": ["water"],
        "base_hp": 20,
        "base_atk": 7,
        "base_defense": 7,
        "base_speed": 6,
        "evolutions": [{"to":"Wartortle","level":16}],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "3",
        "possible_moves": ["Tackle","Water Gun","Bubble"]
    },
    "Pidgey": {
        "species_name": "Pidgey",
        "type": ["flying"],
        "base_hp": 18,
        "base_atk": 6,
        "base_defense": 5,
        "base_speed": 8,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "4",
        "possible_moves": ["Peck","Gust"]
    },
    "Rattata": {
        "species_name": "Rattata",
        "type": ["normal"],
        "base_hp": 16,
        "base_atk": 7,
        "base_defense": 4,
        "base_speed": 9,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "5",
        "possible_moves": ["Tackle","Quick Attack"]
    },
    "Caterpie": {
        "species_name": "Caterpie",
        "type": ["bug"],
        "base_hp": 19,
        "base_atk": 5,
        "base_defense": 4,
        "base_speed": 6,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "6",
        "possible_moves": ["Tackle","String Shot"]
    },
    "Geodude": {
        "species_name": "Geodude",
        "type": ["rock"],
        "base_hp": 20,
        "base_atk": 9,
        "base_defense": 8,
        "base_speed": 4,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "7",
        "possible_moves": ["Tackle","Rock Throw"]
    },
    "Magikarp": {
        "species_name": "Magikarp",
        "type": ["water"],
        "base_hp": 15,
        "base_atk": 3,
        "base_defense": 6,
        "base_speed": 10,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "8",
        "possible_moves": ["Splash","Tackle"]
    },
    "Pikachu": {
        "species_name": "Pikachu",
        "type": ["electric"],
        "base_hp": 18,
        "base_atk": 8,
        "base_defense": 5,
        "base_speed": 11,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "9",
        "possible_moves": ["Thunder Shock","Quick Attack"]
    },
    "Gastly": {
        "species_name": "Gastly",
        "type": ["ghost"],
        "base_hp": 16,
        "base_atk": 9,
        "base_defense": 4,
        "base_speed": 10,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "10",
        "possible_moves": ["Lick","Night Shade"]
    },
    "Oddish": {
        "species_name": "Oddish",
        "type": ["grass"],
        "base_hp": 19,
        "base_atk": 7,
        "base_defense": 6,
        "base_speed": 5,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "11",
        "possible_moves": ["Absorb","Acid"]
    },
    "Mewtwo": {
        "species_name": "Mewtwo",
        "type": ["psychic"],
        "base_hp": 50,
        "base_atk": 20,
        "base_defense": 15,
        "base_speed": 18,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "12",
        "possible_moves": ["Psychic","Swift","Recover"]
    }
}

moves_data = {
    "Scratch": {"power": 5},
    "Ember": {"power": 7},
    "Flamethrower": {"power": 10},
    "Tackle": {"power": 5},
    "Vine Whip": {"power": 7},
    "Growl": {"power": 0},
    "Water Gun": {"power": 7},
    "Bubble": {"power": 6},
    "Peck": {"power": 6},
    "Gust": {"power": 7},
    "Quick Attack": {"power": 6},
    "String Shot": {"power": 0},
    "Rock Throw": {"power": 8},
    "Splash": {"power": 0},
    "Thunder Shock": {"power": 7},
    "Lick": {"power": 6},
    "Night Shade": {"power": 8},
    "Absorb": {"power": 6},
    "Acid": {"power": 6},
    "Psychic": {"power": 12},
    "Swift": {"power": 8},
    "Recover": {"power": 0}
}

starter_pokemon = ["Charmander", "Bulbasaur", "Squirtle"]

items = {
    "Health Potion": {
        "stat": "health",
        "target": "curr_pokemon",
        "value": 20,
        "sale_price": 50,
        "description": "Restores 20 HP to a Pokemon"
    },
    "Super Potion": {
        "stat": "health",
        "target": "curr_pokemon",
        "value": 50,
        "sale_price": 100,
        "description": "Restores 50 HP to a Pokemon"
    },
    "Pokeball": {
        "stat": "capture",
        "target": "wild_pokemon",
        "value": 0.3,
        "sale_price": 200,
        "description": "Used to catch wild Pokemon"
    },
    "Protein": {
        "stat": "atk",
        "target": "curr_pokemon",
        "value": 2,
        "sale_price": 300,
        "description": "Permanently increases Attack by 2"
    },
    "Iron": {
        "stat": "defense",
        "target": "curr_pokemon",
        "value": 2,
        "sale_price": 300,
        "description": "Permanently increases Defense by 2"
    },
    "Carbos": {
        "stat": "speed",
        "target": "curr_pokemon",
        "value": 2,
        "sale_price": 300,
        "description": "Permanently increases Speed by 2"
    },
    "Fire Stone": {
        "stat": "evolution",
        "target": "curr_pokemon",
        "value": "fire",
        "sale_price": 500,
        "description": "Evolves certain fire-type Pokemon"
    }
}

cities = {
    "Pallet Town": {
        "shops": ["General Store"],
        "healing_center": True,
        "gym": False,
        "special_area": "Grassy Fields",
        "description": "A quiet town where your journey begins.",
        "gym_leader": None
    },
    "Viridian City": {
        "shops": ["Potion Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Viridian Forest",
        "description": "A city surrounded by lush forests.",
        "gym_leader": {"name": "Giovanni", "type": "normal", "badge": "Earth Badge"}
    },
    "Pewter City": {
        "shops": ["Rock Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Rocky Mountains",
        "description": "A city known for its rocky terrain.",
        "gym_leader": {"name": "Brock", "type": "rock", "badge": "Boulder Badge"}
    },
    "Cerulean City": {
        "shops": ["Water Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Cerulean Cave",
        "description": "A city by the water with a mysterious cave.",
        "gym_leader": {"name": "Misty", "type": "water", "badge": "Cascade Badge"}
    },
    "Vermilion City": {
        "shops": ["Electric Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Port Docks",
        "description": "A port city with electric energy.",
        "gym_leader": {"name": "Lt. Surge", "type": "electric", "badge": "Thunder Badge"}
    },
    "Lavender Town": {
        "shops": ["Mysterious Shop"],
        "healing_center": True,
        "gym": False,
        "special_area": "Pokemon Tower",
        "description": "A quiet, eerie town with a haunted tower.",
        "gym_leader": None
    },
    "Celadon City": {
        "shops": ["Mega Store", "Evolution Stones"],
        "healing_center": True,
        "gym": True,
        "special_area": "Game Corner",
        "description": "The biggest city with a huge department store.",
        "gym_leader": {"name": "Erika", "type": "grass", "badge": "Rainbow Badge"}
    },
    "Fuchsia City": {
        "shops": ["Safari Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Safari Zone",
        "description": "A city with an exotic safari zone.",
        "gym_leader": {"name": "Koga", "type": "poison", "badge": "Soul Badge"}
    },
    "Saffron City": {
        "shops": ["Psychic Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Silph Co. Building",
        "description": "A bustling metropolis with psychic energy.",
        "gym_leader": {"name": "Sabrina", "type": "psychic", "badge": "Marsh Badge"}
    },
    "Cinnabar Island": {
        "shops": ["Volcano Shop"],
        "healing_center": True,
        "gym": True,
        "special_area": "Volcano Cave",
        "description": "An island with an active volcano and secret labs.",
        "gym_leader": {"name": "Blaine", "type": "fire", "badge": "Volcano Badge"}
    }
}

special_areas = {
    "Grassy Fields": {
        "pokemon_types": ["grass", "normal", "flying"],
        "pokemon_pool": ["Pidgey", "Rattata"],
        "pokemon_lvl_range": (3, 6),
        "items": ["Health Potion", "Pokeball"]
    },
    "Viridian Forest": {
        "pokemon_types": ["bug", "grass"],
        "pokemon_pool": ["Caterpie", "Pidgey"],
        "pokemon_lvl_range": (5, 8),
        "items": ["Health Potion", "Super Potion"]
    },
    "Rocky Mountains": {
        "pokemon_types": ["rock", "ground"],
        "pokemon_pool": ["Geodude"],
        "pokemon_lvl_range": (8, 12),
        "items": ["Protein", "Iron"]
    },
    "Cerulean Cave": {
        "pokemon_types": ["water", "psychic"],
        "pokemon_pool": ["Magikarp", "Gastly"],
        "pokemon_lvl_range": (10, 15),
        "items": ["Super Potion", "Pokeball"],
        "special": "mewtwo_location"
    },
    "Port Docks": {
        "pokemon_types": ["water", "electric"],
        "pokemon_pool": ["Magikarp", "Pikachu"],
        "pokemon_lvl_range": (12, 16),
        "items": ["Health Potion", "Carbos"]
    },
    "Pokemon Tower": {
        "pokemon_types": ["ghost"],
        "pokemon_pool": ["Gastly"],
        "pokemon_lvl_range": (15, 20),
        "items": ["Super Potion"]
    },
    "Game Corner": {
        "pokemon_types": ["normal"],
        "pokemon_pool": ["Rattata", "Pidgey"],
        "pokemon_lvl_range": (10, 15),
        "items": ["Health Potion", "Pokeball"]
    },
    "Safari Zone": {
        "pokemon_types": ["grass", "normal", "water"],
        "pokemon_pool": ["Oddish", "Pidgey", "Magikarp"],
        "pokemon_lvl_range": (18, 25),
        "items": ["Super Potion", "Pokeball", "Protein"]
    },
    "Silph Co. Building": {
        "pokemon_types": ["normal"],
        "pokemon_pool": ["Rattata"],
        "pokemon_lvl_range": (20, 25),
        "items": ["Iron", "Carbos"]
    },
    "Volcano Cave": {
        "pokemon_types": ["fire"],
        "pokemon_pool": ["Charmander"],
        "pokemon_lvl_range": (25, 30),
        "items": ["Fire Stone", "Super Potion"]
    }
}

routes = {
    "Route 1": {
        "connects": ["Pallet Town", "Viridian City"],
        "distance": 3,
        "pokemon_pool": ["Pidgey", "Rattata"],
        "trainer_chance": 0.3
    },
    "Route 2": {
        "connects": ["Viridian City", "Pewter City"],
        "distance": 4,
        "pokemon_pool": ["Pidgey", "Caterpie"],
        "trainer_chance": 0.4
    },
    "Route 3": {
        "connects": ["Pewter City", "Cerulean City"],
        "distance": 5,
        "pokemon_pool": ["Geodude", "Pidgey"],
        "trainer_chance": 0.4
    },
    "Route 4": {
        "connects": ["Cerulean City", "Vermilion City"],
        "distance": 4,
        "pokemon_pool": ["Magikarp", "Pikachu"],
        "trainer_chance": 0.3
    },
    "Route 5": {
        "connects": ["Vermilion City", "Lavender Town"],
        "distance": 3,
        "pokemon_pool": ["Pidgey", "Gastly"],
        "trainer_chance": 0.3
    },
    "Route 6": {
        "connects": ["Lavender Town", "Celadon City"],
        "distance": 4,
        "pokemon_pool": ["Oddish", "Pidgey"],
        "trainer_chance": 0.4
    },
    "Route 7": {
        "connects": ["Celadon City", "Fuchsia City"],
        "distance": 5,
        "pokemon_pool": ["Oddish", "Rattata"],
        "trainer_chance": 0.4
    },
    "Route 8": {
        "connects": ["Fuchsia City", "Saffron City"],
        "distance": 4,
        "pokemon_pool": ["Gastly", "Pidgey"],
        "trainer_chance": 0.5
    },
    "Route 9": {
        "connects": ["Saffron City", "Cinnabar Island"],
        "distance": 6,
        "pokemon_pool": ["Charmander", "Geodude"],
        "trainer_chance": 0.5
    }
}

# Utility functions
def index_of_lists(list):
    indexes = []
    for i in list:
        indexes.append(list.index(i)+1)
    return indexes

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def new_scene(state):
    """Start a new scene: clears terminal and resets scene log."""
    state.captured_output = StringIO()
    state.current_scene_log = []
    clear_screen()

def restore_scene(state):
    """Restore the current scene to terminal."""
    clear_screen()
    for line in state.current_scene_log:
        print(line)

def log_print(state, message):
    """Print live AND save message to current scene."""
    print(message)
    state.current_scene_log.append(message)

def text(state, message, delay=0.02):
    """Typewriter effect, live printing, saves to scene log."""
    for i, char in enumerate(message):
        if i == len(message) - 1:
            print(char)
        else:
            print(char, end='', flush=True)
            time.sleep(delay)
    state.current_scene_log.append(message)

def pause_menu(state):
    clear_screen()
    print("PAUSE MENU")
    print("1) LOAD\n2) SAVE\n3) INVENTORY\n4) POKEDEX\n5) MAP\n6) RETURN")
    choice = ginput(state, "Choose an option: ", "1","2","3","4","5","6")
    if choice == "6":
        restore_scene(state)
    elif choice == "5":
        show_map(state)
    elif choice == "4":
        open_pokedex(state)
    elif choice == "3":
        open_inv(state)
    else:
        log_print(state, f"Option {choice} selected. (Feature not implemented yet)")
        time.sleep(1)
        restore_scene(state)

def show_map(state):
    new_scene(state)
    log_print(state, "MAP")
    for loc, discovered in state.discovered_locations.items():
        if discovered:
            log_print(state, f"- {loc}")
        else:
            log_print(state, "- ???") 
    log_print(state, "\nPress any key to return")
    input()
    restore_scene(state)

def pinput(prompt, *val_opts):
    """Input without pause menu option"""
    while True:
        user_input = input(prompt).strip()
        
        if user_input in val_opts:
            return user_input
        
        try:
            int_val = int(user_input)
            if int_val in val_opts:
                return int_val
        except ValueError:
            pass

        try:
            float_val = float(user_input)
            if float_val in val_opts:
                return float_val
        except ValueError:
            pass

        print(f"Invalid input: '{user_input}'. Please choose from {val_opts}.")

def ginput(state, prompt, *val_opts):
    """Input with pause menu option"""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "p":
            pause_menu(state)
            continue
        
        if user_input in val_opts:
            return user_input
        
        try:
            int_val = int(user_input)
            if int_val in val_opts:
                return int_val
        except ValueError:
            pass

        try:
            float_val = float(user_input)
            if float_val in val_opts:
                return float_val
        except ValueError:
            pass

        print(f"Invalid input: '{user_input}'. Please choose from {val_opts} or type 'p' for pause menu.")

def open_inv(state):
    new_scene(state)
    if not state.player_inv:
        log_print(state, "Your inventory is empty!")
    else:
        log_print(state, "=== INVENTORY ===")
        for idx, item in enumerate(state.player_inv, 1):
            log_print(state, f"{idx}) {item}")
        
        choice = ginput(state, "\n1) Use Item\n2) Return\nChoice: ", "1", "2")
        if choice == "1":
            item_choice = ginput(state, "Which item? ", *[str(i) for i in range(1, len(state.player_inv)+1)])
            use_item(state, state.player_inv[int(item_choice)-1])
    
    log_print(state, "\nPress any key to return")
    input()
    restore_scene(state)

def use_item(state, item_name):
    if item_name not in items:
        log_print(state, "Invalid item!")
        return
    
    item_data = items[item_name]
    
    if item_data["target"] == "curr_pokemon":
        log_print(state, "\nChoose a Pokemon:")
        for slot, poke in state.player_pokemon.items():
            log_print(state, f"{slot}) {poke['nickname']} - HP: {poke['hp']}/{poke['max_hp']}")
        
        poke_choice = ginput(state, "Choose: ", *[str(s) for s in state.player_pokemon.keys()])
        selected_poke = state.player_pokemon[int(poke_choice)]
        
        if item_data["stat"] == "health":
            old_hp = selected_poke["hp"]
            selected_poke["hp"] = min(selected_poke["max_hp"], selected_poke["hp"] + item_data["value"])
            healed = selected_poke["hp"] - old_hp
            log_print(state, f"{selected_poke['nickname']} was healed for {healed} HP!")
            state.player_inv.remove(item_name)
        
        elif item_data["stat"] == "atk":
            selected_poke["atk"] += item_data["value"]
            log_print(state, f"{selected_poke['nickname']}'s Attack increased by {item_data['value']}!")
            state.player_inv.remove(item_name)
        
        elif item_data["stat"] == "defense":
            selected_poke["defense"] += item_data["value"]
            log_print(state, f"{selected_poke['nickname']}'s Defense increased by {item_data['value']}!")
            state.player_inv.remove(item_name)
        
        elif item_data["stat"] == "speed":
            selected_poke["speed"] += item_data["value"]
            log_print(state, f"{selected_poke['nickname']}'s Speed increased by {item_data['value']}!")
            state.player_inv.remove(item_name)

def open_pokedex(state):
    new_scene(state)
    count = 0
    for i in original_pokemon_data:
        count += 1
        print(f"{count}) {i}")
    choice_temp = pinput("\nActions:\n1) Sort\n2) Return\nChoice: ", "1", "2")
    if choice_temp == "1":
        choice_temp = ginput(state, "Options:\n1) Owned\n2) Not Owned\n3) Return\nChoice: ", "1","2","3")
        if choice_temp == "1":
            for slot, poke in state.player_pokemon.items():
                print(f"{poke['nickname']} ({poke['species_name']}) - Lv {poke['level']}")
        elif choice_temp == "2":
            owned = [p["species_name"] for p in state.player_pokemon.values()]
            for species in original_pokemon_data:
                if species not in owned:
                    print(f"??? - {species}")
    
    log_print(state, "\nPress any key to return")
    input()
    restore_scene(state)

# BATTLE SYSTEM
def get_active_pokemon(player_party):
    for slot, p in player_party.items():
        if p["hp"] > 0:
            return slot, p
    return None, None

def is_party_alive(player_party):
    for p in player_party.values():
        if p["hp"] > 0:
            return True
    return False

def deal_damage(state, attacker, defender, move_name):
    move = moves_data[move_name]
    power = move["power"]
    dmg = max(1, (attacker["atk"] + power) - defender["defense"])
    defender["hp"] -= dmg
    if defender["hp"] < 0:
        defender["hp"] = 0
    log_print(state, f"{attacker['nickname']} used {move_name}! It dealt {dmg} damage!")

def player_turn(state, active_player, active_opponent, is_wild=False):
    log_print(state, "\nYour turn!")
    log_print(state, "1) Attack")
    log_print(state, "2) Use Item")
    if is_wild:
        log_print(state, "3) Try to Catch")
        log_print(state, "4) Run")
        choice = ginput(state, "Choose action: ", "1", "2", "3", "4")
    else:
        log_print(state, "3) Run")
        choice = ginput(state, "Choose action: ", "1", "2", "3")
    
    if choice == "1":
        log_print(state, "\nChoose a move:")
        for i, mv in enumerate(active_player["moves"], start=1):
            log_print(state, f"{i}) {mv}")
        
        move_choice = ginput(state, "Move: ", *[str(i) for i in range(1, len(active_player["moves"])+1)])
        chosen_move = active_player["moves"][int(move_choice)-1]
        deal_damage(state, active_player, active_opponent, chosen_move)
        return "attack"
    
    elif choice == "2":
        if not state.player_inv:
            log_print(state, "No items to use!")
            return player_turn(state, active_player, active_opponent, is_wild)
        
        log_print(state, "\nItems:")
        for idx, item in enumerate(state.player_inv, 1):
            log_print(state, f"{idx}) {item}")
        
        item_choice = ginput(state, "Which item? ", *[str(i) for i in range(1, len(state.player_inv)+1)])
        use_item(state, state.player_inv[int(item_choice)-1])
        return "item"
    
    elif choice == "3" and is_wild:
        if "Pokeball" not in state.player_inv:
            log_print(state, "You don't have any Pokeballs!")
            return player_turn(state, active_player, active_opponent, is_wild)
        
        catch_rate = 0.3 + (1 - active_opponent["hp"] / active_opponent["max_hp"]) * 0.5
        if random.random() < catch_rate:
            log_print(state, f"You caught {active_opponent['nickname']}!")
            
            new_slot = max(state.player_pokemon.keys()) + 1
            active_opponent['exp'] = 0
            active_opponent['exp_to_next'] = 100
            active_opponent['gender'] = random.choice(["male", "female"])
            active_opponent['pokedex_inv_id'] = new_slot
            state.player_pokemon[new_slot] = active_opponent.copy()
            state.player_inv.remove("Pokeball")
            return "caught"
        else:
            log_print(state, f"{active_opponent['nickname']} broke free!")
            state.player_inv.remove("Pokeball")
            return "failed_catch"
    
    elif (choice == "4" and is_wild) or (choice == "3" and not is_wild):
        if random.random() < 0.5:
            log_print(state, "You ran away!")
            return "ran"
        else:
            log_print(state, "Couldn't escape!")
            return "failed_run"

def pok_turn(state, active_player, active_opponent):
    move = random.choice(active_opponent["moves"])
    log_print(state, "\nEnemy turn!")
    deal_damage(state, active_opponent, active_player, move)

def gain_exp(state, pokemon, amount):
    pokemon["exp"] += amount
    log_print(state, f"{pokemon['nickname']} gained {amount} EXP!")
    
    while pokemon["exp"] >= pokemon["exp_to_next"]:
        pokemon["exp"] -= pokemon["exp_to_next"]
        pokemon["level"] += 1
        
        pokemon["max_hp"] += 3
        pokemon["hp"] += 3
        pokemon["atk"] += 1
        pokemon["defense"] += 1
        pokemon["speed"] += 1
        
        log_print(state, f"\n*** {pokemon['nickname']} leveled up to Level {pokemon['level']}! ***")
        log_print(state, f"HP +3, ATK +1, DEF +1, SPD +1")
        
        pokemon["exp_to_next"] = int(pokemon["exp_to_next"] * 1.2)

def battle(state, player_party, enemy_data, enemy_type="wild"):
    enemy = enemy_data.copy()
    enemy["nickname"] = enemy.get("name", enemy["species_name"])
    enemy["max_hp"] = enemy["hp"]

    if "moves" not in enemy:
        enemy["moves"] = ["Tackle"]

    log_print(state, f"A {enemy['nickname']} appeared!\n")

    while True:
        slot, active_player = get_active_pokemon(player_party)
        if active_player is None:
            log_print(state, "All your Pokémon fainted!")
            return "lose"

        if enemy["hp"] <= 0:
            log_print(state, f"You defeated {enemy['nickname']}!")
            exp_gain = enemy.get("level", 5) * 20
            gain_exp(state, active_player, exp_gain)
            return "win"

        is_wild = (enemy_type == "wild")
        action = player_turn(state, active_player, enemy, is_wild)

        if action == "ran":
            return "ran"
        if action == "caught":
            return "caught"

        if enemy["hp"] <= 0:
            log_print(state, f"You defeated {enemy['nickname']}!")
            exp_gain = enemy.get("level", 5) * 20
            gain_exp(state, active_player, exp_gain)
            return "win"

        if action in ["attack", "failed_catch", "failed_run"]:
            pok_turn(state, active_player, enemy)

        if active_player["hp"] <= 0:
            log_print(state, f"{active_player['nickname']} fainted!\n")
            if not is_party_alive(player_party):
                log_print(state, "All your Pokémon fainted!")
                return "lose"

def mew_battle(state):
    text(state, "You Found Mewtwo!")
    time.sleep(1)
    new_scene(state)
    text(state, "Mewtwo stares at you with intense psychic power...")
    text(state, "This is the ultimate challenge!")
    time.sleep(2)
    
    mewtwo_data = {
        "species_name": "Mewtwo",
        "name": "Mewtwo",
        "level": 70,
        "type": ["psychic"],
        "hp": 200,
        "max_hp": 200,
        "atk": 30,
        "defense": 20,
        "speed": 25,
        "moves": ["Psychic", "Swift", "Recover"]
    }
    
    result = battle(state, state.player_pokemon, mewtwo_data, "legendary")
    
    if result == "win":
        new_scene(state)
        text(state, "=" * 50)
        text(state, "CONGRATULATIONS!")
        text(state, "You have defeated Mewtwo and become the ultimate Pokemon Master!")
        text(state, "=" * 50)
        time.sleep(3)
        return True
    else:
        text(state, "Mewtwo was too powerful... Try training more!")
        return False

def explore_special_area(state, area_name):
    """Explore a special area, with chances to find Pokemon and items"""
    if area_name not in special_areas:
        log_print(state, "This area doesn't exist!")
        return
    
    area = special_areas[area_name]
    new_scene(state)
    log_print(state, f"=== {area_name} ===")
    log_print(state, "You explore the area...")
    time.sleep(1)
    
    if area.get("special") == "mewtwo_location" and len(state.gym_badges) >= 8:
        encounter = ginput(state, "\nYou sense an incredibly powerful presence deeper in the cave...\nInvestigate? (y/n): ", "y", "n")
        if encounter == "y":
            if mew_battle(state):
                return
    
    if random.random() < 0.6:
        log_print(state, "\nA wild Pokemon appeared!")
        species = random.choice(area["pokemon_pool"])
        level = random.randint(*area["pokemon_lvl_range"])
        
        wild_pokemon = {
            "species_name": species,
            "name": species,
            "level": level,
            "type": original_pokemon_data[species]["type"],
            "hp": original_pokemon_data[species]["base_hp"] + (level * 2),
            "max_hp": original_pokemon_data[species]["base_hp"] + (level * 2),
            "atk": original_pokemon_data[species]["base_atk"] + level,
            "defense": original_pokemon_data[species]["base_defense"] + (level // 2),
            "speed": original_pokemon_data[species]["base_speed"] + level,
            "moves": original_pokemon_data[species]["possible_moves"][:2]
        }
        
        result = battle(state, state.player_pokemon, wild_pokemon, "wild")
        
        if result == "lose":
            heal_all_pokemon(state)
            log_print(state, "\nYou rushed to the Pokemon Center!")
    
    if random.random() < 0.4:
        item_key = f"{area_name}_item_{random.randint(1,100)}"
        if item_key not in state.collected_items:
            found_item = random.choice(area["items"])
            log_print(state, f"\nYou found a {found_item}!")
            state.player_inv.append(found_item)
            state.collected_items[item_key] = True
    
    log_print(state, "\nPress any key to leave")
    input()

def heal_all_pokemon(state):
    """Heal all Pokemon to full HP"""
    for poke in state.player_pokemon.values():
        poke["hp"] = poke["max_hp"]

def healing_center(state):
    new_scene(state)
    log_print(state, "=== POKEMON CENTER ===")
    log_print(state, "Welcome! Let me heal your Pokemon!")
    time.sleep(1)
    log_print(state, "Healing...")
    time.sleep(1)
    heal_all_pokemon(state)
    log_print(state, "Your Pokemon are fully healed!")
    time.sleep(1)

def shop(state, shop_types):
    """Shop to buy items"""
    new_scene(state)
    log_print(state, "=== SHOP ===")
    log_print(state, f"Money: ${state.player_money}")
    log_print(state, "\nItems for sale:")
    
    available_items = []
    if "General Store" in shop_types:
        available_items.extend(["Health Potion", "Super Potion", "Pokeball"])
    if "Evolution Stones" in shop_types:
        available_items.append("Fire Stone")
    if any(shop in shop_types for shop in ["Psychic Shop", "Rock Shop", "Water Shop"]):
        available_items.extend(["Protein", "Iron", "Carbos"])
    
    for idx, item_name in enumerate(available_items, 1):
        price = items[item_name]["sale_price"]
        log_print(state, f"{idx}) {item_name} - ${price}")
    
    log_print(state, f"{len(available_items)+1}) Leave")
    
    choice = ginput(state, "\nWhat would you like to buy? ", *[str(i) for i in range(1, len(available_items)+2)])
    
    if int(choice) <= len(available_items):
        item_name = available_items[int(choice)-1]
        price = items[item_name]["sale_price"]
        
        if state.player_money >= price:
            state.player_money -= price
            state.player_inv.append(item_name)
            log_print(state, f"\nYou bought {item_name}!")
            time.sleep(1)
        else:
            log_print(state, "\nNot enough money!")
            time.sleep(1)

def gym_battle(state, gym_leader):
    """Battle a gym leader"""
    new_scene(state)
    log_print(state, f"=== {gym_leader['name'].upper()}'S GYM ===")
    log_print(state, f"Gym Leader {gym_leader['name']} challenges you!")
    time.sleep(2)
    
    leader_pokemon = {
        "species_name": "Leader Pokemon",
        "name": f"{gym_leader['name']}'s Pokemon",
        "level": 15 + (len(state.gym_badges) * 5),
        "type": [gym_leader["type"]],
        "hp": 60 + (len(state.gym_badges) * 10),
        "max_hp": 60 + (len(state.gym_badges) * 10),
        "atk": 12 + (len(state.gym_badges) * 2),
        "defense": 10 + (len(state.gym_badges) * 2),
        "speed": 10 + len(state.gym_badges),
        "moves": ["Tackle", "Quick Attack"]
    }
    
    result = battle(state, state.player_pokemon, leader_pokemon, "trainer")
    
    if result == "win":
        state.gym_badges.append(gym_leader["badge"])
        log_print(state, f"\nCongratulations! You earned the {gym_leader['badge']}!")
        state.player_inv.append("Super Potion")
        log_print(state, "You also received a Super Potion!")
        time.sleep(2)
    else:
        log_print(state, f"\n{gym_leader['name']} was too strong! Train more and come back!")
        time.sleep(2)

def view_party(state):
    """View your Pokemon party"""
    new_scene(state)
    log_print(state, "=== YOUR PARTY ===")
    for slot, poke in state.player_pokemon.items():
        log_print(state, f"\n{slot}) {poke['nickname']} ({poke['species_name']})")
        log_print(state, f"   Level: {poke['level']}")
        log_print(state, f"   HP: {poke['hp']}/{poke['max_hp']}")
        log_print(state, f"   ATK: {poke['atk']} | DEF: {poke['defense']} | SPD: {poke['speed']}")
        
        exp = poke.get('exp', 0)
        exp_to_next = poke.get('exp_to_next', 100)
        log_print(state, f"   EXP: {exp}/{exp_to_next}")
    
    log_print(state, "\nPress any key to return")
    input()

def travel_menu(state):
    """Show available cities to travel to"""
    new_scene(state)
    log_print(state, "=== TRAVEL ===")
    log_print(state, f"Current location: {state.current_location}")
    log_print(state, "\nAvailable routes:")
    
    available_routes = []
    for route_name, route_data in routes.items():
        if state.current_location in route_data["connects"]:
            destination = [c for c in route_data["connects"] if c != state.current_location][0]
            available_routes.append((route_name, destination))
    
    for idx, (route, dest) in enumerate(available_routes, 1):
        log_print(state, f"{idx}) {route} -> {dest}")
    
    log_print(state, f"{len(available_routes)+1}) Stay here")
    
    choice = ginput(state, "\nWhere do you want to go? ", *[str(i) for i in range(1, len(available_routes)+2)])
    
    if int(choice) <= len(available_routes):
        route_name, destination = available_routes[int(choice)-1]
        travel_route(state, route_name, destination)
    else:
        restore_scene(state)

def travel_route(state, route_name, destination):
    """Travel along a route with encounters"""
    route = routes[route_name]
    new_scene(state)
    log_print(state, f"=== Traveling {route_name} ===")
    log_print(state, f"Distance: {route['distance']} km\n")
    
    state.discovered_locations[route_name] = True
    
    for i in range(route["distance"]):
        progress = int((i / route["distance"]) * 20)
        bar = "=" * progress + " " * (20 - progress)
        print(f"\r[{bar}] {i}/{route['distance']} km", end="", flush=True)
        time.sleep(0.5)
        
        if random.random() < 0.4:
            print()
            
            if random.random() < route["trainer_chance"]:
                trainer_id = f"{route_name}_trainer_{i}"
                if trainer_id not in state.defeated_trainers:
                    log_print(state, "\nA trainer spotted you!")
                    time.sleep(1)
                    
                    trainer_pokemon = {
                        "species_name": "Trainer Pokemon",
                        "name": "Trainer's Pokemon",
                        "level": 8 + len(state.gym_badges) * 3,
                        "type": ["normal"],
                        "hp": 40 + len(state.gym_badges) * 5,
                        "max_hp": 40 + len(state.gym_badges) * 5,
                        "atk": 10 + len(state.gym_badges),
                        "defense": 8 + len(state.gym_badges),
                        "speed": 8 + len(state.gym_badges),
                        "moves": ["Tackle", "Quick Attack"]
                    }
                    
                    result = battle(state, state.player_pokemon, trainer_pokemon, "trainer")
                    
                    if result == "win":
                        state.defeated_trainers.append(trainer_id)
                        prize_money = 100 + (len(state.gym_badges) * 50)
                        state.player_money += prize_money
                        log_print(state, f"\nYou won ${prize_money}!")
                        time.sleep(1)
                    elif result == "lose":
                        log_print(state, "\nYou blacked out and returned to the Pokemon Center!")
                        heal_all_pokemon(state)
                        time.sleep(2)
                        return "blackout"
                    
                    progress = int((i / route["distance"]) * 20)
                    bar = "=" * progress + " " * (20 - progress)
                    print(f"\r[{bar}] {i}/{route['distance']} km", end="", flush=True)
            
            else:
                log_print(state, "\nA wild Pokemon appeared!")
                species = random.choice(route["pokemon_pool"])
                level = random.randint(5 + len(state.gym_badges) * 2, 8 + len(state.gym_badges) * 2)
                
                wild_pokemon = {
                    "species_name": species,
                    "name": species,
                    "level": level,
                    "type": original_pokemon_data[species]["type"],
                    "hp": original_pokemon_data[species]["base_hp"] + (level * 2),
                    "max_hp": original_pokemon_data[species]["base_hp"] + (level * 2),
                    "atk": original_pokemon_data[species]["base_atk"] + level,
                    "defense": original_pokemon_data[species]["base_defense"] + (level // 2),
                    "speed": original_pokemon_data[species]["base_speed"] + level,
                    "moves": original_pokemon_data[species]["possible_moves"][:2]
                }
                
                result = battle(state, state.player_pokemon, wild_pokemon, "wild")
                
                if result == "lose":
                    log_print(state, "\nYou blacked out and returned to the Pokemon Center!")
                    heal_all_pokemon(state)
                    time.sleep(2)
                    return "blackout"
                
                progress = int((i / route["distance"]) * 20)
                bar = "=" * progress + " " * (20 - progress)
                print(f"\r[{bar}] {i}/{route['distance']} km", end="", flush=True)
    
    progress = 20
    bar = "=" * progress
    print(f"\r[{bar}] {route['distance']}/{route['distance']} km")
    
    log_print(state, f"\nArrived at {destination}!")
    time.sleep(1)
    state.current_location = destination
    state.discovered_locations[destination] = True
def enter_city(state, city_name):
    """Enter a city and choose where to go"""
    state.discovered_locations[city_name] = True
    state.current_location = city_name
    
    while True:
        new_scene(state)
        city = cities[city_name]
        log_print(state, f"=== {city_name.upper()} ===")
        log_print(state, city["description"])
        log_print(state, "\nWhere would you like to go?")
        
        options = []
        option_num = 1
        
        if city["healing_center"]:
            log_print(state, f"{option_num}) Pokemon Center")
            options.append("center")
            option_num += 1
        
        if city["shops"]:
            log_print(state, f"{option_num}) Shop")
            options.append("shop")
            option_num += 1
        
        if city["gym"]:
            badge_name = city["gym_leader"]["badge"]
            if badge_name in state.gym_badges:
                log_print(state, f"{option_num}) Gym (Already beaten)")
            else:
                log_print(state, f"{option_num}) Gym")
            options.append("gym")
            option_num += 1
        
        if city["special_area"]:
            log_print(state, f"{option_num}) {city['special_area']}")
            options.append("special")
            option_num += 1
        
        log_print(state, f"{option_num}) Travel to another city")
        options.append("travel")
        option_num += 1
        
        log_print(state, f"{option_num}) View Party")
        options.append("party")
        
        choice = ginput(state, "\nChoice: ", *[str(i) for i in range(1, option_num+1)])
        selected = options[int(choice)-1]
        
        if selected == "center":
            healing_center(state)
        elif selected == "shop":
            shop(state, city["shops"])
        elif selected == "gym":
            if city["gym_leader"]["badge"] not in state.gym_badges:
                gym_battle(state, city["gym_leader"])
        elif selected == "special":
            explore_special_area(state, city["special_area"])
        elif selected == "travel":
            travel_menu(state)
            break
        elif selected == "party":
            view_party(state)

def main():
    """Main game function"""
    state = GameState()
    
    # Ask player name
    while True:
        name = input("What is your name: ").strip()
        if name:
            confirm = ginput(state, f"Are you sure you want to be called '{name}'? (y/n): ", "y", "n")
            if confirm == "y":
                break
    new_scene(state)

    # Main menu
    new_scene(state)
    log_print(state, "Pokemon")
    log_print(state, "1) Load Save Data")
    log_print(state, "2) Start New Game")

    choice = ginput(state, "Choose an option: ", "1", "2")

    if choice == "1":
        log_print(state, "Loading game...")
        try:
            open("pokemon_game/saves.txt")
            print("found")
        except FileNotFoundError:
            print("not found")
    else:
        for _ in range(2):
            new_scene(state)
            for dots in ["", ".", "..", "..."]:
                print(f"Starting new game{dots}")
                time.sleep(0.4)
                new_scene(state)
        print(title_ascii)
        time.sleep(2)

    input("\n\n\nPress ENTER to continue...")
    new_scene(state)

    # Opening story sequence
    text(state, "=" * 60)
    text(state, "WELCOME TO THE WORLD OF POKÉMON!")
    text(state, "=" * 60)
    time.sleep(2)
    new_scene(state)

    text(state, f"Greetings, {name}. I am Professor Oak, the leading Pokémon")
    text(state, "researcher in the Kanto region.")
    time.sleep(2)
    new_scene(state)

    text(state, "For years, I have studied the incredible creatures known as")
    text(state, "Pokémon - beings with mysterious powers that live alongside")
    text(state, "humans in harmony.")
    time.sleep(3)
    new_scene(state)

    text(state, "But recently, something has disturbed the balance of our world...")
    time.sleep(2)
    new_scene(state)

    text(state, "Deep within Cerulean Cave, an ancient and powerful Pokémon has")
    text(state, "awakened. Its name is MEWTWO - a legendary psychic-type Pokémon")
    text(state, "of unmatched intelligence and strength.")
    time.sleep(3)
    new_scene(state)

    text(state, "Mewtwo was created through genetic experiments, and its power")
    text(state, "has grown beyond anything we've ever encountered. It's said that")
    text(state, "only a true Pokémon Master can face such a legendary being.")
    time.sleep(3)
    new_scene(state)

    text(state, "Your mission, should you choose to accept it, is to become that")
    text(state, "Master. Travel across the Kanto region, collect the 8 Gym Badges")
    text(state, "by defeating each Gym Leader, and grow strong enough to challenge")
    text(state, "Mewtwo in Cerulean Cave.")
    time.sleep(3)
    new_scene(state)

    text(state, "The path ahead won't be easy:")
    text(state, "  • Battle wild Pokémon and trainers to gain experience")
    text(state, "  • Capture new Pokémon to build your team")
    text(state, "  • Challenge Gym Leaders to earn their badges")
    text(state, "  • Explore special areas to find rare Pokémon and items")
    text(state, "  • Once you have all 8 badges, venture into Cerulean Cave")
    time.sleep(4)
    new_scene(state)

    text(state, "Remember: Mewtwo will only reveal itself to those who have")
    text(state, "proven their worth by collecting all 8 Gym Badges.")
    time.sleep(2)
    new_scene(state)

    text(state, "But first, every trainer needs their first Pokémon partner.")
    text(state, "Choose wisely, as this Pokémon will be with you from the")
    text(state, "very beginning of your journey!")
    time.sleep(3)

    # Show starter Pokémon
    new_scene(state)
    text(state, f"So, {name}, which Pokémon will you choose?\n")
    time.sleep(1)

    for i, species in enumerate(starter_pokemon, start=1):
        data = original_pokemon_data[species]
        log_print(state, f"{i}) {species}")
        log_print(state, f"   Type: {', '.join(data['type'])}")
        log_print(state, f"   HP: {data['base_hp']}  ATK: {data['base_atk']}  DEF: {data['base_defense']}  SPD: {data['base_speed']}")
        log_print(state, "")

    choice = ginput(state, "Choose your starter: ", "1", "2", "3")
    starter_species = starter_pokemon[int(choice)-1]

    state.player_pokemon = {
        1: {
            "nickname": starter_species,
            "species_name": starter_species,
            "level": 5,
            "type": original_pokemon_data[starter_species]["type"],
            "hp": original_pokemon_data[starter_species]["base_hp"],
            "max_hp": original_pokemon_data[starter_species]["base_hp"],
            "atk": original_pokemon_data[starter_species]["base_atk"],
            "defense": original_pokemon_data[starter_species]["base_defense"],
            "speed": original_pokemon_data[starter_species]["base_speed"],
            "exp": 0,
            "exp_to_next": 100,
            "moves": original_pokemon_data[starter_species]["possible_moves"][:2],
            "gender": "male",
            "pokedex_inv_id": 1
        }
    }

    new_scene(state)
    text(state, f"Excellent choice, {name}! {starter_species} is a powerful ally.")
    text(state, f"{starter_species} looks at you with determination in its eyes.")
    time.sleep(2)

    new_scene(state)
    text(state, "Now, let me give you some important advice for your journey:")
    time.sleep(1)
    new_scene(state)

    text(state, "TIP #1: THE PAUSE MENU")
    text(state, "At any point during your adventure, when you see an input prompt,")
    text(state, "you can type 'P' to open the pause menu. There you can:")
    text(state, "  • Save your progress")
    text(state, "  • Check your Pokédex")
    text(state, "  • View your inventory")
    text(state, "  • See the map of discovered locations")
    time.sleep(4)
    new_scene(state)

    text(state, "TIP #2: YOUR JOURNEY PATH")
    text(state, "Here's the recommended route to collect all 8 Gym Badges:")
    text(state, "  1. Pallet Town (START) → Route 1 → Viridian City")
    text(state, "  2. Route 2 → Pewter City (Badge #1: Brock)")
    text(state, "  3. Route 3 → Cerulean City (Badge #2: Misty)")
    text(state, "  4. Route 4 → Vermilion City (Badge #3: Lt. Surge)")
    text(state, "  5. Route 5 → Lavender Town → Route 6 → Celadon City (Badge #4)")
    text(state, "  6. Route 7 → Fuchsia City (Badge #5)")
    text(state, "  7. Route 8 → Saffron City (Badge #6)")
    text(state, "  8. Route 9 → Cinnabar Island (Badge #7)")
    text(state, "  9. Return to Viridian City (Badge #8: Giovanni)")
    text(state, "  10. Finally, enter Cerulean Cave to face MEWTWO!")
    time.sleep(6)
    new_scene(state)

    text(state, "TIP #3: TRAINING AND PREPARATION")
    text(state, "Don't rush! Take time to:")
    text(state, "  • Battle wild Pokémon to level up your team")
    text(state, "  • Explore special areas for rare Pokémon and items")
    text(state, "  • Visit Pokémon Centers to heal (they're free!)")
    text(state, "  • Buy potions and Pokéballs at shops")
    text(state, "  • Catch diverse Pokémon types to counter Gym Leaders")
    time.sleep(5)
    new_scene(state)

    text(state, "TIP #4: MEWTWO")
    text(state, "Remember, Mewtwo is incredibly powerful. You'll need:")
    text(state, "  • All 8 Gym Badges to access Cerulean Cave")
    text(state, "  • A well-trained team of high-level Pokémon")
    text(state, "  • Plenty of healing items")
    text(state, "  • Strategy and determination!")
    time.sleep(4)
    new_scene(state)

    text(state, "Alright, that's enough talk! Let's test your skills with your")
    text(state, "first battle. A wild Rattata has appeared!")
    time.sleep(2)

    new_scene(state)
    enemy_pokemon = {
        "species_name": "Rattata",
        "name": "Wild Rattata",
        "level": 3,
        "hp": 15,
        "max_hp": 15,
        "atk": 5,
        "defense": 3,
        "speed": 6,
        "moves": ["Tackle"]
    }
    result = battle(state, state.player_pokemon, enemy_pokemon, "wild")

    if result == "win":
        new_scene(state)
        text(state, "Congratulations on your first victory!")
        time.sleep(1)
    else:
        new_scene(state)
        text(state, "Don't worry, every trainer loses sometimes. Let me heal your")
        text(state, "Pokémon for you.")
        heal_all_pokemon(state)
        time.sleep(2)

    new_scene(state)
    text(state, "You're ready now! Your adventure begins in Pallet Town.")
    text(state, "")
    text(state, "Remember your goal:")
    text(state, "  → Collect all 8 Gym Badges")
    text(state, "  → Explore and train your Pokémon")
    text(state, "  → Face Mewtwo in Cerulean Cave")
    text(state, "")
    text(state, f"The fate of the Kanto region rests in your hands, {name}!")
    text(state, "Good luck, and may you become the ultimate Pokémon Master!")
    time.sleep(4)

    # Give starter items
    state.player_inv.extend(["Health Potion", "Health Potion", "Pokeball", "Pokeball", "Pokeball"])
    new_scene(state)
    text(state, "=" * 60)
    text(state, "STARTER PACK RECEIVED!")
    text(state, "=" * 60)
    text(state, "Professor Oak hands you a backpack with:")
    text(state, "  • 2x Health Potion (heals 20 HP)")
    text(state, "  • 3x Pokéball (for catching wild Pokémon)")
    text(state, "")
    text(state, "Use them wisely on your journey!")
    time.sleep(3)

    # Main game loop - start in Pallet Town
    enter_city(state, "Pallet Town")

if __name__ == "__main__":
    main()