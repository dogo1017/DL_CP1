#DL 1st, for loops notes
import time


nums = [4,654,136,84,651,86,42,1,564,3,4894]
health = 15

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number")
    else:
        print(num)
        print("The loop is over")

for num in range(1,health,2):
    print(num)
    

for num in range(20,0):
	print(num)

message = "Hello"

for char in message:
     print(char)
     time.sleep(0.5)