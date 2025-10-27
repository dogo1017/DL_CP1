#DL 1st, combat practice
import random
import time

#def dis_message(message,get_input):
#    for char in message:
#        time.sleep(0.09)
#        print(char, end="")
#    if get_input == True:
#        get_input = input()
#        return get_input
    
#def dis_options(message,get_input):
#    message_parts = message.split('\n')
#    print(message_parts)

def stat_change(available_points, stat_value, stat_name):
    while True:
         point_change = int(input(f"How many points would you like to add to {stat_name}? (1-{available_points}, or 0 to cancel): "))
         if 0 <= point_change <= available_points:
             stat_value += point_change
             return stat_value, point_change
         else:
             print(f"Please input a number from 0 to {available_points}.")

user_attack = 1
user_defense = 1
user_health = 1
user_damage_low = 1
user_damage_high = 1
user_luck = 1


low_monsters = [
    {'name': 'Giant Rat', 'description': 'A common sewer pest, grown to a formidable size.', 'health': 15, 'attack': 5, 'defense': 2, 'damage_range': (1, 4)},
    {'name': 'Kobold', 'description': 'Small, reptilian humanoids known for their cunning traps.', 'health': 10, 'attack': 6, 'defense': 3, 'damage_range': (2, 5)},
    {'name': 'Forest Slime', 'description': 'A slow-moving, gelatinous creature that absorbs smaller prey.', 'health': 25, 'attack': 3, 'defense': 1, 'damage_range': (1, 2)},
    {'name': 'Goblin Shaman', 'description': 'A magically-inclined goblin who can cast minor curses.', 'health': 30, 'attack': 12, 'defense': 7, 'damage_range': (5, 10)},
    {'name': 'Giant Spider', 'description': 'A venomous spider that can quickly ensnare its prey.', 'health': 20, 'attack': 8, 'defense': 4, 'damage_range': (2, 6)},
    {'name': 'Zombie', 'description': 'A slow but relentless undead foe, shambling forward with a groan.', 'health': 35, 'attack': 6, 'defense': 5, 'damage_range': (3, 7)},
    {'name': 'Animated Armor', 'description': 'An empty suit of armor, given a semblance of life by a malevolent spirit.', 'health': 40, 'attack': 10, 'defense': 8, 'damage_range': (4, 8)}
]
mid_monsters = [
    {'name': 'Stone Golem', 'description': 'An animated statue, slow but incredibly durable.', 'health': 120, 'attack': 15, 'defense': 20, 'damage_range': (10, 15)},
    {'name': 'Giant Scorpion', 'description': 'A massive arachnid with a venomous stinger.', 'health': 60, 'attack': 18, 'defense': 10, 'damage_range': (8, 12)},
    {'name': 'Ogre', 'description': 'A brutish and powerful humanoid with a massive club.', 'health': 150, 'attack': 20, 'defense': 15, 'damage_range': (12, 18)},
    {'name': 'Wraith', 'description': 'A spectral undead creature that can drain the life force of its enemies.', 'health': 80, 'attack': 25, 'defense': 12, 'damage_range': (15, 25)},
    {'name': 'Basilisk', 'description': 'A reptilian monster with a petrifying gaze.', 'health': 90, 'attack': 22, 'defense': 18, 'damage_range': (10, 20)},
    {'name': 'Wyvern', 'description': 'A smaller, more aggressive cousin of the dragon, with a venomous stinger on its tail.', 'health': 100, 'attack': 28, 'defense': 16, 'damage_range': (15, 22)}
]
high_monsters = [
    {'name': 'Shadow Wyrm', 'description': 'A fearsome dragon that controls the darkness and manipulates shadows.', 'health': 500, 'attack': 40, 'defense': 35, 'damage_range': (30, 50)},
    {'name': 'Lich Lord', 'description': 'An undead sorcerer with mastery over the dark arts.', 'health': 300, 'attack': 50, 'defense': 25, 'damage_range': (25, 45)},
    {'name': 'Ancient Dragon', 'description': 'A colossal and ancient dragon of immense power and wisdom.', 'health': 800, 'attack': 60, 'defense': 45, 'damage_range': (40, 70)},
    {'name': 'Demon Prince', 'description': 'A tyrannical lord of the underworld, with formidable strength and dark magic.', 'health': 600, 'attack': 55, 'defense': 30, 'damage_range': (35, 60)},
    {'name': 'Elemental Lord', 'description': 'A primordial being of pure elemental energy, commanding immense destructive power.', 'health': 450, 'attack': 45, 'defense': 40, 'damage_range': (35, 55)}
]



name = input("Hello, What is your name?\n")
while True:
    difficulty = input("What difficulty would you like to play?\n1) easy\n2) medium\n3) hard\n4) dungeon\n")
    if difficulty == "1":
        points = random.randint(25,35)
        break
    elif difficulty == "2":
        points = random.randint(130,150)
        break
    elif difficulty == "3":
        points = random.randint(260,340)
        break
    elif difficulty == "4":
        points = random.randint(20,30)
        break
    else:
        print("Please write a number from 1-4")

if difficulty == 4:
    print(f"Welcome {name}, you will be able to chose the stats of your player by distributing more points to your health, attack, damage, luck, and defense levels for every floor you beat.")
else:
    print(f"Welcome {name}, you will be able to chose the stats of your player by distributing {points} to your health, attack, damage, luck, and defense levels")

while points > 0:
    stat_to_change = input(f"Which stat would you like to add points to?\nPoints left: {points}\nhealth: {user_health}\nattack: {user_attack}\ndamage: {user_damage_low}-{user_damage_high}\nluck: {user_luck}\ndefense: {user_defense}\n")

    if stat_to_change == 'health':
        user_health, points_spent = stat_change(points, user_health, 'health')
        points -= points_spent
    elif stat_to_change == 'attack':
        user_attack, points_spent = stat_change(points, user_attack, 'attack')
        points -= points_spent
    elif stat_to_change == 'defense':
        user_defense, points_spent = stat_change(points, user_defense, 'defense')
        points -= points_spent
    elif stat_to_change == 'luck':
        user_luck, points_spent = stat_change(points, user_luck, 'luck')
        user_damage_low = user_luck
        points -= points_spent
    elif stat_to_change == 'damage':
        print(f"Your minimum damage is linked to your luck stat ({user_luck}).")
        user_damage_high, points_spent = stat_change(points, user_damage_high, 'max damage')
        points -= points_spent
    else:
        print("Please enter 'health', 'attack', 'damage', 'luck', or 'defense'.")

while True:

    if difficulty == "1":
        current_monster = random.choice(low_monsters)
        monster_health =  1
        while True:
            print(low_monsters[1].replace("'", "").replace(",", "").replace(" ", "\n"))
