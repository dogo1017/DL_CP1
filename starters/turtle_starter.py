import turtle as t

def draw_branch(length):
    if length > 5:
        t.forward(length)
        draw_branch(length / 3)
        t.backward(length)
        t.right(60)

t = t.Turtle()
t.speed(10)
t.color("light blue")
t.penup()
t.teleport(0,0)
t.pendown()

for i in range(6):
    draw_branch(100)
    t.right(60)

t.hideturtle()