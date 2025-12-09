# DL 1st, final project 


# add sound, remove globals, fix asciis, Test

import time
import random
import os
import sys
from io import StringIO



script_dir = os.path.dirname(os.path.abspath(__file__))
save_file_path = os.path.join(script_dir, 'saves.txt')
#with open(save_file_path, 'w') as file:
#        file.write("Hello")


# Variables:

captured_output = StringIO()
current_scene_log = []

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

def text(message, delay=0.05):
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
    }
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
        "moves": ["Scratch","Ember"],  # currently knows
        "gender": "male",
        "pokedex_inv_id": 1
    }
}

starter_pokemon = [1,2]

# list of all items, the stats they change, and time (e.g. health, 1, 5.0, extra info or abilities)

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

def pause_menu():
    new_scene()
    log_print("PAUSE MENU")
    log_print("1) LOAD\n2) SAVE\n3) INVENTORY\n4) POKEDEX\n5) MAP\n6) RETURN")
    choice = ginput("Choose an option: ", "1","2","3","4","5","6")
    # placeholder logic for pause menu actions
    if choice == "6":
        restore_scene()
    else:
        log_print(f"Option {choice} selected. (Feature not implemented yet)")
        time.sleep(1)
        restore_scene()


# define ginput function:
#   - take input and list of valid options
#   - if input == 'p': open pause_menu
#   - otherwise return valid option

def ginput(prompt, *val_opts):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "p":
            pause_menu()
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
    log_print("1) Potions\n2) Party\n")


# define use_item function:
#   - heal pokemon, cure status, use pokeball, etc.

# define open_party function:
#   - show player's 6 pokemon
#   - allow rearranging, swapping with storage

# define pc_storage function:
#   - store extra pokemon not in party



# POKEDEX SYSTEM


# define open_pokedex function:
#   - display list of seen/caught pokemon
#   - show info if caught, silhouette if not
#   - allow search by name or type


# BATTLE SYSTEM


# define player_turn function:
#   - options: attack, items, switch, run
#   - use isopt to validate
#   - return chosen action

def player_turn(cur_player_bat, cur_op_bat):
    ginput("1) Attack\n2) Items\n3) Switch\n4) Bonus Abilities")



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

# define battle function:
#   - while both sides have usable pokemon:
#       - player_turn
#       - if enemy alive: op_turn or pok_turn
#   - award exp, items, money if player wins

def battle(player_party, op_status, op_type):
    while True:
        if player_party == "alive" and op_status == "alive":
            player_turn()
            if op_type == "gym leader" or op_type == "trainer":
                op_turn()
            else:
                pok_turn()
        elif player_party == "down":
            player_loose()
        elif op_status == "down":
            player_win()




# LEGENDARY & SPECIAL BATTLES


# define mew_battle function:
#   - unique intro text + warnings
#   - boosted stats for mew
#   - no running allowed
#   - if win: unlock endgame screen
def mew_battle():
    text("You Found Mewto")
# define rare_legendary_encounter:
#   - very low chance during area exploration
#   - unique catch difficulty and moves



# CITIES, GYMS, AND AREAS


# define enter_city function:
#   - show city name + description
#   - give list of places: shops, healing center, gym, special area, NPC interactions
#   - player chooses where to go

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

# define route function:
#   - traveling between cities
#   - chance of random encounters
#   - chance of finding trainers
#   - chance of environmental events



# HEALING CENTERS


# define healing_center function:
#   - heal all pokemon
#   - restore PP
#   - auto-rush trigger: 
#       - if entire team HP < certain threshold, instantly teleport player to nearest center



# ITEM SHOPS


# define shop function:
#   - display available items
#   - show prices
#   - confirm purchase
#   - subtract money, add items to inventory

# define stone_shop function:
#   - sells evolution stones

# define special_shop function:
#   - sells TMs or rare goods



# STORIES & WORLD EVENTS


# define city_story_event function:
#   - trigger when first entering a city
#   - may involve NPCs, small quests, or unlocking gym

# define global_story_event function:
#   - triggers after major gym wins or milestones
#   - used for endgame, unlock mew area, etc.


# MAIN GAME LOOP

# while True:
#   - show main menu: new game, load game, credits, quit
#   - if new game: choose starter pokemon
#   - tutorial on battling
#   - send player to first city
#   - continue game through gym progression
#   - after final gym, unlock mew area
#   - after beating mew, show victory screen and option to keep playing


# Ask player name
while True:
    name = input("What is your name: ").strip()
    if name:  # Make sure they entered something
        confirm = ginput(f"Are you sure you want to be called '{name}'? (y/n): ", "y", "n")
        if confirm == "y":
            break

# Main menu
new_scene()
log_print("Pokemon")
log_print("1) Load Save Data")
log_print("2) Start New Game")

choice = ginput("Choose an option: ", "1", "2")

if choice == "1":
    log_print("Loading game...")
    # open saves.txt file
    try:
        open("pokemon_game/saves.txt")
        print("found")
    except FileNotFoundError:
        print("not found")
    # search for names
    # print names to choose from
    # choose which one to load with timestamps
    # overide the current save data with load data
    # give options to return throughout interaction
    # give option to input own throughout interaction
    
else:
    # Loading animation for starting new game
    for _ in range(2):
        new_scene()
        for dots in ["", ".", "..", "..."]:
            print(f"Starting new game{dots}")
            time.sleep(0.4)
            new_scene()
    print(title_ascii)
    time.sleep(2)

input("\n\n\nenter any key to continue")
new_scene()
# Show starter Pokémon in current scene
start_pok_names = []
start_pok_ascii = []
start_pok_stats = []
#for pokemon in starter_pokemon:
    #start_pok_names.append(original_pokemon_data[starter_pokemon[pokemon]][name])
    #start_pok_ascii.append(original_pokemon_data[starter_pokemon[pokemon]][ascii_battle])
    #start_pok_stats.append(original_pokemon_data[starter_pokemon[pokemon]][stats])
chosen_starter = ginput(f"Welcome {name}, Before you start your adventure, we should get you your starter pokemon:\n\n{"hello"}", *starter_pokemon)
player_pokemon.append(original_pokemon_data[chosen_starter])
new_scene()
text(f"Nice choice! {original_pokemon_data[chosen_starter]} is a great pokemon.")
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
battle()




