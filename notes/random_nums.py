#DL 1st, random numbers notes
import random

#generate stat options
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

# Set Stats
strength = int(input("Which stat do you want as your strength: \n")) +2

print(f"This is a random number from 0 - 1: {random.random()}")
print(f"This is a random number from 1 - 20: {random.randint(1,20)}")
