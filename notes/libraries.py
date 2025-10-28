#DL 1st, libraries notes
import turtle as t
import random
colors = ["orange", "green", "blue", "red", "purple"]

side = random.randint(10,500)
t.color(random.choice(colors))
screen = t.Screen()
screen.addshape('rickroll-roll.gif')
t.shape('rickroll-roll.gif')
screen.mainloop()



t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()


t.penup()
t.goto(50,50)


t.begin_fill()
for i in range(4):
    t.forward(250)
    t.right(90)
t.end_fill()

t.pendown()



t.done()