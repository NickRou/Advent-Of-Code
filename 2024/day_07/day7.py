from itertools import product

class Utils:
    @staticmethod
    def parse_input(filename):
        with open(filename) as f:
            lines = f.read().splitlines()
        f.close()
        
        for i in range(len(lines)):
            lines[i] = lines[i].split(': ')
        return lines


class Day7:
    def __init__(self, lines):
        self.lines = lines
        self.possible_opereators = ['+', '*', '||']

    def calculate(self, values, operators):
        total = 0
        for i in range(len(values)-1):
            val1, val2 = values[i], values[i+1]
            operator = operators[i]
            if operator == '+':
                total = val1 + val2 if total == 0 else total + val2
            elif operator == '*':
                total = val1 * val2 if total == 0 else total * val2
            elif operator == '||':
                total = int(str(val1) + str(val2)) if total == 0 else int(str(total) + str(val2))
        return total

    def check_equation(self, target_total, values):
        num_operators = len(values) - 1
        operator_combos = list(product(self.possible_opereators, repeat=num_operators))
        for operator_combo in operator_combos:
            equation_result = self.calculate(values, operator_combo)
            if equation_result == target_total:
                return True
        return False


    def get_total_calibration_result(self):
        calibration_result = 0
        for line in self.lines:
            target_total = int(line[0])
            values = [int(i) for i in line[1].split(' ')]
            if self.check_equation(target_total, values):
                calibration_result += target_total
        return calibration_result






if __name__ == '__main__':
    lines = Utils.parse_input('day7.input')
    part1 = Day7(lines).get_total_calibration_result()
    print("Part 1: ", part1)