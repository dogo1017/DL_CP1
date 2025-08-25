# DL 1st, who are you
import os
user_data = {}

while True:
    rerun = "No"
    name = input("What is your name? \n")
    if name in user_data:
        print("Hello! You have already used this code. You are", user_data[name]['age'], "and like the color", user_data[name]['color'])
        rerun = input("\nWould you like to add or check information (Yes/No): ")
        if rerun == "Yes" or "yes" or "y" or "Y":
            os.system('cls')
            continue
        else:
            exit()
    else:
        age = input("What is your age? \n")
        color = input("What is your favorite color? \n")
        user_data[name] = {'age': age, 'color': color}
        print(name, "is", age, "years old and likes the color", color)
        rerun = input("\nWould you like to add or check information (Yes/No): ")
        if rerun == "Yes" or rerun == "yes" or rerun == "y" or rerun == "Y":
            os.system('cls')
            continue
        else:
            exit()
