#DL 1st, while loops
import time
import random
for num in range(1,21):
    print(num)

num = 1 
while num <= 20:
    print(num)
    num += 1
else:
    print("The condition was met")

# infinite loop
num = 1

while num <= 20:
    print(num)
    num += 1 #Prevents an infinite loop

    goose = random.randint(1,20)
    count = 0

while True:
    count += 1
    if count == goose:
        break
    else:
        print("duck")
else:
    print("GOOSE!")