if grid_rows[y][x+1] >= 0 and grid_rows[y][x+1] <= len(grid_rows[1]) and grid_rows[y][x+1] == 0:
            stack.append([y, x+1])
        if grid_rows[y][x-1] >= 0 and grid_rows[y][x-1] <= len(grid_rows[1]) and grid_rows[y][x-1] == 0:
            stack.append([y, x-1])
        if grid_rows[y+1][x] >= 0 and grid_rows[y+1][x] <= len(grid_rows) and grid_rows[y+1][x] == 0:
            stack.append([y+1, x])
        if grid_rows[y-1][x] >= 0 and grid_rows[y-1][x] <= len(grid_rows) and grid_rows[y-1][x] == 0:
            stack.append([y-1, x])