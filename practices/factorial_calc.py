#DL 1st, factorial calc practice

# display_factorial(number)
def display_factorial(number_str):
    try:
        number = int(number_str)
        if number > 0:
            return True
        else:
            return False
    except ValueError:
        return False

# stupid proof to make sure it is a whole number
while True:
    number_input = input("Please input a positive whole number: ")
    # stupid proof to make sure it is a whole number
    if display_factorial(number_input):
        number = int(number_input)
        break
    else:
        print("Please type a valid input")
        continue
# factorial variables is set to 1 for the number in the number
# factorial variables
factorial = 1
# Calculate factorial
for i in range(1, number + 1): # Iterate from 1 up to and including 'number'
    factorial = factorial * i
# display factorial
print(factorial)
