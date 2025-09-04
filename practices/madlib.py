#DL 1st, madlibs

inputs = []
num = 0
word_types = [
    "n adjective",            # 0
    "n adjective",            # 1
    " type of bird",         # 2
    " room in a house",      # 3
    " verb (past tense)",    # 4
    " verb",                 # 5
    " relative's name",      # 6
    " noun",                 # 7
    " liquid",               # 8
    " verb ending in -ing",  # 9
    " part of body (plural)",# 10
    " noun (plural)",        # 11
    " verb ending in -ing",  # 12
    " noun"                  # 13
]

for i in word_types:
    word = input(f"Give me a{word_types[num]}: ")
    inputs.append(word)
    num += 1

message = "It was a " + inputs[0] + ", cold November day. I’m  I woke up to the " + inputs[1] + " smell of " + inputs[2] + " roasting in the " + inputs[3] + " Room downstairs. I " + inputs[4] + " down the stairs to see if I could help " + inputs[5] + " the " + inputs[2] + ' dinner. My mom said, “See if ' + inputs[6] + " needs a fresh " + inputs[8] + '." So I carried a tray of glasses full of the liquid into the ' + inputs[9] + " room. When I got there, I was so shocked I dropped the " + inputs[8] + ", I couldn’t believe my " + inputs[10] + "! There was " + inputs[11] + " " + inputs[12] + " on the " + inputs[13] + "!"

print(message)