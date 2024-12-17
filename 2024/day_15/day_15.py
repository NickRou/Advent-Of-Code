def parse_input():
    with open('day_15.input') as f:
        grid, moves = f.read().split("\n\n")
    f.close()

    grid = [list(row) for row in grid.splitlines()]

    return grid, moves

class Warehouse:
    def __init__(self, grid, moves):
        self.grid = grid
        self.moves = moves
        self.robot_marker = '@'
        self.free_space_marker = '.'
        self.box_marker = 'O'
        self.wall_marker = '#'

    def print_grid(self):
        for row in self.grid:
            print_row = ''.join(row)
            print(print_row)

    def find_robot_position(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == self.robot_marker:
                    return i, j
                
    def calculate_gps_sum(self):
        # 100 * distance from top edge + distance from left edge
        gps_sum = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == self.box_marker:
                    gps_sum += 100 * i + j

        return gps_sum
                
    def move_boxes(self, move, robot):
        x, y = robot.pos
        dir = robot.dir(move)
        
        # find all boxes in direction until we hit a free space
        boxes = []
        x, y = x + dir[0], y + dir[1]
        while grid[y][x] == self.box_marker:
            boxes.append((x, y))
            x, y = x + dir[0], y + dir[1]
        
        if grid[y][x] == self.free_space_marker:
            # move all boxes in direction
            if len(boxes) > 0:
                for box in boxes:
                    box_x, box_y = box
                    box_nx, box_ny = box_x + dir[0], box_y + dir[1]
                    grid[box_ny][box_nx] = self.box_marker
                start_box_x, start_box_y = boxes[0]
                self.grid[start_box_y][start_box_x] = self.free_space_marker
            
            
            # move robot
            rx, ry = robot.pos
            self.grid[ry][rx] = self.free_space_marker
            next_robot_pos = robot.next_pos(move)
            robot.pos = next_robot_pos
            rx, ry = robot.pos
            self.grid[ry][rx] = self.robot_marker

    
    def move_robot(self):
        start_pos = self.find_robot_position()
        r = Robot(start_pos)

        for move in self.moves:
            if move is None or move == '\n':
                continue
            next_robot_pos = r.next_pos(move)
            # if the next move is a wall don't do aything
            if self.pos_is_wall(next_robot_pos):
                # self.print_grid()
                continue
            # if the next move is free space, move the robot there
            elif self.pos_is_free_space(next_robot_pos):
                x, y = r.pos
                self.grid[y][x] = self.free_space_marker
                r.pos = next_robot_pos
                x, y = r.pos
                self.grid[y][x] = self.robot_marker
            # if the next move is a box, move boxes accordingly
            else:
                self.move_boxes(move, r)
            # self.print_grid()
            
        self.print_grid()


    def pos_is_wall(self, pos):
        x, y = pos
        if self.grid[y][x] == self.wall_marker:
            return True
        return False
    
    def pos_is_free_space(self, pos):
        x, y = pos
        if self.grid[y][x] == self.free_space_marker:
            return True
        return False
            

class Robot:
    def __init__(self, pos):
        self.directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
        self.pos = pos

    def next_pos(self, move):
        dir = self.directions[move]
        return (self.pos[0] + dir[0], self.pos[1] + dir[1])
    
    def dir(self, move):
        return self.directions[move]

if __name__ == '__main__':
    grid, moves = parse_input()
    w = Warehouse(grid, moves)
    w.move_robot()
    print(w.calculate_gps_sum())
    

    