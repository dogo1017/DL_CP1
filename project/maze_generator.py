#DL 1st, maze_generator

import random
import turtle as t

# --- Maze grid ---
maze_grids = [
"WOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXW"
]

# --- Maze generation (your branch method) ---
cur_pos = [0, 1]  
maze_grids[cur_pos[0]] = maze_grids[cur_pos[0]][:cur_pos[1]] + "O" + maze_grids[cur_pos[0]][cur_pos[1]+1:]

branch_options = [cur_pos]

while branch_options:
    cur_pos = random.choice(branch_options)
    r, c = cur_pos

    vert_move_opts = []
    horz_move_opts = []

    if r > 1 and maze_grids[r - 2][c] == "W":  
        vert_move_opts.append(r - 2)
        horz_move_opts.append(c)
    if r < len(maze_grids) - 2 and maze_grids[r + 2][c] == "W":  
        vert_move_opts.append(r + 2)
        horz_move_opts.append(c)
    if c > 1 and maze_grids[r][c - 2] == "W":  
        vert_move_opts.append(r)
        horz_move_opts.append(c - 2)
    if c < len(maze_grids[0]) - 2 and maze_grids[r][c + 2] == "W": 
        vert_move_opts.append(r)
        horz_move_opts.append(c + 2)

    if not vert_move_opts:
        maze_grids[r] = maze_grids[r][:c] + "F" + maze_grids[r][c+1:]
        branch_options.remove(cur_pos)
        continue

    move = random.randint(0, len(vert_move_opts) - 1)
    new_r = vert_move_opts[move]
    new_c = horz_move_opts[move]

    mid_r = (r + new_r) // 2
    mid_c = (c + new_c) // 2
    maze_grids[mid_r] = maze_grids[mid_r][:mid_c] + "O" + maze_grids[mid_r][mid_c+1:]

    maze_grids[new_r] = maze_grids[new_r][:new_c] + "O" + maze_grids[new_r][new_c+1:]

    branch_options.append([new_r,new_c])

# --- Turtle drawing ---
t.speed(0)
t.hideturtle()
t.penup()

cell_size = 20
start_x = -len(maze_grids[0]) * cell_size / 2
start_y = len(maze_grids) * cell_size / 2

for row_i, row in enumerate(maze_grids):
    for col_i, cell in enumerate(row):
        x = start_x + col_i * cell_size
        y = start_y - row_i * cell_size
        t.goto(x, y)
        t.pendown()
        if cell == "W":
            t.fillcolor("black")
        elif cell == "O":
            t.fillcolor("white")
        elif cell == "F":
            t.fillcolor("lightgray")
        elif cell == "X":
            t.fillcolor("red")
        t.begin_fill()
        for _ in range(4):
            t.forward(cell_size)
            t.right(90)
        t.end_fill()
        t.penup()

t.done()
