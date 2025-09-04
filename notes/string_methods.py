# DL 1st, String Methods Notes

subject = "Computer Programming 1!"
print(subject.upper())
print(subject.center(100))

# Stupid/idiot Proofing
#color = input("What is your favorite color? ").strip().lower()
#title() capitalizes each word
##print("That is cool " + full_name + ". I like " + color + " Too!")
##full_name = input("What is your full name? ").strip().title()
##print("That is cool {full_name}. I like {color} Too!".format(full_name = full_name, color = color))
##print(f"That is cool {full_name}. I like {color} Too!")
pi = "3.14159"
#print(f"We all know pie is equal to {pi: 3f}")
print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog."
word = "jumps"
print(sentence.find(word))
start = sentence.index(word)
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)
