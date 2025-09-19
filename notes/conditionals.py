#DL 1st, conditionals Notes
import random

game_info = {"player_hp": 20,
             "player_attack": 2,
             "player_damage": 2,
             "player_defense": 5,
             "monster_hp": 15,
             "monster_attack": 3,
             "monster_damage": 10,
             "monster_defense": 2}

damage_roll = random.randint(1,8) + game_info["player_damage"]
hit_roll = random.randint(1,20)

if hit_roll == 20:
    print("You got a crit! That means you get to roll for damage twice!")    
    damage_roll = random.randint(1,8) + random.randint(1,8) + game_info["player_damage"]
    print(f"You did {damage_roll} damage.")
elif hit_roll == 1:
    print("You rolled a critical failure! Now the monster gets to attack you!")
    damage_roll = random.randint(1,12) + game_info["monster_damage"]
    game_info["player_hp"] -= (damage_roll - game_info["player_defense"])
    print(f"The monster rolled {damage_roll}, your hp is now {game_info["player_hp"]}")
elif hit_roll >= 12:
    print("You hit! Roll for damage!")
    if damage_roll > game_info["monster_defense"]:
        print(f"You did {damage_roll-game_info["monster_defense"]}.")
        game_info["monster_hp"] -= (damage_roll-game_info["monster_defense"])
    else:
        print("You did no damage.")
else:
    print("You missed.")

print("Your turn is over")

if game_info["monster_hp"] > 0:
    attack_roll = random.randint(1,20) + game_info["monster_attack"]
