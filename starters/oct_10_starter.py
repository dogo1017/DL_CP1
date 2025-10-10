#DL 1st, oct 10 starter
import random


board = []
resume = True

first_turn = random.randint(0,1)

while resume == True:
    
    if first_turn == False: 
        board == board.replace(computer, "X")
        first_turn == True
    else: 
        pass
    
    computer = random.randint(1,9)
    player = int(input("What part of the board? (1-9)\n"))
    if player not in board:
        board.append(player)
    else:
        print("Please type a different number")

    
    if 1 in board and 2 in board and 3 in board:
        print("You Won")
    if 4 in board and 5 in board and 6 in board:
        print("You Won")
    if 7 in board and 8 in board and 9 in board:
        print("You Won")
        
    if 1 in board and 5 in board and 9 in board:
        print("You Won")
    if 7 in board and 5 in board and 3 in board:
        print("You Won")

    if 1 in board and 4 in board and 7 in board:
        print("You Won")
    if 2 in board and 5 in board and 8 in board:
        print("You Won")
    if 3 in board and 6 in board and 9 in board:
        print("You Won")

    resume = input("Do you want to continue? (Y/N)\n").strip().lower()
    if resume == "y":
        resume = True      
    if resume == "n": 
        resume = False