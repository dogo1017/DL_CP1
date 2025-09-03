#DL 1st, madlibs

inputs = []
num = 1
word_types = ["n adjective", "n adjective", " type of bird", " room in a house", " verb (past tense)", " verb", " relatives name", " noun", " liquid", " verb ending in -ing", " part of body (plural)", " noun (plural)",  " verb ending in -ing", " noun"]

for i in word_types:
    word = input(f"Give me a{word_types[num]}: ")
    inputs[num] = {'word': word} 
    num += 1