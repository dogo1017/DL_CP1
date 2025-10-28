# DL 1st, combat practice
import random
import time

def attack_turn(attacker_name, target_name, attacker_damage_low, attacker_damage_high, target_defense, luck, target_health, is_player):

    if is_player:
        target = input("Attack where? head or body? ").lower()
        if target == "head":
            hit_chance = 40 + luck * 2
            dmg = random.randint(attacker_damage_low + 3, attacker_damage_high + 5)
        else:
            hit_chance = 80 + luck * 2
            dmg = random.randint(attacker_damage_low, attacker_damage_high)
    else:
        hit_chance = 75
        dmg = random.randint(attacker_damage_low, attacker_damage_high)

    if random.randint(1, 100) <= hit_chance:
        actual_dmg = max(0, dmg - target_defense)
        target_health -= actual_dmg
        if is_player:
            print(f"You hit the {target_name} for {actual_dmg} damage!")
        else:
            print(f"The {attacker_name} hits you for {actual_dmg} damage!")
    else:
        if is_player:
            print("You missed!")
        else:
            print(f"The {attacker_name} missed!")

    return target_health

def ensure_damage_valid(low, high):
    if low > high:
        low, high = high, low
    return low, high

def stat_change(available_points, stat_value, stat_name):
    while True:
        try:
            point_change = int(input(f"How many points would you like to add to {stat_name}? (1-{available_points}, or 0 to cancel): "))
            if 0 <= point_change <= available_points:
                stat_value += point_change
                return stat_value, point_change
            else:
                print(f"Please input a number from 0 to {available_points}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

user_attack = 1
user_defense = 1
user_health = 1
user_damage_low = 1
user_damage_high = 1
user_luck = 1


low_monsters = [
    {"name": "Slime", "description": "A small blob of goo that jiggles menacingly.", "health": 20, "attack": 3, "defense": 1, "damage_range": (2, 4)},
    {"name": "Rat", "description": "A filthy rat with glowing red eyes.", "health": 18, "attack": 4, "defense": 1, "damage_range": (2, 5)},
    {"name": "Bat", "description": "A screeching cave bat that darts through the air.", "health": 15, "attack": 3, "defense": 1, "damage_range": (1, 4)},
    {"name": "Spider", "description": "A large spider that lunges at you.", "health": 22, "attack": 4, "defense": 1, "damage_range": (2, 5)},
    {"name": "Goblin", "description": "A mischievous goblin with a rusty dagger.", "health": 25, "attack": 5, "defense": 2, "damage_range": (3, 6)},
    {"name": "Tiny Lizard", "description": "A quick reptile that tries to bite your ankle.", "health": 19, "attack": 3, "defense": 1, "damage_range": (2, 4)},
    {"name": "Wormling", "description": "A wriggling worm from the damp soil.", "health": 16, "attack": 2, "defense": 1, "damage_range": (1, 3)},
    {"name": "Kobold", "description": "A cowardly creature that attacks in short bursts.", "health": 24, "attack": 5, "defense": 2, "damage_range": (3, 5)},
    {"name": "Beetle", "description": "A hard-shelled insect that charges straight at you.", "health": 23, "attack": 4, "defense": 3, "damage_range": (2, 5)},
    {"name": "Mushling", "description": "A walking mushroom that puffs out spores.", "health": 24, "attack": 4, "defense": 2, "damage_range": (3, 5)},
    {"name": "Dust Imp", "description": "A small imp that throws clumps of dirt at you.", "health": 21, "attack": 3, "defense": 1, "damage_range": (2, 4)},
    {"name": "Cave Crab", "description": "A rock-shelled crab that snaps with its claws.", "health": 28, "attack": 4, "defense": 3, "damage_range": (3, 6)},
    {"name": "Torch Spirit", "description": "A faint flicker of flame given weak form.", "health": 18, "attack": 4, "defense": 1, "damage_range": (2, 5)},
    {"name": "Mudling", "description": "A muddy creature that slaps at you with sticky arms.", "health": 26, "attack": 3, "defense": 2, "damage_range": (3, 5)},
    {"name": "Mini Harpy", "description": "A screeching bird-woman that dive-bombs you.", "health": 27, "attack": 5, "defense": 2, "damage_range": (3, 6)}
]
mid_monsters = [
    {"name": "Skeleton", "description": "A reanimated pile of bones with a cracked sword.", "health": 35, "attack": 6, "defense": 3, "damage_range": (4, 8)},
    {"name": "Zombie", "description": "A decaying corpse that moves slowly but hits hard.", "health": 40, "attack": 7, "defense": 3, "damage_range": (5, 8)},
    {"name": "Bandit", "description": "A sneaky thief who attacks from the shadows.", "health": 38, "attack": 8, "defense": 2, "damage_range": (5, 9)},
    {"name": "Wolf", "description": "A wild wolf with glowing yellow eyes.", "health": 34, "attack": 7, "defense": 3, "damage_range": (5, 9)},
    {"name": "Dark Mage", "description": "A shadowy sorcerer muttering curses under its breath.", "health": 42, "attack": 9, "defense": 3, "damage_range": (6, 10)},
    {"name": "Stone Golem", "description": "A massive creature made of rock and dust.", "health": 50, "attack": 8, "defense": 5, "damage_range": (6, 10)},
    {"name": "Lizardman", "description": "A reptilian humanoid wielding a spear.", "health": 44, "attack": 8, "defense": 4, "damage_range": (5, 9)},
    {"name": "Ghoul", "description": "A corpse-eater with long claws and sharp teeth.", "health": 38, "attack": 9, "defense": 3, "damage_range": (6, 9)},
    {"name": "Fire Wisp", "description": "A floating flame that launches small bursts of fire.", "health": 33, "attack": 9, "defense": 2, "damage_range": (6, 10)},
    {"name": "Iron Guard", "description": "An enchanted suit of armor that moves on its own.", "health": 48, "attack": 8, "defense": 6, "damage_range": (5, 9)},
    {"name": "Orc Scout", "description": "A bulky warrior with crude iron gear.", "health": 45, "attack": 9, "defense": 4, "damage_range": (6, 10)},
    {"name": "Bog Witch", "description": "A hag who mutters in ancient tongues, cursing her foes.", "health": 36, "attack": 10, "defense": 3, "damage_range": (7, 10)},
    {"name": "Shadow Hound", "description": "A beast formed of mist and darkness.", "health": 40, "attack": 10, "defense": 3, "damage_range": (7, 11)},
    {"name": "Harpy", "description": "A shrieking bird-like woman that dives with sharp talons.", "health": 42, "attack": 9, "defense": 3, "damage_range": (6, 10)},
    {"name": "Cursed Knight", "description": "A fallen warrior bound to the dungeon’s power.", "health": 52, "attack": 10, "defense": 5, "damage_range": (7, 11)}
]

high_monsters = [
    {"name": "Orc Warrior", "description": "A hulking orc with heavy armor and a massive axe.", "health": 55, "attack": 10, "defense": 5, "damage_range": (7, 12)},
    {"name": "Wraith", "description": "A ghostly figure that drains your life force.", "health": 48, "attack": 11, "defense": 4, "damage_range": (8, 13)},
    {"name": "Fire Elemental", "description": "A being made of pure flame.", "health": 60, "attack": 12, "defense": 4, "damage_range": (9, 14)},
    {"name": "Minotaur", "description": "A beast with the body of a man and head of a bull.", "health": 65, "attack": 13, "defense": 6, "damage_range": (9, 15)},
    {"name": "Necromancer", "description": "A master of dark magic who summons spirits.", "health": 58, "attack": 12, "defense": 5, "damage_range": (9, 14)},
    {"name": "Fallen Knight", "description": "A once-noble warrior consumed by darkness.", "health": 70, "attack": 13, "defense": 7, "damage_range": (10, 15)},
    {"name": "Thunder Spirit", "description": "A storm made flesh, crackling with energy.", "health": 60, "attack": 14, "defense": 5, "damage_range": (10, 15)},
    {"name": "Vampire", "description": "A dark noble who drains your vitality with each strike.", "health": 64, "attack": 13, "defense": 6, "damage_range": (9, 15)},
    {"name": "Frost Giant", "description": "A towering giant that freezes the air around it.", "health": 80, "attack": 14, "defense": 7, "damage_range": (10, 16)},
    {"name": "Serpent Queen", "description": "A snake-bodied ruler who commands venom and charm.", "health": 70, "attack": 15, "defense": 6, "damage_range": (10, 16)},
    {"name": "Shadow Assassin", "description": "A blade-wielding killer that moves faster than sight.", "health": 55, "attack": 16, "defense": 5, "damage_range": (9, 15)},
    {"name": "Demon Soldier", "description": "A crimson-skinned warrior with molten eyes.", "health": 68, "attack": 15, "defense": 7, "damage_range": (10, 17)},
    {"name": "Lava Beast", "description": "A molten creature whose punches erupt fire.", "health": 78, "attack": 15, "defense": 8, "damage_range": (10, 17)},
    {"name": "Abyssal Harbinger", "description": "A creature from another realm, dripping shadows.", "health": 85, "attack": 16, "defense": 8, "damage_range": (11, 18)},
    {"name": "Ancient Guardian", "description": "A relic defender of the dungeon’s final chamber.", "health": 90, "attack": 17, "defense": 9, "damage_range": (11, 18)}
]

low_bosses = [
    {"name": "Slime King", "description": "A huge, wobbling mass of slime wearing a crown.", "health": 45, "attack": 6, "defense": 3, "damage_range": (4, 7)},
    {"name": "Goblin Chief", "description": "Leader of the goblins, carrying a jagged club.", "health": 55, "attack": 7, "defense": 3, "damage_range": (5, 8)}
]

mid_bosses = [
    {"name": "Bone Lord", "description": "A giant skeleton with glowing eyes and a greatsword.", "health": 70, "attack": 10, "defense": 6, "damage_range": (7, 11)},
    {"name": "Cursed Champion", "description": "An armored knight whose soul burns with hatred.", "health": 80, "attack": 11, "defense": 7, "damage_range": (8, 12)}
]

high_bosses = [
    {"name": "Dragon Lord", "description": "A massive dragon whose roar shakes the dungeon walls.", "health": 120, "attack": 16, "defense": 8, "damage_range": (12, 18)},
    {"name": "Void Serpent", "description": "A colossal serpent from the dark void itself.", "health": 140, "attack": 17, "defense": 9, "damage_range": (13, 19)}
]

final_boss = [
    {"name": "Eternal Demon King", "description": "The source of all evil in the dungeon. Its aura burns your soul.", "health": 200, "attack": 20, "defense": 10, "damage_range": (15, 22)}
]


name = input("Hello, What is your name?\n")
while True:
    difficulty = input("What difficulty would you like to play?\n1) easy\n2) medium\n3) hard\n4) dungeon(May still contain bugs)\n")
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

if difficulty == "4":
    print(f"Welcome {name}, you will be able to chose the stats of your player by distributing more points to your health, attack, damage, luck, and defense levels for every floor you beat.")
else:
    print(f"Welcome {name}, you will be able to chose the stats of your player by distributing {points} to your health, attack, damage, luck, and defense levels")

while points > 0:
    stat_to_change = input(
        f"Which stat would you like to add points to?\n"
        f"Points left: {points}\n"
        f"health: {user_health}\n"
        f"attack: {user_attack}\n"
        f"damage: {user_damage_low}-{user_damage_high}\n"
        f"luck: {user_luck}\n"
        f"defense: {user_defense}\n"
    ).lower()

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
        points -= points_spent

    elif stat_to_change == 'damage':
        print(f"Your minimum damage is linked to your luck stat ({user_luck}).")
        user_damage_high, points_spent = stat_change(points, user_damage_high, 'max damage')
        points -= points_spent

    else:
        print("Please enter 'health', 'attack', 'damage', 'luck', or 'defense'.")
        continue

    if user_damage_low < user_luck:
        user_damage_low = user_luck
    if user_damage_low > user_damage_high:
        user_damage_low = user_damage_high

score = 0
floor = 1
playing = True

print("\nYou descend into the dungeon...")

while playing:
    print(f"\n--- Floor {floor} ---")

    if floor == 1:
        dungeon_level = low_monsters
        boss = random.choice(low_bosses)
    elif floor == 2:
        dungeon_level = mid_monsters
        boss = random.choice(mid_bosses)
    elif floor == 3:
        dungeon_level = high_monsters
        boss = random.choice(high_bosses)
    else:
        dungeon_level = []
        boss = final_boss[0]

    user_damage_low, user_damage_high = ensure_damage_valid(user_damage_low, user_damage_high)

    for monster in dungeon_level:
        print(f"\nA {monster['name']} appears! {monster['description']}")
        monster_health = monster['health']


        first_turn = random.choice([True, False])
        if first_turn:
            print("You move first!")
        else:
            print(f"The {monster['name']} moves first!")


        while monster_health > 0 and user_health > 0:
            print(f"\nYour Health: {user_health} | {monster['name']} Health: {monster_health}")
            if first_turn: 
                print("\nWhat would you like to do?")
                print("1) Attack Head/Body")
                print("2) Block (Gain +5 temporary DEF this turn)")
                print("3) Rest (Gain +5 Health)")
                print("4) Run (Attempt to escape)")
                
                move = input("Choose action (1-4): ").lower()
                
                if move == "1":
                    monster_health = attack_turn(
                        name, monster['name'],
                        user_damage_low, user_damage_high,
                        monster['defense'], user_luck,
                        monster_health, True)
                    
                elif move == "2":
                    temp_defense = user_defense + 5
                    print(f"You raise your guard, your defense is temporarily {temp_defense}.")
                    
                    monster['temp_def'] = 5
                    
                elif move == "3":
                    user_health = min(user_health + 5, user_health + 5)
                    print(f"You take a moment to rest and regain 5 health.")
                    
                elif move == "4":
                    if random.randint(1, 100) <= 60:
                        print(f"You escaped successfully from the {monster['name']}!")
                        playing = False
                        break 
                    else:
                        print(f"You failed to run away from the {monster['name']}!")
                        
                else:
                    print("Invalid action, losing your turn.")

            if playing == False: 
                break 

            if monster_health > 0 and not first_turn: 
                
                temp_def_bonus = monster.pop('temp_def', 0) 

                user_health = attack_turn(
                    monster['name'], name,
                    monster['damage_range'][0], monster['damage_range'][1],
                    user_defense + temp_def_bonus, 0,
                    user_health, False)

            first_turn = not first_turn

            if user_health <= 0:
                print("\nYou have been defeated...")
                playing = False
                break

        if playing == False or user_health <= 0:
            break

        if monster_health <= 0:
            print(f"You defeated the {monster['name']}!")
            score += 10 + monster['attack']
            if random.randint(1, 100) <= 30:
                loot_type = random.choice(["attack", "defense", "health", "luck"])
                print(f"The {monster['name']} dropped a {loot_type} orb!")
                if loot_type == "attack":
                    user_attack += 1
                elif loot_type == "defense":
                    user_defense += 1
                elif loot_type == "health":
                    user_health += 10
                elif loot_type == "luck":
                    user_luck += 1

    if playing == False:
        break 

    print(f"\n--- Boss Battle! {boss['name']} appears! ---")
    boss_health = boss['health']

    while boss_health > 0 and user_health > 0:
        print(f"\nYour Health: {user_health} | {boss['name']} Health: {boss_health}")
        
        move = input("Choose action: attack / run: ").lower() 

        if move == "attack":
            boss_health = attack_turn(name, boss['name'], user_damage_low, user_damage_high, boss['defense'], user_luck, boss_health, True)
        elif move == "run":
            print("You cannot run from a boss!")

        if boss_health > 0:
            user_health = attack_turn(boss['name'], name, boss['damage_range'][0], boss['damage_range'][1], user_defense, 0, user_health, False)

    if user_health <= 0:
        print("\nYou were slain by the boss...")
        break

    print(f"\nYou defeated {boss['name']}! Floor {floor} cleared!")
    score += 100 + boss['attack']

    if random.randint(1, 100) <= 50:
        print("You obtained a boss relic! All stats +2!")
        user_attack += 2
        user_defense += 2
        user_luck += 2
        user_damage_high += 2

    print("\nYou feel your power growing. You may distribute 10 points.")
    bonus_points = 10
    while bonus_points > 0:
        stat_to_change = input(f"Points left: {bonus_points}\nhealth({user_health}) attack({user_attack}) defense({user_defense}) luck({user_luck})\nChoose stat: ").lower()
        if stat_to_change == "health":
            user_health += 5
            bonus_points -= 1
        elif stat_to_change == "attack":
            user_attack += 1
            bonus_points -= 1
        elif stat_to_change == "defense":
            user_defense += 1
            bonus_points -= 1
        elif stat_to_change == "luck":
            user_luck += 1
            bonus_points -= 1
        else:
            print("Invalid stat.")

    cont = input("Do you continue to the next floor or leave? (continue/leave): ").lower()
    if cont == "leave":
        if random.randint(1, 100) <= 10:
            print("As you leave, a monster ambushes you!")
            user_health -= 10
            if user_health <= 0:
                print("You were slain during your escape...")
                break
        else:
            print("You safely leave the dungeon.")
            break

    floor += 1

print(f"\nGame Over. Final Score: {score}")