#DL 1st, flex calc practice



# Greet the user and show available operations
print("Welcome to the Flexible Calculator!")
print("Available operations: sum, average, max, min, product")

# List of valid operations
val_ops = ["sum", "average", "max", "min", "product"]
active = True  # Keep calculator running until user quits

# Function to add numbers
def sum_nums(*nums):
    total = 0  # Start with zero
    for num in nums:  # Go through all numbers
        total += num  # Add each number to total
    return total  # Return the sum

# Function to calculate average
def avg(*nums):
    return sum_nums(*nums) / len(nums)  # Divide sum by number of numbers

# Function to find maximum
def max_num(*nums):
    return max(nums)  # Return the largest number

# Function to find minimum
def min_num(*nums):
    return min(nums)  # Return the smallest number

# Function to multiply numbers
def product(*nums):
    total = 1  # Start with 1
    for num in nums:  # Go through all numbers
        total *= num  # Multiply total by each number
    return total  # Return the product

# Function to format result nicely
def format_result(res):
    if res == int(res):  # If result is whole number
        return int(res)  # Show as integer
    return res  # Otherwise show as float

# Main loop for calculator
while active:  # Repeat until user quits
    nums = []  # List to store numbers
    # Ask user which operation to perform
    operation = input("Which operation would you like to perform? ").lower().strip()
    if operation not in val_ops:  # Check if operation is valid
        print("Please type a valid operation")
        continue  # Go back to asking operation

    # Ask user to enter numbers
    print("Enter numbers (type 'done' when finished):")
    while True:  # Repeat until "done" is typed
        new_num = input("Number: ")
        if new_num.lower() == "done":  # Stop asking numbers
            break
        try:  
            nums.append(float(new_num))  # Convert input to number
        except ValueError:  # If input is not a number
            print("Please type a valid number")
            continue

    if not nums:  # If user entered no numbers
        print("No numbers entered. Try again.")
        continue

    # Show calculation being performed
    print(f"Calculating {operation} of: {', '.join(str(format_result(n)) for n in nums)}")

    # Perform the operation and store result
    if operation == "sum":
        res = sum_nums(*nums)
    elif operation == "average":
        res = avg(*nums)
    elif operation == "max":
        res = max_num(*nums)
    elif operation == "min":
        res = min_num(*nums)
    elif operation == "product":
        res = product(*nums)

    # Show the result
    print(f"Result = {format_result(res)}")

    # Ask if user wants to do another calculation
    while True:
        end = input("Do you want to do another calculation (y,n)? ").strip().lower()
        if end == "y":  # Continue loop
            break
        elif end == "n":  # Stop loop
            active = False
            print("Thanks for using my calculator! :)")
            break
        else:
            print("Please type a valid answer")  # Invalid input