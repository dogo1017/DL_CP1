#DL 1st, cesar cypher practice
# use a list with each lower and uppercase letter
new = []
up_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# define the function encode with parameters char and num_shift
def encode_decode(char,num_shift):
    if char in up_letters:
        char_ind = up_letters.idex(char)
        char = up_letters(char_ind + num_shift)
        return(char)
    elif char in low_letters:
        char_ind = low_letters.idex(char)
        char = low_letters(char_ind + num_shift)
        return(char)
    else:
        return (char)

# use a list to give each letter of the alphabet upper and lowercase a value of its num in asci 



# display options decode and encode with numbers and take in the input in variable operation
while True:
    operation = input("Which operation would you like to preform?\n1) encode\n2) decode\n").strip()
    if operation == 1:
        message = input("What message would you like to encode: ")
        break
    elif operation == 2:
        message = input("What message would you like to decode: ")
        break
    else:
        print("Please write a valid input(1-2)")

num_shift = input("How much would you like to shift the message by (1-25): ").strip

message = input("What message would you like to change: ")

if operation == 2:
    num_shift = num_shift * -1

for char in message:
    new.append(encode_decode)