#DL 1st, combat practice
attack = 0
defense = 0
health = 0
damage = 0
user_stats = {"attack": attack, "defense": defense, "health": health, "damage": damage}

low_monsters = [{"name": "Giant Rat", "description": "A common sewer pest, grown to a formidable size.","health": 15,"attack": 5,"defense": 2,"damage_range": (1, 4),},    {"name": "Kobold","description": "Small, reptilian humanoids known for their cunning traps.",    "health": 10,    "attack": 6,    "defense": 3,    "damage_range": (2, 5),},    {"name": "Forest Slime","description": "A slow-moving, gelatinous creature that absorbs smaller prey.",    "health": 25,    "attack": 3,    "defense": 1,    "damage_range": (1, 2),},    {"name": "Goblin Shaman","description": "A magically-inclined goblin who can cast minor curses.",    "health": 30,    "attack": 12,    "defense": 7,    "damage_range": (5, 10),}]    
                
mid_monsters = [{"name": "Stone Golem","description": "An animated statue, slow but incredibly durable.",    "health": 120,    "attack": 15,    "defense": 20,    "damage_range": (10, 15),},    {"name": "Giant Scorpion","description": "A massive arachnid with a venomous stinger.",    "health": 60,    "attack": 18,    "defense": 10,    "damage_range": (8, 12)}]    
                
high_monsters = [{"name": "Shadow Wyrm","description": "A fearsome dragon that controls the darkness and manipulates shadows.",    "health": 500,    "attack": 40,    "defense": 35,    "damage_range": (30, 50),},    {"name": "Lich Lord","description": "An undead sorcerer with mastery over the dark arts.",    "health": 300,    "attack": 50,    "defense": 25,    "damage_range": (25, 45),}]


name = input("What is your name?")
difficulty = input("What difficulty would you like to play?\n1) Easy\n2) medium\n3) hard")
print(f"Welcome {name}, you will be able to chose the stats of your player by distributing ")