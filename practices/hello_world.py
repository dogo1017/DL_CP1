# DL, 1st Hello World Python
returning_users = ["Bob", "Joe", "Tim", "Alan", "Shrek"]
name = input("What is your name: ")
if name == "Douglas":
     print("Hello awesome person")
elif name == "Jacob":
     print("Oh... It's you")
elif name == "Ms. LaRose":
     print("please give me an A", name)
elif name in returning_users:
     print("Welcome back", name)
else:
     print("Hello", name, "Welcome to my code")
