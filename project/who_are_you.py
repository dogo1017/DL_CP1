# DL 1st, who are you

user_data = {}

while True:
    name = input("What is your name? \n")
    if name in user_data:
        print(user_data['age'])
        print("Hello! You have already used this code. You are {age} and like the color {color}")
    else:
        age = input("What is your age? \n")
        color = input("What is your favorite color? \n")
        user_data[name] = {'age': age, 'color': color}
        print(name, "is", age, "years old and likes the color", color)