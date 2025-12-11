for i, species in enumerate(starter_pokemon, start=1):
    data = original_pokemon_data[species]
    log_print(f"{i}) {species}")
    log_print(f"   Type: {', '.join(data['type'])}")
    log_print(f"   HP: {data['base_hp']}  ATK: {data['base_atk']}  DEF: {data['base_defense']}  SPD: {data['base_speed']}")
    log_print("")  # blank line

choice_temp = i in enumerate(starter_pokemon)
choice = ginput("Choose your starter: ", 1,2)
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
        "moves": original_pokemon_data[starter_species]["possible_moves"][:2],
        "gender": "male",
        "pokedex_inv_id": 1
    }
}

new_scene()
text(f"Nice choice! {starter_pokemon[choice-1]} is a great pokemon.")
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
    "name": "Wild Bunnip",
    "hp": 18,
    "attack": 4,
    "defense": 2
}
battle(player_pokemon, enemy_pokemon, "wild")

text("Well now that you have won your first fight, it is time for you to head out to the first town, so get out there and enjoy yourself!")
time.sleep(1)
new_scene()