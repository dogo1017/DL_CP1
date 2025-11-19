#DL 1st, flex calc

def sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return(sum)


print("Welcome to the Flexible Calculator!")

print("Available operations: sum, avg, max, min, product")

val_ops = ["sum", "avg", "max", "min", "product"]

active = True

while active == True:
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
            continue
        print(f"Calculating {operation} of:", end = '')
        iter = 0
        for num in nums:
            iter += 1
            if iter > 0:
                print(f", {num}", end = '')
        print("")
    if operation == "sum":
        print(f"Result =", sum(*nums))
    if operation == "average":
        print(f"Result =", sum(*nums))
    if operation == "max":
        print(f"Result =", sum(*nums))
    if operation == "min":
        print(f"Result =", sum(*nums))
    if operation == "product":
        print(f"Result =", sum(*nums))
    

    while True:
        continue = input("Do you want to do another calculation(y,n) ").strip().lower()
        if continue == "y":
            break
        if continue == "n":
            active = "n"
        else:
            print("please type a valid answer")