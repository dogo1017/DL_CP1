# DL 1st, maze_generator

import random
import turtle as t

grid_rows = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]

grid_columns = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]

for row in range(len(grid_rows)):
    for col in range(len(grid_rows[row])):
        grid_rows[row][col] = random.randint(0, 1)

for row in range(len(grid_rows)):
    for col in range(len(grid_rows[row])):
        if grid_rows[row][col] == 1:
            grid_rows[row][col] = random.randint(1,2)

for column in range(len(grid_columns)):
    for row in range(len(grid_columns[column])):
        grid_columns[column][row] = random.randint(0, 1)

for column in range(len(grid_columns)):
    for row in range(len(grid_columns[column])):
        if grid_columns[column][row] == 1:
            grid_columns[column][row] = random.randint(1,2)


t.teleport(0,0)
t.penup()
t.back(25)
t.left(90)
t.forward(25)
t.right(90)
t.pendown()
t.forward(25 * len(grid_rows[1]))

t.penup()
t.teleport(0,0)
t.back(25)
t.right(90)
t.back(25)
t.pendown()
t.forward(25 * len(grid_rows[1]))
t.right(90)
t.forward((25 * len(grid_rows[1])))
t.speed(0)

for row in range(len(grid_rows)):
    for col in range(len(grid_rows[row])):
        if grid_rows[row][col] == 1:
            t.pendown()
        t.forward(25)
        t.penup()
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25 * len(grid_rows[1]))
    t.right(180)

t.teleport(0,0)
t.right(90)

for column in range(len(grid_columns)):
    for row in range(len(grid_columns[column])):
        if grid_columns[column][row] == 1:
            t.pendown()
        t.forward(25)
        t.penup()
    t.right(-90)
    t.forward(25)
    t.right(-90)
    t.forward(25 * len(grid_columns[1]))
    t.right(180)



t.done()

