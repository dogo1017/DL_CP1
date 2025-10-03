#DL 1st, rock paper scissors
import random

while True:
    bot_guess = random.randint(1,3)
    player_guess = input("Do you chose Rock, Paper, or Scissors?\n").strip().lower()
    if player_guess == "rock":
        player_guess = 1
    elif player_guess == "paper":
        player_guess = 2
    elif player_guess == "scissors":
        player_guess = 3
    else:
        print("please type a valid input")
        continue

    if bot_guess == 1:
        if player_guess == bot_guess:
            print("You tied")
        elif player_guess == 2:
            print("You won")
        else:
            print("You lost")