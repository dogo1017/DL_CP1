# DL 1st, maze_generator

import random
import turtle as t

def is_solvable(grid):
    
    stack_unvisited = True
    stack = [0,0]
    x = 0
    y = 0
    while stack_unvisited == False:
        



grid_rows = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

grid_columns = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



for row in range(len(grid_rows)):
    for col in range(len(grid_rows[row])):
        grid_rows[row][col] = random.randint(0, 1)

for row in range(len(grid_rows)):
    for col in range(len(grid_rows[row])):
        if grid_rows[row][col] == 1 or grid_rows[row][col] == 2:
            grid_rows[row][col] = random.randint(1,2)

for column in range(len(grid_columns)):
    for row in range(len(grid_columns[column])):
        grid_columns[column][row] = random.randint(0, 1)

for column in range(len(grid_columns)):
    for row in range(len(grid_columns[column])):
        if grid_columns[column][row] == 1 or grid_columns[column][row] == 2:
            grid_columns[column][row] = random.randint(1,2)

t.speed(0)
t.teleport(0,0)
t.penup()
t.back(25)
t.left(90)
t.forward(25) 
t.right(90)
t.forward(25)
t.pendown()
t.forward((25 * len(grid_rows[1]))-25)
t.right(90)

t.forward((25 * len(grid_rows[1])))
t.right(90)
t.penup()
t.forward(25)
t.pendown()
t.forward((25 * len(grid_rows[1]))-25)
t.right(90)
t.forward(25 * len(grid_rows[1]))

t.teleport(0,0)
t.right(90)
t.backward(25)
for row in range(len(grid_rows)):
    for col in range(len(grid_rows[row])):
        if grid_rows[row][col] == 1 or grid_rows[row][col] == 2:
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
t.backward(25)

for column in range(len(grid_columns)):
    for row in range(len(grid_columns[column])):
        if grid_columns[column][row] == 1 or grid_columns[column][row] == 2:
            t.pendown()
        t.forward(25)
        t.penup()
    t.right(-90)
    t.forward(25)
    t.right(-90)
    t.forward(25 * len(grid_columns[1]))
    t.right(180)



t.done()

