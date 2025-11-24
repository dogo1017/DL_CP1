# display_factorial(number)
def display_factorial(number):
    # While True
    while True:
        # try isdigit
        try:
            number.isdigit()     
        # except
        except:
            continue
        return True
            

# user input for positive full number
while True:
    number = input("Please input a positive whole number")
# stupid proof to make sure it is a whole number
    if display_factorial(number) == True and int(number) > 0:
        number = int(number)
        break
    else:
        print("Please type a valid input")
        continue
# factorial variables is set to 1 for the number in the number
for i in range(number):
    factorial = 1 
# number * factorial = factorial
    factorial = number * factorial
# number - 1 = number
    number = number - 1
# display factorial
print(factorial)

