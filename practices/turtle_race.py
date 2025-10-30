#DL 1st, turtle race practice

from turtle import *
import random

height = window_height()
width = window_width()
screen = Screen()
screen_width = window_width()
screen_height = window_height()

def win(cur_pos):
    finish_line_x = screen_width // 2 - 50
    return cur_pos >= finish_line_x


def steps():
    steps = random.randint(100,500)
    return steps

def map_setup():
    speed(10)
    penup()
    teleport((width/10*4),(height/3))
    pendown()
    right(90)
    forward(height-(height/3))
    speed(1)
    hideturtle()


map_setup()


t1 = Turtle()
t1.color("red")
t1.shape("turtle")
t1.teleport((width/1000 - 600),(height/10-300))
t2 = Turtle()
t2.color("yellow")
t2.shape("turtle")
t2.teleport((width/1000 - 600),(height/10*2-300))
t3 = Turtle()
t3.color("blue")
t3.shape("turtle")
t3.teleport((width/1000 - 600),(height/10*3-300))
t4 = Turtle()
t4.color("green")
t4.shape("turtle")
t4.teleport((width/1000 - 600),(height/10*4-300))
t5 = Turtle()
t5.color("purple")
t5.shape("turtle")
t5.teleport((width/1000 - 600),(height/10*5-300))

all_turtles = [t1, t2, t3, t4, t5]

while True:
    for all_turtle in all_turtles:
        all_turtle.forward(steps())
        if all_turtle.xcor() > 250:
            race_is_on = False
            winning_color = all_turtle.pencolor()
            print(f"The {winning_color} turtle wins!")
            done()
            break
