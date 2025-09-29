#DL 1st, lists notes
import random

sibs = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jefferson", "Jake"]

print(sibs[5])
print(f"The list is {len(sibs)} people long")
print(sibs)
sibs[0] = "Eric"
sibs[6:-1] = ["Xavier", "Hailey"]
sibs.pop()
sibs.pop(3)
sibs.remove("Andrew")
#sibs.clear()
#sbs.append("Andrew")
sibs.insert(2, "Andrew")
sibs.extend(["Joseph", "Israel", "Zee"])
print(sibs)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]
        ]

fruit = ("Apple", "Orange", "Pineapple") #tuple ordered, not changeable


veggies = {"Spinach", "Kale", "Broccoli", "Carrot"} #set unordered, changeable"
