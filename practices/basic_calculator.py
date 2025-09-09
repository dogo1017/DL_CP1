#DL 1st, basic calculator
types = ["addition", "subtraction", "multiplication", "division", "integer division", "modulo", "exponent"]
num1 = input("What is the first number you want to use in the equation")
num2 = input("What is the second number you want to use in the equation")
result_add = num1 + num2
result_sub = num1 - num2
result_mult = num1 * num2
result_div = num1 / num2
result_int_div = num1 // num2
result_mod = num1 % num2
result_exp = num1 ** num2
while True:
    equation_type = input("What type of math equation do you want to use (addition, subtraction, multiplication, division, integer division, modulo, exponent)").strip().lower()
    if equation_type in types: 
        break
    else:
        print("Please type a valid input")
