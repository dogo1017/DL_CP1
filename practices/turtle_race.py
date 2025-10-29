#DL 1st, turtle race practice

import turtle as t
import random

def steps():
    steps = random.randint(10,50)
    return steps

screen = t.Screen()
screen.setup(600,400)


map = t.Turtle()
map.teleport(580,380) 
map.pencolor("black")
map.pendown()
map.right(90)
map.forward(360)
map.penup()
    


t1 = t.Turtle()
t1.color("red")
t1.shape("turtle")
t2 = t.Turtle()
t2.color("yellow")
t2.shape("turtle")
t3 = t.Turtle()
t3.color("blue")
t3.shape("turtle")
t4 = t.Turtle()
t4.color("green")
t4.shape("turtle")
t5 = t.Turtle()
t5.color("purple")
t5.shape("turtle")

all_turtles = [t1, t2, t3, t4, t5]

while True:
    for turtle in all_turtles:
        print("hi")
        break

t.done()