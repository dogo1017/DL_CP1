# DL 1st, maze_generator

import random
import turtle as t

def is_solvable(grid_rows):
    
    stack_unvisited = False
    stack = [[0,0]]
    x = 0
    y = 0
    stack_pos = 0
    visited = []
    while stack_unvisited == False:
        if  [len(grid_rows[1]),len(grid_rows)] in stack:
            return True
        x = stack[stack_pos][0]
        y = stack[stack_pos][1]
        if stack[stack_pos] in visited:
            stack_pos += 1
            continue
        visited.append(stack[stack_pos])
        if grid_rows[x+1][y] >= 0 and grid_rows[x+1][y] <= len(grid_rows[1]) and grid_rows[x+1][y] == 0:
            stack.append([x+1, y])
        if grid_rows[x-1][y] >= 0 and grid_rows[x-1][y] <= len(grid_rows[1]) and grid_rows[x-1][y] == 0:
            stack.append([x-1, y])
        if grid_rows[x][y+1] >= 0 and grid_rows[x][y+1] <= len(grid_rows) and grid_rows[x][y+1] == 0:
            stack.append([x, y+1])
        if grid_rows[x][y-1] >= 0 and grid_rows[x][y-1] <= len(grid_rows) and grid_rows[x][y-1] == 0:
            stack.append([x, y-1])
        if stack_pos + 1 in range(0,len(stack)):
            stack_pos += 1
        else:
            last_visited = visited[len(visited)]
            stack_pos = visited.index(last_visited)




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


while is_solvable(grid_rows) == False:
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

