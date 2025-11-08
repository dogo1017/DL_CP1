# DL 1st, maze_generator

import random
import turtle as t

grid_size_x = 20
grid_size_y = 20
SQUARE_SIZE = 25

screen = t.Screen()
t.tracer(0)

def is_solvable(grid_rows):
    stack_unvisited = False
    stack = [[0,0]]
    x = 0
    y = 0
    stack_pos = 0
    visited = []

    max_x = len(grid_rows[0]) - 1
    max_y = len(grid_rows) - 1

    while stack_unvisited == False:
        if  [max_y, max_x] in stack:
            return True
        if len(stack)-1 < stack_pos:
            return False
        x = stack[stack_pos][1]
        y = stack[stack_pos][0]
        if stack[stack_pos] in visited:
            stack_pos += 1
            continue
        visited.append(stack[stack_pos])
        if y < max_y and (grid_rows[y][x] == 0 or grid_rows [y][x] == 2):
            stack.append([y+1, x])
        if x < max_x and (grid_rows[y][x] == 0 or grid_rows [y][x] == 1):
            stack.append([y, x+1])
        if x > 0 and (grid_rows[y][x-1] == 0 or grid_rows[y][x-1] == 1):
            stack.append([y,x-1])
        if y > 0 and (grid_rows[y-1][x] == 0 or grid_rows[y-1][x] == 2):
            stack.append([y-1,x])

        if stack_pos + 1 in range(0,len(stack)):
            stack_pos += 1
        else:

            last_visited = visited[len(visited)-1]
            stack_pos = visited.index(last_visited) + 1


def generate_grid(size_x, size_y):
    grid = []
    for y in range(0, size_y):
        row = []
        for x in range(0, size_x):
            row.append(0)
        grid.append(row)

    return grid

grid = generate_grid(grid_size_x, grid_size_y)

for row in range(len(grid)):
    for col in range(len(grid[row])): 
        grid[row][col] = random.randint(1, 3)

grid[0][0] = 0
grid[grid_size_y - 1][grid_size_x - 1] = 0


maze_it = 0
while is_solvable(grid) == False:
    maze_it += 1
    #print(f'Maze generation attempt {maze_it}')
    new_x = random.randint(0, grid_size_x - 1)
    new_y = random.randint(0, grid_size_y - 1)
    grid[new_y][new_x] = 0


    
t.speed(0)
t.teleport(SQUARE_SIZE, 0)
t.forward(SQUARE_SIZE * grid_size_x - SQUARE_SIZE)
t.right(90)

t.forward(SQUARE_SIZE * grid_size_y)
t.right(90)
t.penup()
t.forward(SQUARE_SIZE)
t.pendown()
t.forward(SQUARE_SIZE * grid_size_x - SQUARE_SIZE)
t.right(90)
t.forward(SQUARE_SIZE * grid_size_y)


for row in range(grid_size_y):
    for col in range(grid_size_x):
        if grid[row][col] == 1 or grid[row][col] == 3:
            t.teleport(col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE * -1)
            t.goto((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE * -1)
        if grid[row][col] == 2 or grid[row][col] == 3:
            t.teleport((col + 1) * SQUARE_SIZE, (row) * SQUARE_SIZE * -1)
            t.goto((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE * -1)


t.done()

screen.update()
t.done()