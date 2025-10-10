#DL 1st, password strength

# initialize length_check, uppercase_check, lowercase_check, number_check, and special_char_check all with False values
# case_check = ""
# points = 0

# user_pass = input by user with instructions on the criteria of the password and instructions

# if length of user password is Greater than or equal to 8:
#  length check = True


# loop for characters in user_pass:
#   if char is uppercase
#       uppercase_check = True
#   or if char is lowercase
#       lowercase_check = True
#   or if char is a number
#        nuber_check = True




test = "THIS should work"
test_check = test.lower().replace(" ", "")

for char in test:
    if char in test_check:
        print("hi")