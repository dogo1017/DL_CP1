
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


# define pause_menu function:
#   - clear screen
#   - show options: save, load, inventory, pokedex, map, return
#   - run correct function based on user choice

# define isopt function:
#   - take input and list of valid options
#   - if input == 'p': open pause_menu
#   - otherwise return valid option



# INVENTORY + PARTY MANAGEMENT


# define open_inventory function:
#   - list all items with quantities
#   - let player choose to use items or sort

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
#   - options: attack, items, switch, run, defend(optional)
#   - use isopt to validate
#   - return chosen action

# define op_turn function:  # gym leaders & trainers
#   - choose strongest or random move
#   - small chance to use healing item
#   - switch pokemon if low HP

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



# LEGENDARY & SPECIAL BATTLES


# define mew_battle function:
#   - unique intro text + warnings
#   - boosted stats for mew
#   - no running allowed
#   - if win: unlock endgame screen

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
