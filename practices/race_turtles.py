#DL 1st, turtle race practice

#  Import everything from the turtle module (this lets us draw and move turtles)
from turtle import *

# Import the random module so we can make the turtles move random distances
import random

# Get the height of the turtle window
height = window_height()

# Get the width of the turtle window
width = window_width()

# Create a screen where the turtles will race
screen = Screen()

# Get the width of the screen
screen_width = window_width()

# Get the height of the screen
screen_height = window_height()


#  Define a function to check if a turtle has reached the finish line
def win(cur_pos):
    # The finish line will be near the right side of the screen
    finish_line_x = screen_width // 2 - 50
    # If the turtle’s position is past the finish line, it wins
    return cur_pos >= finish_line_x


#  Define a function to decide how far a turtle should move each turn
def steps():
    # Choose a random number between 50 and 100 for how far the turtle moves
    steps = random.randint(50,100)
    return steps


#  Define a function to draw the finish line
def map_setup():
    speed(10) # turn speed up to make map setup faster
    penup() # lift pen
    goto(300, height/2 - 100)  # move to top of screen near the right
    pendown() # put pen down to start drawing
    right(90) # turn the turtle to be facing down
    forward(height - 200)  # draw finish line downward
    penup() # lift pen
    hideturtle() # hide the turtle


# Call the function to set up the race map
map_setup()

# Create the first racing turtle (red)
t1 = Turtle()
t1.color("red") # Give it a red color
t1.shape("turtle") # Make it look like a turtle
t1.teleport((width/1000 - 600),(height/10-300))  # Move it to its starting position

# Create the second racing turtle (yellow)
t2 = Turtle()
t2.color("yellow")
t2.shape("turtle")
t2.teleport((width/1000 - 600),(height/10*2-300))

# Create the third racing turtle (blue)
t3 = Turtle()
t3.color("blue")
t3.shape("turtle")
t3.teleport((width/1000 - 600),(height/10*3-300))

# Create the fourth racing turtle (green)
t4 = Turtle()
t4.color("green")
t4.shape("turtle")
t4.teleport((width/1000 - 600),(height/10*4-300))

# Create the fifth racing turtle (purple)
t5 = Turtle()
t5.color("purple")
t5.shape("turtle")
t5.teleport((width/1000 - 600),(height/10*5-300))


# Put all the turtles into a list so we can loop through them easily
all_turtles = [t1, t2, t3, t4, t5]


# Start the race — keep running until one turtle wins
while True:
    # Go through each turtle one by one
    for all_turtle in all_turtles:
        # Move the turtle forward by a random distance
        all_turtle.forward(steps())
        # Check if this turtle has crossed the finish line
        if all_turtle.xcor() > 300:
            # Stop the race when a turtle wins
            race_is_on = False
            # Get the color of the winning turtle
            winning_color = all_turtle.pencolor()
            # Print out the winning turtle’s color
            print(f"The {winning_color} turtle wins!")
            # Keep the window open so we can see the result
            done()
            # Exit the loop so the race ends
            break