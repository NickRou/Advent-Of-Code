import copy
import time

start = time.time()

grid = []

with open('day6.input') as file:
    for line in file:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])
guard_pos_y, guard_pos_x = 0, 0
grid_visited = []

for i in range (0, rows):
    grid_visited.append([])
    for j in range (0, cols):
        grid_visited[i].append(False) 
        if grid[i][j] == '^':
            guard_pos_y, guard_pos_x = i, j
            grid_visited[i].append(True)

count = 0 
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dir_next = {0: 3, 1: 2, 2: 0, 3: 1}
dir_index = 0
dy, dx = -1, 0 

def check_loop(_grid, _dy, _dx, _guard_pos_y, _guard_pos_x, _dir_index):
    _grid_visited = {} 
    while True:
        # Change from the previous approach: Use dict instead of a list of tuples.
        # Lowers the visited checking complexity from Linear time to Logarithmic. 
        # This of course results in a significant saving of time.  
        if _grid_visited.get((_guard_pos_y, _guard_pos_x)) is None: 
            _grid_visited[(_guard_pos_y, _guard_pos_x)] = [_dir_index]
        elif _dir_index not in _grid_visited[(_guard_pos_y, _guard_pos_x)]:
            _grid_visited[(_guard_pos_y, _guard_pos_x)].append(_dir_index)
        else:
            global count
            count += 1
            return
        if 0<=_guard_pos_y + _dy<rows and 0<=_guard_pos_x + _dx<cols:
            if _grid[_guard_pos_y + _dy][_guard_pos_x + _dx] == '#':
                _dir_index = dir_next[_dir_index]
                _dy, _dx = dirs[_dir_index][0], dirs[_dir_index][1]
                continue
        else:
            return
        _guard_pos_y += _dy
        _guard_pos_x += _dx

while True:
    if 0<=guard_pos_y + dy<rows and 0<=guard_pos_x + dx<cols:
        if grid[guard_pos_y + dy][guard_pos_x + dx] == '#':
            dir_index = dir_next[dir_index]
            dy, dx = dirs[dir_index][0], dirs[dir_index][1]
            continue
        elif not(grid_visited[guard_pos_y + dy][guard_pos_x + dx]):
            grid_visited[guard_pos_y + dy][guard_pos_x + dx] = True
            grid_copy = copy.deepcopy(grid)
            grid_copy[guard_pos_y + dy][guard_pos_x + dx] = '#';
            check_loop(grid_copy, dy, dx, guard_pos_y, guard_pos_x, dir_index)
        guard_pos_y += dy 
        guard_pos_x += dx
    else:
        break

print(count)

end = time.time()

print(f"{end-start} seconds taken to get the answer.") # 23.6 seconds on my computer. 
                                                       # 6 times speedup. 