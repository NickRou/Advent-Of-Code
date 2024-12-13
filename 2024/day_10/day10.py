def aoc10():
    with open("day10.input") as f:
        grid = f.read().splitlines()
    f.close()
    for i in range(len(grid)):
        grid[i] = list(grid[i])

    print(calc_trails(grid))

def calc_trails(grid):
    trailhead_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # start of a trailhead
            if grid[i][j] == '0':
                score = find_trail_rating(grid, i, j, 0)
                print("Score: " + str(score))
                trailhead_score += score

    return trailhead_score

def out_of_bounds(x, y, grid):
    return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])


def find_trail(grid, x, y, curr_height, visited=None):
    if visited is None:
        visited = set()
    if out_of_bounds(x, y, grid) or (x, y) in visited or int(grid[x][y]) != curr_height:
        return 0
    visited.add((x, y))
    if grid[x][y] == '9':
        return 1
    
    return (find_trail(grid, x + 1, y, curr_height + 1, visited) + 
            find_trail(grid, x - 1, y, curr_height + 1, visited) + 
            find_trail(grid, x, y + 1, curr_height + 1, visited) + 
            find_trail(grid, x, y - 1, curr_height + 1, visited))


def find_trail_rating(grid, x, y, curr_height):
    if out_of_bounds(x, y, grid) or int(grid[x][y]) != curr_height:
        return 0
    if grid[x][y] == '9':
        return 1
    
    return (find_trail_rating(grid, x + 1, y, curr_height + 1) + 
            find_trail_rating(grid, x - 1, y, curr_height + 1) + 
            find_trail_rating(grid, x, y + 1, curr_height + 1) + 
            find_trail_rating(grid, x, y - 1, curr_height + 1))




aoc10()