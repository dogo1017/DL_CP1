# DL 1st, password strength

#initialize run as "yes"
run = "yes" 
#initialize run_input as "yes"
run_input = "yes"

#loop entire code while the value of the variable run is "yes"
while run == "yes":
    #initialize length_check, uppercase_check, lowercase_check, number_check, and special_char_check all with the value of 0
    length_check = uppercase_check = lowercase_check = number_check = special_char_check = 0
    #spec_char = list with all special characters accepted (!@#$%^&*()_+-=[]{}|;:,.<>?)
    spec_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]

    #user_pass = input by user with instructions on the criteria of the password and instructions and use .strip to stupid proof
    user_pass = input("Please type a password: ").strip()
    #if length of user password is Greater than or equal to 8:
    if len(user_pass) >= 8:
        #length check = 1
        length_check = 1
    #loop for characters in user_pass
    for char in user_pass:
        #if character is uppercase
        if char.isupper() == True:  
            #set the value of uppercase_check as 1
            uppercase_check = 1
        #or if character is lowercase
        elif char.islower() == True:
            #Set the value of lowercase_check as 1
            lowercase_check = 1
        #or if character is a number
        elif char.isdigit() == True:
            #Set the value of number_check as 1
            number_check = 1
        #or if character matches an item in spec_char list
        elif char in spec_char:
            #set the value of special_char_check as 1
            special_char_check = 1
        #else:
        else:
            #display that the character being looped is not a valid character that can be used and break
            print(f"''")

    #pass_strength = all check variables added together
    #display pass_strength to user

    #if pass_strength is less than 5
        #display info on the info that comes next showing what part of the password is weak
    #if length_check = 0
        #display that the password needs to be greater than 8
    #if uppercase_check = 0
        #display that the password needs to have an uppercase letter
    #if lowercase_check = 0
        #display that the password needs to have an lowercase letter
    #if number_check = 0
        #display that the password needs to include a number
    #if special_char_check = 0
        #display that the password needs to include a special character (!@#$%^&*()_+-=[]{}|;:,.<>?)

    #loop until break:
        #run_input = display question of if user want to try again (Yes/No) and use .strip() and .lower() to stupid proof
        #if run_input equals yes or no then end loop
        #else:
            #print to type a valid input