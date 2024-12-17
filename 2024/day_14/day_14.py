from collections import defaultdict
import re

def print_grid(grid):
    for row in grid:
        print_row = []
        for cell in row:
            if cell == 0:
                print_row.append('.')
            else:
                print_row.append(str(cell))
        print(''.join(print_row))

def part_1(moves, iterations):
    tiles_tall, tiles_wide = 103, 101
    grid = [[0 for _ in range(tiles_wide)] for _ in range(tiles_tall)]
    robots = defaultdict(tuple[list, list])

    # generate robots dict
    for i in range(len(moves)):
        move = moves[i]
        p, v = move[0], move[1]
        robots[i] = (p, v)

    # iterate through robot moves
    for _ in range(iterations):
        for robot_id in robots:
            p, v = robots[robot_id]
            x, y = p[0], p[1]
            vx, vy = v[0], v[1]
            x, y = (x + vx) % tiles_wide, (y + vy) % tiles_tall
            robots[robot_id] = ([x, y], v)
    
    for robot_id in robots:
        p, v = robots[robot_id]
        x, y = p[0], p[1]
        grid[y][x] += 1
    
    print_grid(grid)

    # get quadrant scores (assuming grid lengths are always odd)
    x_mid = tiles_wide // 2
    y_mid = tiles_tall // 2

    quad1, quad2, quad3, quad4 = 0, 0, 0, 0
    for i in range(y_mid):
        for j in range(x_mid):
            quad1 += grid[i][j]
    for i in range(y_mid+1, tiles_tall):
        for j in range(x_mid):
            quad3 += grid[i][j]
    for i in range(y_mid):
        for j in range(x_mid+1, tiles_wide):
            quad2 += grid[i][j]
    for i in range(y_mid+1, tiles_tall):
        for j in range(x_mid+1, tiles_wide):
            quad4 += grid[i][j]

    return quad1 * quad2 * quad3 * quad4

def part_2(moves, iterations):
    tiles_tall, tiles_wide = 103, 101
    grid = [['.' for _ in range(tiles_wide)] for _ in range(tiles_tall)]
    robots = defaultdict(tuple[list, list])

    # generate robots dict
    for i in range(len(moves)):
        move = moves[i]
        p, v = move[0], move[1]
        robots[i] = (p, v)


    check_str = '*' * 10
    # iterate through robot moves
    for _ in range(iterations):
        for robot_id in robots:
            p, v = robots[robot_id]
            x, y = p[0], p[1]
            grid[y][x] = '.'
            vx, vy = v[0], v[1]
            x, y = (x + vx) % tiles_wide, (y + vy) % tiles_tall
            robots[robot_id] = ([x, y], v)
            grid[y][x] = '*'
        
        for y in range(tiles_tall):
            if check_str in ''.join(grid[y]):
                print("iteration", _+1, "found solution")
                for i in range(tiles_tall):
                    print(''.join(grid[i]))
                break
        


if __name__ == '__main__':
    with open('day_14.input') as f:
        lines = f.read().splitlines()
        lines = [line.split(" ") for line in lines]
        # [...(p=[px, py], v=[vx, vy]), ...]
        moves = []
        for line in lines:
            p, v = line[0], line[1]
            p, v = list(map(int, re.findall(r'-?\d+', p))), list(map(int, re.findall(r'-?\d+', v)))
            moves.append((p, v))
    f.close()

    # print(part_1(moves, 100))
    print(part_2(moves, 10000))

