#DL 1st, basic calculator
types = ["addition", "subtraction", "multiplication", "division", "integer division", "modulo", "exponent"]

while True:
    num1 = float(input("What is the first number you want to use in the equation: "))
    num2 = float(input("What is the second number you want to use in the equation: "))

    while True:
        equation_type = input("What type of math equation do you want to use (addition, subtraction, multiplication, division, integer division, modulo, exponent): ").strip().lower()
        if equation_type in types: 
            break
        else:
            print("Please type a valid input")
    if equation_type == "addition":
        operator = "+"
        result = num1 + num2
    elif equation_type == "subtraction":
        operator = "-"
        result = num1 - num2
    elif equation_type == "multiplication":
        operator = "*"
        result = num1 * num2
    elif equation_type == "division":
        operator = "/"
        result = num1 / num2
    elif equation_type == "integer division":
        operator = "//"
        result = num1 // num2
    elif equation_type == "modulo":
        operator = "%"       
        result = num1 % num2
    elif equation_type == "exponent":
        operator = "**"
        result = num1 ** num2
        num1 = round(num1, 2)
        num2 = round(num2, 2)
        result = round(result, 2)
    print(f"{num1:.2f} {operator} {num2:.2f} = {result:.2f}")
    repeat = input("Do you want to try another calculation?(Yes/No): ").strip().lower()
    if not repeat ==  "yes":
        break