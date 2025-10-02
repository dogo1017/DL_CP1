#DL 1st, rock paper scissors
import random

while True:
    bot_guess = random.randint(1,3)
    player_guess = input("rock, paper, or scissors: ").lower()
    if bot_guess == 1:
        if player_guess == "rock":
    	    print("Tie, try again")
        elif player_guess == "scissors":
            print("You lost")
        elif player_guess == "paper":
            print("You won")
        else:
            print("please type a valid input")
    elif bot_guess == 2:
	    if player_guess == "paper":
            print("Tie, try again")
        elif player_guess == "rock":
            print("You lost")
	    elif player_guess == "paper":
	    	print("You won")
	    else:
	    	print("please type a valid input")
