#DL 1st, functions notes

def add(x,y):
    print(f"{x} + {y} = {x+y}")
    return x+y

add(5,5)
add(10,12)
add(3,9)



health = 100
monster_health = 100
player_health = 100

def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
monster_health, player_health = damage(10, "player")
print(f"Monster Health: {monster_health}")
print(f"Player Health: {player_health}")
def add(x,y):
    return x+y
def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]
    return initials

total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x=0
while x < add(3,9):
    print("Duck")
    x += 1
print("Goose!")
print(initials("Douglas London"))