#DL 1st, squared numbers practice

#code golfed(72)
# set r to range to show how many number, set l to the results of each number times itself using mapand lambda, then loop for each number in the list r that prints an output with the valuse from the current loop and the squared number using the current iteration as the index
r=range(21);l=list(map(lambda n:n*n,r))
for i in r:print(f"{i}²={l[i]}")

# One line version(75)
#r=range(21);l=list(map(lambda n:n*n,r));[print(f"{i}^2={l[i]}") for i in r]


# version with better output if first one doesnt meet rubric
#r=range(21);l=list(map(lambda n:n*n,r))
#for i in r:print(f"Original: {i}, Squared:{l[i]}")

# Non map Version(40)
#for i in range(21):print(f"{i}²={i*i}")
