


def part_1(garden: list[list[str]]) -> int:
    visited = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]
    areas = []

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if not visited[i][j]:
                areas.append(dfs(garden, i, j, garden[i][j], visited))

    price = 0
    for area, perimeter in areas:
        print(area, perimeter)
        price += area * perimeter

    return price

def check_corner(grid, points, plant):
    result = []
    for i in range(len(points)):
        point = points[i]
        if point[0] < 0 or point[0] >= len(grid) or point[1] < 0 or point[1] >= len(grid[0]):
            result.append("Border")
        elif grid[point[0]][point[1]] != plant:
            result.append("Diff")
        else:
            result.append("Same")
    
    if result == ["Diff", "Same", "Same"]:
        return 1
    elif result == ["Same", "Diff", "Diff"]:
        return 1
    elif "Same" not in result:
        return 1

    else:
        return 0


def get_corners(grid, x, y):
    plant = grid[x][y]
    top_left = [(x-1, y-1), (x, y-1), (x-1, y)]
    top_right = [(x-1, y+1), (x, y+1), (x-1, y)]
    bottom_left = [(x+1, y-1), (x, y-1), (x+1, y)]
    bottom_right = [(x+1, y+1), (x, y+1), (x+1, y)]

    corners = (check_corner(grid, top_left, plant) + check_corner(grid, top_right, plant) +
               check_corner(grid, bottom_left, plant) + check_corner(grid, bottom_right, plant))
    return corners
    

def get_perimeter(garden, x, y):
    plant = garden[x][y]
    perimeter = 4
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_x = x + dx
        next_y = y + dy
        if next_x < 0 or next_x >= len(garden) or next_y < 0 or next_y >= len(garden[0]):
            continue
        if garden[next_x][next_y] == plant:
            perimeter -= 1
    return perimeter


def dfs(garden, x, y, plant, visited):
    if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
        return 0, 0
    elif visited[x][y] or garden[x][y] != plant:
        return 0, 0

    visited[x][y] = True
    perimeter = get_corners(garden, x, y)
    count = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        result = dfs(garden, x + dx, y + dy, plant, visited)
        count += result[0]
        perimeter += result[1]
    return count, perimeter




if __name__ == '__main__':
    with open('day_12.input') as f:
        input = f.read().splitlines()
        input = [list(line) for line in input]
    f.close()
    print(part_1(input))