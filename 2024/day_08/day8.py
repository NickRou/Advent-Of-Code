class Utils:
    @staticmethod
    def parse_input(filename):
        with open(filename) as f:
            grid = f.read().splitlines()
        f.close()
        return grid
    

class Day8:
    def __init__(self, grid):
        self.grid = grid
        self.antennas = {}
        self.antenna_pairs = {}
        self.antinodes = set()

    def add_antenna(self, antenna, x, y):
        if antenna not in self.antennas:
            self.antennas[antenna] = [(x, y)]
        else:
            self.antennas[antenna].append((x, y))

    def add_antenna_pair(self, antenna, coordinates):
        if antenna not in self.antenna_pairs:
            self.antenna_pairs[antenna] = [coordinates]
        else:
            self.antenna_pairs[antenna].append(coordinates)

    def coordinates_in_range(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def part1(self): 
        # build map of antennas
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] != '.':
                    self.add_antenna(self.grid[x][y], x, y)
        
        # get antenna pairs
        for antenna in self.antennas:
            coordinates = self.antennas[antenna]
            for i in range(len(coordinates)-1):
                for j in range(i+1, len(coordinates)):
                    self.add_antenna_pair(antenna, (coordinates[i], coordinates[j]))

        # build antinodes
        for antenna in self.antenna_pairs:
            coordinate_pairs = self.antenna_pairs[antenna]
            for coordinate_pair in coordinate_pairs:
                x1, y1 = map(int, coordinate_pair[0])
                x2, y2 = map(int, coordinate_pair[1])

                x_diff = x2 - x1
                y_diff = y2 - y1

                antinode1 = (x1 - x_diff, y1 - y_diff)
                antinode2 = (x2 + x_diff, y2 + y_diff)

                if self.coordinates_in_range(antinode1[0], antinode1[1]):
                    self.antinodes.add(antinode1)
                if self.coordinates_in_range(antinode2[0], antinode2[1]):
                    self.antinodes.add(antinode2)

        return len(self.antinodes)
    
    def part2(self): 
        count = 0
        original = 0
        # build map of antennas
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] != '.':
                    original += 1
                    self.add_antenna(self.grid[x][y], x, y)
        
        # get antenna pairs
        for antenna in self.antennas:
            coordinates = self.antennas[antenna]
            for i in range(len(coordinates)-1):
                for j in range(i+1, len(coordinates)):
                    self.add_antenna_pair(antenna, (coordinates[i], coordinates[j]))

        # build antinodes
        for antenna in self.antenna_pairs:
            coordinate_pairs = self.antenna_pairs[antenna]
            for coordinate_pair in coordinate_pairs:
                x1, y1 = map(int, coordinate_pair[0])
                x2, y2 = map(int, coordinate_pair[1])
                x_diff = x2 - x1
                y_diff = y2 - y1

                while True:
                    antinode1 = (x1 - x_diff, y1 - y_diff)
                    antinode2 = (x2 + x_diff, y2 + y_diff)

                    antinode1Valid = self.coordinates_in_range(antinode1[0], antinode1[1])
                    antinode2Valid = self.coordinates_in_range(antinode2[0], antinode2[1])

                    if not antinode1Valid and not antinode2Valid:
                        break
                    else:
                        x1, y1 = antinode1
                        x2, y2 = antinode2
                        if antinode1Valid:
                            self.antinodes.add(antinode1)
                        if antinode2Valid:
                            self.antinodes.add(antinode2)

        for i in range(len(self.grid)):
            self.grid[i] = list(self.grid[i])
            
        for antinode in self.antinodes:
            if self.grid[antinode[0]][antinode[1]] == '.':
                count += 1
                self.grid[antinode[0]][antinode[1]] = '#'

        for line in self.grid:
            print(''.join(line))

        return count + original















if __name__ == "__main__":
    grid = Utils.parse_input('day8.input')
    day8 = Day8(grid)
    print(day8.part1())
    day8_part2 = Day8(grid)
    print(day8_part2.part2())