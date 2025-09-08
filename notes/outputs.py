#DL 1st, output formatting notes

name = "Eric"
age = 999999999999999999999999999999999999999999999999999999999999999
money = 25.1
percent = .74

print("Hello {}, you are {}. That is so old! You have ${:.2f} you must be rich!".format(name, age, money))

print(f"Hello {name}, you are {age:.2f}. That is so old! You have ${money:.2f} you must be rich! Random percent is {percent:.1f}%.")
