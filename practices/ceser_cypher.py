#DL 1st, cesar cypher practice

# create an empty string to hold the new encoded or decoded message
new = ""

# create lists of uppercase and lowercase letters
up_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# define the function encode_decode with parameters char and num_shift
def encode_decode(char,num_shift):
    # if the character is uppercase
    if char in up_letters:
        # find the index of the character in uppercase list
        char_ind = up_letters.index(char)
        # wrap around alphabet using modulo (handles both forward and backward)
        char = up_letters[(char_ind + num_shift) % 26]
        # return the shifted uppercase character
        return(char)
    # if the character is lowercase
    elif char in low_letters:
        # find the index of the character in lowercase list
        char_ind = low_letters.index(char)
        # wrap around alphabet using modulo (handles both forward and backward)
        char = low_letters[(char_ind + num_shift) % 26]
        # return the shifted lowercase character
        return(char)
    # if the character is not a letter, just return it as is
    else:
        return (char)

# loop until a valid operation is chosen (encode or decode)
while True:
    operation = input("Which operation would you like to preform?\n1) encode\n2) decode\n")
    # if user chooses encode
    if operation == "1":
        message = input("What message would you like to encode: ")
        break
    # if user chooses decode
    elif operation == "2":
        message = input("What message would you like to decode: ")
        break
    # if invalid input, ask again
    else:
        print("Please write a valid input(1-2)")

# loop until a valid shift amount is entered
while True:
    num_shift = int(input("How much would you like to shift the message by (1-25): "))
    # check if shift is within valid range
    if num_shift in range(1,26):
        break
    else:
        print("Please input a number from 1-25")

# if the operation is decode, make shift negative
if operation == "2":  # <-- FIXED (was comparing to int before)
    num_shift = num_shift * -1

# loop through each character in the message and encode/decode it
for char in message:
    new = new + encode_decode(char,num_shift)

# print the final encoded or decoded message
print(new)
