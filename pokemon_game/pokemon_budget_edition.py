# DL 1st, final project 

# add sound, remove globals, fix asciis, Test
import json
import os
import time
import random
import sys
from io import StringIO

"""
file_name = 'pokemon_database_db.json'

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, file_name)

try:
    with open(file_path, 'r') as file:
        data = json.load(file)

        print("--- Data as a Python object ---")
        print(data)
        print("-" * 40)

        print("--- Formatted JSON Output ---")
        print(json.dumps(data, indent=4))
        print("-" * 40)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found at {file_path}")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from the file '{file_name}'. Check file integrity.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
"""
#script_dir = os.path.dirname(os.path.abspath(__file__))
#save_file_path = os.path.join(script_dir, 'saves.txt')
#with open(save_file_path, 'w') as file:
#        file.write("Hello")


# Variables:

captured_output = StringIO()
current_scene_log = []

# Game state tracking
defeated_trainers = []
collected_items = {}
gym_badges = []
player_money = 500

def index_of_lists(list):
    indexes = []
    for i in list:

        indexes.append(list.index(i)+1)
    return indexes

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS / Linux
        os.system('clear')

def new_scene():
    """Start a new scene: clears terminal and resets scene log."""
    global captured_output, current_scene_log
    captured_output = StringIO()
    current_scene_log = []
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS / Linux
        os.system('clear')

def restore_scene():
    """Restore the current scene to terminal."""
    clear_screen()
    for line in current_scene_log:
        print(line)

def log_print(message):
    """Print live AND save message to current scene."""
    print(message)
    current_scene_log.append(message)

def text(message, delay=0.02):
    """Typewriter effect, live printing, saves to scene log."""
    for i, char in enumerate(message):
        if i == len(message) - 1:
            print(char)
        else:
            print(char, end='', flush=True)
            time.sleep(delay)
    current_scene_log.append(message)

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


discovered_locations = {
    "Pallet Town": True,  # always starts discovered
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

current_location = "Pallet Town"

# list of all pokemon, type, names, evolution/s, pokedex number
original_pokemon_data = {
    "Charmander": {
        "species_name": "Charmander",
        "type": ["fire"],
        "base_hp": 20,
        "base_atk": 8,
        "base_defense": 5,
        "base_speed": 7,
        "evolutions": [{"to":"Charmeleon","level":16}],
        "ascii_battle": "LARGE ASCII HERE (If you are seeing this message than the ascii cannot be found, either fix the problem, or continue playing wihtout it)",
        "ascii_small": "SMALL ASCII HERE (If you are seeing this message than the ascii cannot be found, either fix the problem, or continue playing wihtout it)",
        "ascii_silhouette": "SILHOUETTE HERE (If you are seeing this message than the ascii cannot be found, either fix the problem, or continue playing wihtout it)",
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
        "ascii_battle": "LARGE ASCII HERE (If you are seeing this message than the ascii cannot be found, either fix the problem, or continue playing wihtout it)",
        "ascii_small": "SMALL ASCII HERE (If you are seeing this message than the ascii cannot be found, either fix the problem, or continue playing wihtout it)",
        "ascii_silhouette": "SILHOUETTE HERE (If you are seeing this message than the ascii cannot be found, either fix the problem, or continue playing wihtout it)",
        "pokedex_id": "2", #placeholders, not real ids
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
    "Spearow": {
        "species_name": "Spearow",
        "type": ["flying"],
        "base_hp": 17,
        "base_atk": 8,
        "base_defense": 4,
        "base_speed": 9,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "5",
        "possible_moves": ["Peck","Fury Attack"]
    },
    "Fearow": {
        "species_name": "Fearow",
        "type": ["flying"],
        "base_hp": 25,
        "base_atk": 12,
        "base_defense": 8,
        "base_speed": 13,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "6",
        "possible_moves": ["Drill Peck","Agility"]
    },
    "Pidgeotto": {
        "species_name": "Pidgeotto",
        "type": ["flying"],
        "base_hp": 24,
        "base_atk": 10,
        "base_defense": 7,
        "base_speed": 11,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "7",
        "possible_moves": ["Wing Attack","Quick Attack"]
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
        "pokedex_id": "8",
        "possible_moves": ["Tackle","Quick Attack"]
    },
    "Raticate": {
        "species_name": "Raticate",
        "type": ["normal"],
        "base_hp": 23,
        "base_atk": 11,
        "base_defense": 8,
        "base_speed": 12,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "9",
        "possible_moves": ["Hyper Fang","Super Fang"]
    },
    "Jigglypuff": {
        "species_name": "Jigglypuff",
        "type": ["normal"],
        "base_hp": 30,
        "base_atk": 5,
        "base_defense": 3,
        "base_speed": 3,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "10",
        "possible_moves": ["Pound","Sing"]
    },
    "Meowth": {
        "species_name": "Meowth",
        "type": ["normal"],
        "base_hp": 18,
        "base_atk": 6,
        "base_defense": 5,
        "base_speed": 11,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "11",
        "possible_moves": ["Scratch","Bite"]
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
        "pokedex_id": "12",
        "possible_moves": ["Tackle","String Shot"]
    },
    "Weedle": {
        "species_name": "Weedle",
        "type": ["bug"],
        "base_hp": 18,
        "base_atk": 5,
        "base_defense": 4,
        "base_speed": 7,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "13",
        "possible_moves": ["Poison Sting","String Shot"]
    },
    "Beedrill": {
        "species_name": "Beedrill",
        "type": ["bug"],
        "base_hp": 24,
        "base_atk": 12,
        "base_defense": 6,
        "base_speed": 10,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "14",
        "possible_moves": ["Twineedle","Pin Missile"]
    },
    "Butterfree": {
        "species_name": "Butterfree",
        "type": ["bug"],
        "base_hp": 22,
        "base_atk": 6,
        "base_defense": 7,
        "base_speed": 9,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "15",
        "possible_moves": ["Confusion","Gust"]
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
        "pokedex_id": "16",
        "possible_moves": ["Tackle","Rock Throw"]
    },
    "Graveler": {
        "species_name": "Graveler",
        "type": ["rock"],
        "base_hp": 26,
        "base_atk": 13,
        "base_defense": 12,
        "base_speed": 5,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "17",
        "possible_moves": ["Rock Slide","Earthquake"]
    },
    "Onix": {
        "species_name": "Onix",
        "type": ["rock"],
        "base_hp": 18,
        "base_atk": 6,
        "base_defense": 16,
        "base_speed": 9,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "18",
        "possible_moves": ["Rock Throw","Bind"]
    },
    "Rhyhorn": {
        "species_name": "Rhyhorn",
        "type": ["rock"],
        "base_hp": 28,
        "base_atk": 11,
        "base_defense": 12,
        "base_speed": 3,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "19",
        "possible_moves": ["Horn Attack","Stomp"]
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
        "pokedex_id": "20",
        "possible_moves": ["Splash","Tackle"]
    },
    "Psyduck": {
        "species_name": "Psyduck",
        "type": ["water"],
        "base_hp": 22,
        "base_atk": 8,
        "base_defense": 6,
        "base_speed": 7,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "21",
        "possible_moves": ["Water Gun","Confusion"]
    },
    "Tentacool": {
        "species_name": "Tentacool",
        "type": ["water"],
        "base_hp": 18,
        "base_atk": 6,
        "base_defense": 5,
        "base_speed": 9,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "22",
        "possible_moves": ["Poison Sting","Bubble Beam"]
    },
    "Goldeen": {
        "species_name": "Goldeen",
        "type": ["water"],
        "base_hp": 19,
        "base_atk": 8,
        "base_defense": 7,
        "base_speed": 8,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "23",
        "possible_moves": ["Peck","Water Pulse"]
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
        "pokedex_id": "24",
        "possible_moves": ["Thunder Shock","Quick Attack"]
    },
    "Voltorb": {
        "species_name": "Voltorb",
        "type": ["electric"],
        "base_hp": 18,
        "base_atk": 5,
        "base_defense": 7,
        "base_speed": 13,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "25",
        "possible_moves": ["Spark","Sonic Boom"]
    },
    "Magnemite": {
        "species_name": "Magnemite",
        "type": ["electric"],
        "base_hp": 16,
        "base_atk": 6,
        "base_defense": 10,
        "base_speed": 6,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "26",
        "possible_moves": ["Thunder Shock","Tackle"]
    },
    "Electabuzz": {
        "species_name": "Electabuzz",
        "type": ["electric"],
        "base_hp": 24,
        "base_atk": 11,
        "base_defense": 8,
        "base_speed": 14,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "27",
        "possible_moves": ["Thunder Punch","Thunder"]
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
        "pokedex_id": "28",
        "possible_moves": ["Lick","Night Shade"]
    },
    "Haunter": {
        "species_name": "Haunter",
        "type": ["ghost"],
        "base_hp": 20,
        "base_atk": 12,
        "base_defense": 6,
        "base_speed": 13,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "29",
        "possible_moves": ["Shadow Punch","Hypnosis"]
    },
    "Gengar": {
        "species_name": "Gengar",
        "type": ["ghost"],
        "base_hp": 22,
        "base_atk": 14,
        "base_defense": 8,
        "base_speed": 15,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "30",
        "possible_moves": ["Shadow Ball","Dream Eater"]
    },
    "Cubone": {
        "species_name": "Cubone",
        "type": ["ghost"],
        "base_hp": 22,
        "base_atk": 8,
        "base_defense": 12,
        "base_speed": 5,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "31",
        "possible_moves": ["Bone Club","Headbutt"]
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
        "pokedex_id": "32",
        "possible_moves": ["Absorb","Acid"]
    },
    "Bellsprout": {
        "species_name": "Bellsprout",
        "type": ["grass"],
        "base_hp": 22,
        "base_atk": 10,
        "base_defense": 5,
        "base_speed": 6,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "33",
        "possible_moves": ["Vine Whip","Wrap"]
    },
    "Tangela": {
        "species_name": "Tangela",
        "type": ["grass"],
        "base_hp": 24,
        "base_atk": 8,
        "base_defense": 12,
        "base_speed": 8,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "34",
        "possible_moves": ["Constrict","Vine Whip"]
    },
    "Exeggcute": {
        "species_name": "Exeggcute",
        "type": ["grass"],
        "base_hp": 22,
        "base_atk": 6,
        "base_defense": 10,
        "base_speed": 6,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "35",
        "possible_moves": ["Barrage","Leech Seed"]
    },
    "Vulpix": {
        "species_name": "Vulpix",
        "type": ["fire"],
        "base_hp": 18,
        "base_atk": 6,
        "base_defense": 6,
        "base_speed": 8,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "36",
        "possible_moves": ["Ember","Quick Attack"]
    },
    "Growlithe": {
        "species_name": "Growlithe",
        "type": ["fire"],
        "base_hp": 23,
        "base_atk": 9,
        "base_defense": 6,
        "base_speed": 8,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "37",
        "possible_moves": ["Ember","Bite"]
    },
    "Ponyta": {
        "species_name": "Ponyta",
        "type": ["fire"],
        "base_hp": 22,
        "base_atk": 11,
        "base_defense": 7,
        "base_speed": 12,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "38",
        "possible_moves": ["Flame Charge","Stomp"]
    },
    "Magmar": {
        "species_name": "Magmar",
        "type": ["fire"],
        "base_hp": 24,
        "base_atk": 13,
        "base_defense": 8,
        "base_speed": 13,
        "evolutions": [],
        "ascii_battle": "LARGE ASCII HERE",
        "ascii_small": "SMALL ASCII HERE",
        "ascii_silhouette": "SILHOUETTE HERE",
        "pokedex_id": "39",
        "possible_moves": ["Fire Punch","Flamethrower"]
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
        "pokedex_id": "40",
        "possible_moves": ["Psychic","Swift","Recover"]
    }
}

moves_data = {
    "Scratch": {"power": 5},
    "Ember": {"power": 7},
    "Flamethrower": {"power": 10},
    "Fire Punch": {"power": 9},
    "Flame Charge": {"power": 7},
    "Tackle": {"power": 5},
    "Vine Whip": {"power": 7},
    "Growl": {"power": 0},
    "Water Gun": {"power": 7},
    "Bubble": {"power": 6},
    "Water Pulse": {"power": 8},
    "Bubble Beam": {"power": 8},
    "Peck": {"power": 6},
    "Gust": {"power": 7},
    "Quick Attack": {"power": 6},
    "String Shot": {"power": 0},
    "Rock Throw": {"power": 8},
    "Rock Slide": {"power": 10},
    "Earthquake": {"power": 12},
    "Splash": {"power": 0},
    "Thunder Shock": {"power": 7},
    "Spark": {"power": 7},
    "Thunder Punch": {"power": 9},
    "Thunder": {"power": 12},
    "Lick": {"power": 6},
    "Night Shade": {"power": 8},
    "Shadow Punch": {"power": 9},
    "Shadow Ball": {"power": 10},
    "Absorb": {"power": 6},
    "Acid": {"power": 6},
    "Psychic": {"power": 12},
    "Swift": {"power": 8},
    "Recover": {"power": 0},
    "Poison Sting": {"power": 6},
    "Twineedle": {"power": 7},
    "Pin Missile": {"power": 7},
    "Confusion": {"power": 7},
    "Fury Attack": {"power": 6},
    "Drill Peck": {"power": 10},
    "Agility": {"power": 0},
    "Wing Attack": {"power": 8},
    "Hyper Fang": {"power": 10},
    "Super Fang": {"power": 8},
    "Pound": {"power": 5},
    "Sing": {"power": 0},
    "Bite": {"power": 7},
    "Wrap": {"power": 6},
    "Constrict": {"power": 6},
    "Barrage": {"power": 6},
    "Leech Seed": {"power": 0},
    "Bone Club": {"power": 8},
    "Headbutt": {"power": 9},
    "Horn Attack": {"power": 8},
    "Stomp": {"power": 9},
    "Bind": {"power": 6},
    "Sonic Boom": {"power": 6},
    "Hypnosis": {"power": 0},
    "Dream Eater": {"power": 11}
}


# list of pokemon player owns, current moves, and stats
player_pokemon = {
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
        "moves": ["Scratch","Ember"],  # currently knows
        "gender": "male",
        "pokedex_inv_id": 1
    }
}

starter_pokemon = ["Charmander", "Bulbasaur", "Squirtle"]

# list of all items, the stats they change, and time (e.g. health, 1, 5.0, extra info or abilities)
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
# list of all NPCs and interaction options

# LOAD SAVE

# define save_game function:
#   - gather player pokemon IDs, joined by 'P'
#   - gather item IDs, joined by 'I'
#   - gather city progress flags, joined by 'C'
#   - encode final string in simple cipher (shift letters, reverse, etc.)
#   - write encoded save data to file
#   - return back to pause menu

# define load_game function:
#   - read save file
#   - decode data back into components
#   - reconstruct player's pokemon, inventory, progress, location
#   - load world state and return to main menu




# PAUSE MENU + INPUT SYSTEM

# define new_scene function:
#   - empties the current save of teminal output in variable
#   - clears screen

def pause_menu(player_pokemon, original_pokemon_data):
    clear_screen()
    print("PAUSE MENU")
    print("1) LOAD\n2) SAVE\n3) INVENTORY\n4) POKEDEX\n5) MAP\n6) RETURN")
    choice = ginput("Choose an option: ", "1","2","3","4","5","6")
    if choice == "6":
        restore_scene()
    elif choice == "5":
        show_map()
    elif choice == "4":
        open_pokedex(player_pokemon, original_pokemon_data)
    elif choice == "3":
        open_inv()
    else:
        log_print(f"Option {choice} selected. (Feature not implemented yet)")
        time.sleep(1)
        restore_scene()

def show_map():
    new_scene()
    log_print("MAP")
    for loc, discovered in discovered_locations.items():
        if discovered:
            log_print(f"- {loc}")
        else:
            log_print("- ???") 
    log_print("\nPress any key to return")
    input()
    restore_scene()


# define ginput function:
#   - take input and list of valid options
#   - if input == 'p': open pause_menu
#   - otherwise return valid option
def pinput(prompt, *val_opts):
    while True:
        user_input = input(prompt).strip()
        
        # Check if input matches a valid option (as string)
        if user_input in val_opts:
            return user_input
        
        # Try int
        try:
            int_val = int(user_input)
            if int_val in val_opts:
                return int_val
        except ValueError:
            pass

        # Try float
        try:
            float_val = float(user_input)
            if float_val in val_opts:
                return float_val
        except ValueError:
            pass

        log_print(f"Invalid input: '{user_input}'. Please choose from {val_opts}.")

def ginput(prompt, *val_opts):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "p":
            pause_menu(player_pokemon, original_pokemon_data)
            continue
        
        # Check if input matches a valid option (as string)
        if user_input in val_opts:
            return user_input
        
        # Try int
        try:
            int_val = int(user_input)
            if int_val in val_opts:
                return int_val
        except ValueError:
            pass

        # Try float
        try:
            float_val = float(user_input)
            if float_val in val_opts:
                return float_val
        except ValueError:
            pass

        log_print(f"Invalid input: '{user_input}'. Please choose from {val_opts} or type 'p' for pause menu.")


# INVENTORY + PARTY MANAGEMENT


# define open_inventory function:
#   - list all items with quantities
#   - let player choose to use items or sort

def open_inv():
    new_scene()
    if not player_inv:
        log_print("Your inventory is empty!")
    else:
        log_print("=== INVENTORY ===")
        for idx, item in enumerate(player_inv, 1):
            log_print(f"{idx}) {item}")
        
        choice = ginput("\n1) Use Item\n2) Return\nChoice: ", "1", "2")
        if choice == "1":
            item_choice = ginput("Which item? ", *[str(i) for i in range(1, len(player_inv)+1)])
            use_item(player_inv[int(item_choice)-1])
    
    log_print("\nPress any key to return")
    input()
    restore_scene()

player_inv = []


# define use_item function:
#   - heal pokemon, cure status, use pokeball, etc.

def use_item(item_name):
    global player_pokemon, player_inv
    
    if item_name not in items:
        log_print("Invalid item!")
        return
    
    item_data = items[item_name]
    
    # Show pokemon to use item on
    if item_data["target"] == "curr_pokemon":
        log_print("\nChoose a Pokemon:")
        for slot, poke in player_pokemon.items():
            log_print(f"{slot}) {poke['nickname']} - HP: {poke['hp']}/{poke['max_hp']}")
        
        poke_choice = ginput("Choose: ", *[str(s) for s in player_pokemon.keys()])
        selected_poke = player_pokemon[int(poke_choice)]
        
        if item_data["stat"] == "health":
            old_hp = selected_poke["hp"]
            selected_poke["hp"] = min(selected_poke["max_hp"], selected_poke["hp"] + item_data["value"])
            healed = selected_poke["hp"] - old_hp
            log_print(f"{selected_poke['nickname']} was healed for {healed} HP!")
            player_inv.remove(item_name)
        
        elif item_data["stat"] == "atk":
            selected_poke["atk"] += item_data["value"]
            log_print(f"{selected_poke['nickname']}'s Attack increased by {item_data['value']}!")
            player_inv.remove(item_name)
        
        elif item_data["stat"] == "defense":
            selected_poke["defense"] += item_data["value"]
            log_print(f"{selected_poke['nickname']}'s Defense increased by {item_data['value']}!")
            player_inv.remove(item_name)
        
        elif item_data["stat"] == "speed":
            selected_poke["speed"] += item_data["value"]
            log_print(f"{selected_poke['nickname']}'s Speed increased by {item_data['value']}!")
            player_inv.remove(item_name)

# define open_party function:
#   - show player's 6 pokemon
#   - allow rearranging, swapping with storage

def open_party(player_pokemon, player_party):
    for i in player_party:
        print(i)
    temp_choice = ginput("OPTIONS:\n1) Edit Party\n2) Return", "1","2")
    if temp_choice == "1":
        count = 0
        for i in player_party:
            count += 1
            print(f"{count}) {i}")


# define pc_storage function:
#   - store extra pokemon not in party



# POKEDEX SYSTEM


# define open_pokedex function:
#   - display list of seen/caught pokemon
#   - show info if caught, silhouette if not
#   - allow search by name or type

def open_pokedex(player_pokemon,original_pokemon_data):
    new_scene()
    count = 0
    for i in original_pokemon_data:
        count += 1
        print(f"{count}) {i}")
    choice_temp = pinput("\nActions:\n1) Sort\n2) Return\nChoice: ", "1", "2")
    if choice_temp == "1":
        choice_temp = ginput("Options:\n1) Owned\n2) Not Owned\n3) Return\nChoice: ", "1","2","3")
        if choice_temp == "1":
            for slot, poke in player_pokemon.items():
                print(f"{poke['nickname']} ({poke['species_name']}) - Lv {poke['level']}")
        elif choice_temp == "2":
            owned = [p["species_name"] for p in player_pokemon.values()]
            for species in original_pokemon_data:
                if species not in owned:
                    print(f"??? - {species}")
    
    log_print("\nPress any key to return")
    input()
    restore_scene()

# BATTLE SYSTEM


# define player_turn function:
#   - options: attack, items, switch, run
#   - use isopt to validate
#   - return chosen action


# define op_turn function:  # gym leaders & trainers
#   - choose strongest or random move
#   - small chance to use healing item
#   - switch pokemon if low HP
def op_turn():
    "hello"


# define pok_turn function: # wild pokemon
#   - choose random available move

# define attack function:
#   - check accuracy
#   - determine type effectiveness multiplier
#   - calculate damage based on stats + move power
#   - apply damage and check faint

# define run_attempt function:
#   - calculate run success based on speed difference

def get_active_pokemon(player_party):
    for slot, p in player_party.items():
        if p["hp"] > 0:
            return slot, p
    return None, None  # all fainted


def is_party_alive(player_party):
    for p in player_party.values():
        if p["hp"] > 0:
            return True
    return False

def deal_damage(attacker, defender, move_name):
    move = moves_data[move_name]
    power = move["power"]

    # basic formula you can expand later
    dmg = max(1, (attacker["atk"] + power) - defender["defense"])

    defender["hp"] -= dmg
    if defender["hp"] < 0:
        defender["hp"] = 0

    log_print(f"{attacker['nickname']} used {move_name}! It dealt {dmg} damage!")

def player_turn(active_player, active_opponent, is_wild=False):
    log_print("\nYour turn!")
    log_print("1) Attack")
    log_print("2) Use Item")
    if is_wild:
        log_print("3) Try to Catch")
        log_print("4) Run")
        choice = ginput("Choose action: ", "1", "2", "3", "4")
    else:
        log_print("3) Run")
        choice = ginput("Choose action: ", "1", "2", "3")
    
    if choice == "1":
        log_print("\nChoose a move:")
        for i, mv in enumerate(active_player["moves"], start=1):
            log_print(f"{i}) {mv}")
        
        move_choice = ginput("Move: ", *[str(i) for i in range(1, len(active_player["moves"])+1)])
        chosen_move = active_player["moves"][int(move_choice)-1]
        deal_damage(active_player, active_opponent, chosen_move)
        return "attack"
    
    elif choice == "2":
        if not player_inv:
            log_print("No items to use!")
            return player_turn(active_player, active_opponent, is_wild)
        
        log_print("\nItems:")
        for idx, item in enumerate(player_inv, 1):
            log_print(f"{idx}) {item}")
        
        item_choice = ginput("Which item? ", *[str(i) for i in range(1, len(player_inv)+1)])
        use_item(player_inv[int(item_choice)-1])
        return "item"
    
    elif choice == "3" and is_wild:
        # Try to catch
        if "Pokeball" not in player_inv:
            log_print("You don't have any Pokeballs!")
            return player_turn(active_player, active_opponent, is_wild)
        
        catch_rate = 0.3 + (1 - active_opponent["hp"] / active_opponent["max_hp"]) * 0.5
        if random.random() < catch_rate:
            log_print(f"You caught {active_opponent['nickname']}!")
            
            # Add to player pokemon
            new_slot = max(player_pokemon.keys()) + 1
            player_pokemon[new_slot] = active_opponent.copy()
            player_inv.remove("Pokeball")
            return "caught"
        else:
            log_print(f"{active_opponent['nickname']} broke free!")
            player_inv.remove("Pokeball")
            return "failed_catch"
    
    elif (choice == "4" and is_wild) or (choice == "3" and not is_wild):
        # Try to run
        if random.random() < 0.5:
            log_print("You ran away!")
            return "ran"
        else:
            log_print("Couldn't escape!")
            return "failed_run"

def pok_turn(active_player, active_opponent):
    move = random.choice(active_opponent["moves"])
    log_print("\nEnemy turn!")
    deal_damage(active_opponent, active_player, move)


# define battle function:
#   - while both sides have usable pokemon:
#       - player_turn
#       - if enemy alive: op_turn or pok_turn
#   - award exp, items, money if player wins

def gain_exp(pokemon, amount):
    pokemon["exp"] += amount
    log_print(f"{pokemon['nickname']} gained {amount} EXP!")
    
    while pokemon["exp"] >= pokemon["exp_to_next"]:
        pokemon["exp"] -= pokemon["exp_to_next"]
        pokemon["level"] += 1
        
        # Stat increases
        pokemon["max_hp"] += 3
        pokemon["hp"] += 3
        pokemon["atk"] += 1
        pokemon["defense"] += 1
        pokemon["speed"] += 1
        
        log_print(f"\n*** {pokemon['nickname']} leveled up to Level {pokemon['level']}! ***")
        log_print(f"HP +3, ATK +1, DEF +1, SPD +1")
        
        pokemon["exp_to_next"] = int(pokemon["exp_to_next"] * 1.2)

def battle(player_party, enemy_data, enemy_type="wild"):
    enemy = enemy_data.copy()
    enemy["nickname"] = enemy.get("name", enemy["species_name"])
    enemy["max_hp"] = enemy["hp"]

    if "moves" not in enemy:
        enemy["moves"] = ["Tackle"]

    log_print(f"A {enemy['nickname']} appeared!\n")

    while True:
        slot, active_player = get_active_pokemon(player_party)
        if active_player is None:
            log_print("All your Pokémon fainted!")
            return "lose"

        if enemy["hp"] <= 0:
            log_print(f"You defeated {enemy['nickname']}!")
            # Award EXP
            exp_gain = enemy.get("level", 5) * 15  # Reduced from 20 to 15
            gain_exp(active_player, exp_gain)
            return "win"

        is_wild = (enemy_type == "wild")
        action = player_turn(active_player, enemy, is_wild)

        if action == "ran":
            return "ran"
        if action == "caught":
            return "caught"

        if enemy["hp"] <= 0:
            log_print(f"You defeated {enemy['nickname']}!")
            exp_gain = enemy.get("level", 5) * 15  # Reduced from 20 to 15
            gain_exp(active_player, exp_gain)
            return "win"

        if action in ["attack", "failed_catch", "failed_run"]:
            pok_turn(active_player, enemy)

        if active_player["hp"] <= 0:
            log_print(f"{active_player['nickname']} fainted!\n")
            if not is_party_alive(player_party):
                log_print("All your Pokémon fainted!")
                return "lose"


# LEGENDARY & SPECIAL BATTLES


# define mew_battle function:
#   - unique intro text + warnings
#   - boosted stats for mew
#   - no running allowed
#   - if win: unlock endgame screen
def mew_battle():
    text("You Found Mewtwo!")
    time.sleep(1)
    new_scene()
    text("Mewtwo stares at you with intense psychic power...")
    text("This is the ultimate challenge!")
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
    
    result = battle(player_pokemon, mewtwo_data, "legendary")
    
    if result == "win":
        new_scene()
        text("=" * 50)
        text("CONGRATULATIONS!")
        text("You have defeated Mewtwo and become the ultimate Pokemon Master!")
        text("=" * 50)
        time.sleep(3)
        return True
    else:
        text("Mewtwo was too powerful... Try training more!")
        return False

# define rare_legendary_encounter:
#   - very low chance during area exploration
#   - unique catch difficulty and moves



# CITIES, GYMS, AND AREAS


# define enter_city function:
#   - show city name + description
#   - give list of places: shops, healing center, gym, special area, NPC interactions
#   - player chooses where to go

cities = {
    "Pallet Town": {
        "shops": ["General Store"],
        "healing_center": True,
        "gym": False,
        "special_area": "Grassy Fields",
        "description": "A quiet town where your journey begins.",
        "gym_leader": None,
        "city_level": 1
    },
    "Viridian City": {
        "shops": ["Potion Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Viridian Forest",
        "description": "A city surrounded by lush forests.",
        "gym_leader": {"name": "Giovanni", "type": "normal", "badge": "Earth Badge"},
        "city_level": 2
    },
    "Pewter City": {
        "shops": ["Rock Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Rocky Mountains",
        "description": "A city known for its rocky terrain.",
        "gym_leader": {"name": "Brock", "type": "rock", "badge": "Boulder Badge"},
        "city_level": 3
    },
    "Cerulean City": {
        "shops": ["Water Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Cerulean Cave",
        "description": "A city by the water with a mysterious cave.",
        "gym_leader": {"name": "Misty", "type": "water", "badge": "Cascade Badge"},
        "city_level": 4
    },
    "Vermilion City": {
        "shops": ["Electric Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Port Docks",
        "description": "A port city with electric energy.",
        "gym_leader": {"name": "Lt. Surge", "type": "electric", "badge": "Thunder Badge"},
        "city_level": 5
    },
    "Lavender Town": {
        "shops": ["Mysterious Shop"],
        "healing_center": True,
        "gym": False,
        "special_area": "Pokemon Tower",
        "description": "A quiet, eerie town with a haunted tower.",
        "gym_leader": None,
        "city_level": 6
    },
    "Celadon City": {
        "shops": ["Mega Store", "Evolution Stones"],
        "healing_center": True,
        "gym": True,
        "special_area": "Game Corner",
        "description": "The biggest city with a huge department store.",
        "gym_leader": {"name": "Erika", "type": "grass", "badge": "Rainbow Badge"},
        "city_level": 7
    },
    "Fuchsia City": {
        "shops": ["Safari Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Safari Zone",
        "description": "A city with an exotic safari zone.",
        "gym_leader": {"name": "Koga", "type": "poison", "badge": "Soul Badge"},
        "city_level": 8
    },
    "Saffron City": {
        "shops": ["Psychic Shop", "General Store"],
        "healing_center": True,
        "gym": True,
        "special_area": "Silph Co. Building",
        "description": "A bustling metropolis with psychic energy.",
        "gym_leader": {"name": "Sabrina", "type": "psychic", "badge": "Marsh Badge"},
        "city_level": 9
    },
    "Cinnabar Island": {
        "shops": ["Volcano Shop"],
        "healing_center": True,
        "gym": True,
        "special_area": "Volcano Cave",
        "description": "An island with an active volcano and secret labs.",
        "gym_leader": {"name": "Blaine", "type": "fire", "badge": "Volcano Badge"},
        "city_level": 10
    }
}

special_areas = {
    "Grassy Fields": {
        "pokemon_types": ["grass", "normal", "flying"],
        "pokemon_pool": ["Pidgey", "Rattata", "Meowth"],
        "pokemon_lvl_range": (2, 4),
        "items": ["Health Potion", "Pokeball"]
    },
    "Viridian Forest": {
        "pokemon_types": ["bug", "grass"],
        "pokemon_pool": ["Caterpie", "Weedle", "Pidgey"],
        "pokemon_lvl_range": (4, 7),
        "items": ["Health Potion", "Super Potion"]
    },
    "Rocky Mountains": {
        "pokemon_types": ["rock", "ground"],
        "pokemon_pool": ["Geodude", "Onix"],
        "pokemon_lvl_range": (7, 11),
        "items": ["Protein", "Iron"]
    },
    "Cerulean Cave": {
        "pokemon_types": ["water", "psychic"],
        "pokemon_pool": ["Psyduck", "Goldeen", "Gastly"],
        "pokemon_lvl_range": (10, 14),
        "items": ["Super Potion", "Pokeball"],
        "special": "mewtwo_location"
    },
    "Port Docks": {
        "pokemon_types": ["water", "electric"],
        "pokemon_pool": ["Magikarp", "Tentacool", "Pikachu", "Voltorb"],
        "pokemon_lvl_range": (12, 16),
        "items": ["Health Potion", "Carbos"]
    },
    "Pokemon Tower": {
        "pokemon_types": ["ghost"],
        "pokemon_pool": ["Gastly", "Haunter", "Cubone"],
        "pokemon_lvl_range": (14, 19),
        "items": ["Super Potion"]
    },
    "Game Corner": {
        "pokemon_types": ["normal"],
        "pokemon_pool": ["Rattata", "Raticate", "Meowth", "Jigglypuff"],
        "pokemon_lvl_range": (12, 17),
        "items": ["Health Potion", "Pokeball"]
    },
    "Safari Zone": {
        "pokemon_types": ["grass", "normal", "water"],
        "pokemon_pool": ["Oddish", "Bellsprout", "Tangela", "Exeggcute"],
        "pokemon_lvl_range": (17, 22),
        "items": ["Super Potion", "Pokeball", "Protein"]
    },
    "Silph Co. Building": {
        "pokemon_types": ["normal"],
        "pokemon_pool": ["Raticate", "Jigglypuff"],
        "pokemon_lvl_range": (20, 24),
        "items": ["Iron", "Carbos"]
    },
    "Volcano Cave": {
        "pokemon_types": ["fire"],
        "pokemon_pool": ["Vulpix", "Growlithe", "Ponyta", "Magmar"],
        "pokemon_lvl_range": (22, 28),
        "items": ["Fire Stone", "Super Potion"]
    }
}

def explore_special_area(area_name):
    """Explore a special area, with chances to find Pokemon and items"""
    global collected_items
    
    if area_name not in special_areas:
        log_print("This area doesn't exist!")
        return
    
    area = special_areas[area_name]
    new_scene()
    log_print(f"=== {area_name} ===")
    log_print("You explore the area...")
    time.sleep(1)
    # Check for Mewtwo in Cerulean Cave
    for i in range(10):
        gym_badges.append("hi")
    if area.get("special") == "mewtwo_location" and len(gym_badges) >= 8:
        encounter = ginput("\nYou sense an incredibly powerful presence deeper in the cave...\nInvestigate? (y/n): ", "y", "n")
        if encounter == "y":
            if mew_battle():
                return
    
    # Random encounter
    if random.random() < 0.6:  # 60% chance
        log_print("\nA wild Pokemon appeared!")
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
        
        result = battle(player_pokemon, wild_pokemon, "wild")
        
        if result == "lose":
            heal_all_pokemon()
            log_print("\nYou rushed to the Pokemon Center!")
    
    # Find items
    if random.random() < 0.4:  # 40% chance
        item_key = f"{area_name}_item_{random.randint(1,100)}"
        if item_key not in collected_items:
            found_item = random.choice(area["items"])
            log_print(f"\nYou found a {found_item}!")
            player_inv.append(found_item)
            collected_items[item_key] = True
    
    log_print("\nPress any key to leave")
    input()

def enter_city(city_name):
    """Enter a city and choose where to go"""
    global current_location, discovered_locations
    
    discovered_locations[city_name] = True
    current_location = city_name
    
    while True:
        new_scene()
        city = cities[city_name]
        log_print(f"=== {city_name.upper()} ===")
        log_print(city["description"])
        log_print("\nWhere would you like to go?")
        
        options = []
        option_num = 1
        
        if city["healing_center"]:
            log_print(f"{option_num}) Pokemon Center")
            options.append("center")
            option_num += 1
        
        if city["shops"]:
            log_print(f"{option_num}) Shop")
            options.append("shop")
            option_num += 1
        
        if city["gym"]:
            badge_name = city["gym_leader"]["badge"]
            if badge_name in gym_badges:
                log_print(f"{option_num}) Gym (Already beaten)")
            else:
                log_print(f"{option_num}) Gym")
            options.append("gym")
            option_num += 1
        
        if city["special_area"]:
            log_print(f"{option_num}) {city['special_area']}")
            options.append("special")
            option_num += 1
        
        log_print(f"{option_num}) Travel to another city")
        options.append("travel")
        option_num += 1
        
        log_print(f"{option_num}) View Party")
        options.append("party")
        
        choice = ginput("\nChoice: ", *[str(i) for i in range(1, option_num+1)])
        selected = options[int(choice)-1]
        
        if selected == "center":
            healing_center()
        elif selected == "shop":
            shop(city["shops"])
        elif selected == "gym":
            if city["gym_leader"] and city["gym_leader"]["badge"] not in gym_badges:
                gym_battle(city["gym_leader"])
        elif selected == "special":
            explore_special_area(city["special_area"])
        elif selected == "travel":
            travel_menu(city_name)
            # After travel_menu returns, we're in a new city or staying
            # Break out of this city's loop
            break
        elif selected == "party":
            view_party()

def heal_all_pokemon():
    """Heal all Pokemon to full HP"""
    for poke in player_pokemon.values():
        poke["hp"] = poke["max_hp"]

def healing_center():
    new_scene()
    log_print("=== POKEMON CENTER ===")
    log_print("Welcome! Let me heal your Pokemon!")
    time.sleep(1)
    log_print("Healing...")
    time.sleep(1)
    heal_all_pokemon()
    log_print("Your Pokemon are fully healed!")
    time.sleep(1)

def shop(shop_types):
    """Shop to buy items"""
    global player_money
    
    while True:
        new_scene()
        log_print("=== SHOP ===")
        log_print(f"Money: ${player_money}")
        log_print("\nItems for sale:")
        
        available_items = []
        if "General Store" in shop_types:
            available_items.extend(["Health Potion", "Super Potion", "Pokeball"])
        if "Evolution Stones" in shop_types:
            available_items.append("Fire Stone")
        if any(shop in shop_types for shop in ["Psychic Shop", "Rock Shop", "Water Shop", "Electric Shop"]):
            available_items.extend(["Protein", "Iron", "Carbos"])
        
        for idx, item_name in enumerate(available_items, 1):
            price = items[item_name]["sale_price"]
            log_print(f"{idx}) {item_name} - ${price}")
        
        log_print(f"{len(available_items)+1}) Leave")
        
        choice = ginput("\nWhat would you like to buy? ", *[str(i) for i in range(1, len(available_items)+2)])
        
        if int(choice) <= len(available_items):
            item_name = available_items[int(choice)-1]
            price = items[item_name]["sale_price"]
            
            if player_money >= price:
                player_money -= price
                player_inv.append(item_name)
                log_print(f"\nYou bought {item_name}!")
                time.sleep(1)
            else:
                log_print("\nNot enough money!")
                time.sleep(1)
        else:
            # Leave shop
            break

def gym_battle(gym_leader):
    """Battle a gym leader"""
    global gym_badges
    
    new_scene()
    log_print(f"=== {gym_leader['name'].upper()}'S GYM ===")
    log_print(f"Gym Leader {gym_leader['name']} challenges you!")
    time.sleep(2)
    
    # Create gym leader's Pokemon based on progression
    base_level = 10 + (len(gym_badges) * 4)  # Scales with badges earned
    
    leader_pokemon = {
        "species_name": "Leader Pokemon",
        "name": f"{gym_leader['name']}'s Pokemon",
        "level": base_level,
        "type": [gym_leader["type"]],
        "hp": 50 + (len(gym_badges) * 8),
        "max_hp": 50 + (len(gym_badges) * 8),
        "atk": 10 + (len(gym_badges) * 2),
        "defense": 8 + (len(gym_badges) * 2),
        "speed": 8 + len(gym_badges),
        "moves": ["Tackle", "Quick Attack"]
    }
    
    result = battle(player_pokemon, leader_pokemon, "trainer")
    
    if result == "win":
        gym_badges.append(gym_leader["badge"])
        log_print(f"\nCongratulations! You earned the {gym_leader['badge']}!")
        player_inv.append("Super Potion")
        log_print("You also received a Super Potion!")
        time.sleep(2)
    else:
        log_print(f"\n{gym_leader['name']} was too strong! Train more and come back!")
        time.sleep(2)

def view_party():
    """View your Pokemon party"""
    new_scene()
    log_print("=== YOUR PARTY ===")
    for slot, poke in player_pokemon.items():
        log_print(f"\n{slot}) {poke['nickname']} ({poke['species_name']})")
        log_print(f"   Level: {poke['level']}")
        log_print(f"   HP: {poke['hp']}/{poke['max_hp']}")
        log_print(f"   ATK: {poke['atk']} | DEF: {poke['defense']} | SPD: {poke['speed']}")
        log_print(f"   EXP: {poke.get('exp', 0)}/{poke['exp_to_next']}")
    
    log_print("\nPress any key to return")
    input()

# define city_location function (generic):
#   - for forests, caves, haunted houses, beaches, etc.
#   - show area description
#   - while exploring:
#       - random chance of wild pokemon
#       - random chance of finding items
#       - random chance of trainer battle
#       - allow player to leave

# define gym function:
#   - force player to fight 2-3 trainers inside
#   - then trigger boss battle
#   - if win: award badge + unlock next city

# define npc_interaction function:
#   - display dialogue
#   - give item, quest, or hint depending on NPC



# ROUTES & TRAVEL SYSTEM


# define travel_to_city function:
#   - check if path is unlocked
#   - if locked: show message
#   - if unlocked: move player to next area

routes = {
    "Route 1": {
        "connects": ["Pallet Town", "Viridian City"],
        "distance": 3,
        "pokemon_pool": ["Pidgey", "Rattata"],
        "pokemon_lvl_range": (3, 5),
        "trainer_chance": 0.2
    },
    "Route 2": {
        "connects": ["Viridian City", "Pewter City"],
        "distance": 4,
        "pokemon_pool": ["Pidgey", "Spearow", "Caterpie"],
        "pokemon_lvl_range": (5, 8),
        "trainer_chance": 0.3
    },
    "Route 3": {
        "connects": ["Pewter City", "Cerulean City"],
        "distance": 5,
        "pokemon_pool": ["Geodude", "Pidgeotto"],
        "pokemon_lvl_range": (8, 12),
        "trainer_chance": 0.3
    },
    "Route 4": {
        "connects": ["Cerulean City", "Vermilion City"],
        "distance": 4,
        "pokemon_pool": ["Magikarp", "Psyduck", "Pikachu"],
        "pokemon_lvl_range": (11, 15),
        "trainer_chance": 0.3
    },
    "Route 5": {
        "connects": ["Vermilion City", "Lavender Town"],
        "distance": 3,
        "pokemon_pool": ["Pidgeotto", "Gastly", "Meowth"],
        "pokemon_lvl_range": (13, 17),
        "trainer_chance": 0.3
    },
    "Route 6": {
        "connects": ["Lavender Town", "Celadon City"],
        "distance": 4,
        "pokemon_pool": ["Oddish", "Bellsprout", "Pidgeotto"],
        "pokemon_lvl_range": (16, 20),
        "trainer_chance": 0.4
    },
    "Route 7": {
        "connects": ["Celadon City", "Fuchsia City"],
        "distance": 5,
        "pokemon_pool": ["Oddish", "Raticate", "Butterfree"],
        "pokemon_lvl_range": (18, 23),
        "trainer_chance": 0.4
    },
    "Route 8": {
        "connects": ["Fuchsia City", "Saffron City"],
        "distance": 4,
        "pokemon_pool": ["Haunter", "Fearow", "Raticate"],
        "pokemon_lvl_range": (21, 26),
        "trainer_chance": 0.4
    },
    "Route 9": {
        "connects": ["Saffron City", "Cinnabar Island"],
        "distance": 6,
        "pokemon_pool": ["Growlithe", "Ponyta", "Graveler"],
        "pokemon_lvl_range": (24, 29),
        "trainer_chance": 0.5
    }
}

def travel_menu(city_name):
    """Show available cities to travel to"""
    global current_location
    
    while True:
        new_scene()
        log_print("=== TRAVEL ===")
        log_print(f"Current location: {current_location}")
        log_print("\nAvailable routes:")
        
        available_routes = []
        for route_name, route_data in routes.items():
            if current_location in route_data["connects"]:
                destination = [c for c in route_data["connects"] if c != current_location][0]
                available_routes.append((route_name, destination))
        
        for idx, (route, dest) in enumerate(available_routes, 1):
            log_print(f"{idx}) {route} -> {dest}")
        
        log_print(f"{len(available_routes)+1}) Stay here")
        
        choice = ginput("\nWhere do you want to go? ", *[str(i) for i in range(1, len(available_routes)+2)])
        
        if int(choice) <= len(available_routes):
            route_name, destination = available_routes[int(choice)-1]
            travel_route(route_name, destination, city_name)
            # After travel_route, we're in new city, so return to caller
            return
        else:
            enter_city(city_name)


# define route function:
#   - traveling between cities
#   - chance of random encounters
#   - chance of finding trainers
#   - chance of environmental events

def travel_route(route_name, destination, city_name):
    """Travel along a route with encounters"""
    global current_location, discovered_locations, defeated_trainers
    
    route = routes[route_name]
    new_scene()
    log_print(f"=== Traveling {route_name} ===")
    log_print(f"Distance: {route['distance']} km\n")
    
    discovered_locations[route_name] = True
    
    # Progress bar
    for i in range(route["distance"]):
        progress = int((i / route["distance"]) * 20)
        bar = "=" * progress + " " * (20 - progress)
        print(f"\r[{bar}] {i}/{route['distance']} km", end="", flush=True)
        time.sleep(0.5)
        
        # Random encounter during travel
        if random.random() < 0.35:  # 35% chance per segment (reduced)
            print()  # New line after progress bar
            
            if random.random() < route["trainer_chance"]:
                # Trainer battle
                trainer_id = f"{route_name}_trainer_{i}"
                if trainer_id not in defeated_trainers:
                    log_print("\nA trainer spotted you!")
                    time.sleep(1)
                    
                    # Trainer Pokemon scale with route level
                    trainer_level = (route["pokemon_lvl_range"][0] + route["pokemon_lvl_range"][1]) // 2
                    
                    trainer_pokemon = {
                        "species_name": "Trainer Pokemon",
                        "name": "Trainer's Pokemon",
                        "level": trainer_level,
                        "type": ["normal"],
                        "hp": 30 + trainer_level * 2,
                        "max_hp": 30 + trainer_level * 2,
                        "atk": 8 + (trainer_level // 2),
                        "defense": 6 + (trainer_level // 2),
                        "speed": 7 + (trainer_level // 3),
                        "moves": ["Tackle", "Quick Attack"]
                    }
                    
                    result = battle(player_pokemon, trainer_pokemon, "trainer")
                    
                    if result == "win":
                        defeated_trainers.append(trainer_id)
                        prize_money = 50 + (trainer_level * 10)
                        global player_money
                        player_money += prize_money
                        log_print(f"\nYou won ${prize_money}!")
                        time.sleep(1)
                    elif result == "lose":
                        log_print("\nYou blacked out and returned to the Pokemon Center!")
                        heal_all_pokemon()
                        enter_city(city_name)
                    
                    progress = int((i / route["distance"]) * 20)
                    bar = "=" * progress + " " * (20 - progress)
                    print(f"\r[{bar}] {i}/{route['distance']} km", end="", flush=True)
            
            else:
                # Wild Pokemon
                log_print("\nA wild Pokemon appeared!")
                species = random.choice(route["pokemon_pool"])
                level = random.randint(*route["pokemon_lvl_range"])
                
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
                
                result = battle(player_pokemon, wild_pokemon, "wild")
                
                if result == "lose":
                    log_print("\nYou blacked out and returned to the Pokemon Center!")
                    heal_all_pokemon()
                    return
                
                # Resume progress bar
                progress = int((i / route["distance"]) * 20)
                bar = "=" * progress + " " * (20 - progress)
                print(f"\r[{bar}] {i}/{route['distance']} km", end="", flush=True)
    
    # Complete journey
    progress = 20
    bar = "=" * progress
    print(f"\r[{bar}] {route['distance']}/{route['distance']} km")
    
    log_print(f"\nArrived at {destination}!")
    time.sleep(1)
    
    # Update current location and enter the new city
    current_location = destination
    enter_city(destination)



while True:
    name = input("What is your name: ").strip()
    if name:  # Make sure they entered something
        confirm = ginput(f"Are you sure you want to be called '{name}'? (y/n): ", "y", "n")
        if confirm == "y":
            break
new_scene()

# Main menu
new_scene()
log_print("Pokemon")
#log_print("1) Load Save Data")
#log_print("2) Start New Game")

#choice = ginput("Choose an option: ", "1", "2")

#if choice == "1":
#    log_print("Loading game...")
#    # open saves.txt file
#    try:
#        open("pokemon_game/saves.txt")
#        print("found")
#    except FileNotFoundError:
#        print("not found")
#    # search for names
#    # print names to choose from
#    # choose which one to load with timestamps
#    # overide the current save data with load data
#    # give options to return throughout interaction
#    # give option to input own throughout interaction
    
#else:
#    # Loading animation for starting new game
#    for _ in range(2):
#        new_scene()
#        for dots in ["", ".", "..", "..."]:
#            print(f"Starting new game{dots}")
#            time.sleep(0.4)
#            new_scene()
#    print(title_ascii)
#    time.sleep(2)
print(title_ascii)

#    time.sleep(2)

input("\n\n\nenter any key to continue")
new_scene()
# Show starter Pokémon in current scene
start_pok_names = []
start_pok_ascii = []
start_pok_stats = []
for species in starter_pokemon:
    data = original_pokemon_data[species]

new_scene()
text(f"Welcome {name}, before you start your adventure, choose your starter Pokémon:\n")
time.sleep(1)

for i, species in enumerate(starter_pokemon, start=1):
    data = original_pokemon_data[species]
    log_print(f"{i}) {species}")
    log_print(f"   Type: {', '.join(data['type'])}")
    log_print(f"   HP: {data['base_hp']}  ATK: {data['base_atk']}  DEF: {data['base_defense']}  SPD: {data['base_speed']}")
    log_print("")  # blank line

choice_temp = i in enumerate(starter_pokemon)
choice = ginput("Choose your starter: ", "1", "2", "3")
starter_species = starter_pokemon[int(choice)-1]

player_pokemon = {
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

new_scene()
text(f"Nice choice! {starter_pokemon[int(choice)-1]} is a great pokemon.")
text("Now lets give you some tips")
time.sleep(2)
new_scene()
text("First, at any point in the game, if there is an input, then if you type 'p', it will open the pause menu. Maybe try it after the instructions.")
time.sleep(2)
new_scene()
text("If you ever want to save your game, you can do so in the pause menu, or if you ever want to load a save, you can do so in the pause menu.")
time.sleep(2)
new_scene()
text("There are also some really strong pokemon out there so be careful, but they could also make you stronger, which may help you in finding and beating Mewtwo, one of the strongest and smartest pokemon out there, and also every pokemon trainers goal")
time.sleep(2)
new_scene()
text("If you find and beat Mewtwo, then you would be considered one of if not the BEST pokemon trainers out there, so get out there, explore, and try to catch them all.")
time.sleep(2)
new_scene()
text("Alright lets get you into your first battle.")
new_scene()
enemy_pokemon = {
    "species_name": "Rattata",
    "name": "Wild Rattata",
    "level": 2,
    "hp": 12,
    "max_hp": 12,
    "atk": 4,
    "defense": 2,
    "speed": 5,
    "moves": ["Tackle"]
}
battle(player_pokemon, enemy_pokemon, "wild")

text("\nWell now that you have won your first fight, it is time for you to head out to the first town, so get out there and enjoy yourself!")
time.sleep(2)
new_scene()

# Give starter items
player_inv.extend(["Health Potion", "Health Potion", "Pokeball", "Pokeball", "Pokeball"])
text("You received some starter items!")
text("- 2x Health Potion")
text("- 3x Pokeball")
time.sleep(2)

# Main game loop - start in Pallet Town
enter_city("Pallet Town")