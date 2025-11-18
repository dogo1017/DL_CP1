#DL 1st, flex calc

def sum_numbers(*nums):
    sum = 0
    for num in nums:
        sum += num
    return(sum)

print("Welcome to the Flexible Calculator!")

print("Available operations: sum, average, max, min, product")

val_ops = ["sum", "average", "max", "min", "product"]

while True:
    nums = []
    operation = input("Which operation would you like to preform? ").lower().strip()
    if operation not in val_ops:
        print("Please type a valid input")
        continue
    print("Enter numbers (type 'done' when finished):\n")
    num_inp = True
    while num_inp == True:
        new_num = input("Number: ")
        if new_num.isdigit() == True:
            nums.append(int(new_num))
            continue
        if new_num == "done":
            num_inp = False
        else:
            print("please type a valid number")
    print(f"Calculating {operation} of: {nums[1]}", end = '')
        for num in nums:
        print(f", [num]")
    if operation == "sum":
        print(sum_numbers(*nums))