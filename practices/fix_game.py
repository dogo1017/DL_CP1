#DL 1st, fix the game practice

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        
        if attempts >= max_attempts: # the code is not used after this, logic, it doesnt end the game when max attempts are reached.
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")# this line came after the guess, logic, it let the user guess again even if out of attempts
            game_over = True
            break
        guess = int(input("Enter your guess: ")) # guess was a string, logic, it tried to compare a string and int
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
        # There was an unnecesary continue here, logic, It made the code more confusing but didnt actually effect the code
    print("Game Over. Thanks for playing!")
start_game()