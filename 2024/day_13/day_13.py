import re

def get_values(equation):
    numbers = re.findall(r'\d+', equation)
    return [int(num) for num in numbers]

def is_valid_answer(num, tolerance=1e-2):
    if abs(num - round(num)) < tolerance:
        return True 
    else:
        return False

def calculate_equations(machine):
    a, b, prize = machine[0], machine[1], machine[2]
    a_nums, b_nums, prize_nums = get_values(a), get_values(b), get_values(prize)

    """
    example:
    94a + 22b = 8400
    34a + 67b = 5400

    [94 22] [a] = [8400]
    [34 67] [b] = [5400]

    a inverse = (1/ad-bc) * inverse matrix
    answer = a inverse * b
    """
    # part 2 
    prize_nums = [num + 10000000000000 for num in prize_nums]


    inverse_matrix = [[b_nums[1], -b_nums[0]], [-a_nums[1], a_nums[0]]]
    determinant = (1/(a_nums[0]*b_nums[1] - a_nums[1]*b_nums[0]))
    inverse_matrix = [[determinant * val for val in row] for row in inverse_matrix]

    x_pushes = inverse_matrix[0][0] * prize_nums[0] + inverse_matrix[0][1] * prize_nums[1]
    y_pushes = inverse_matrix[1][0] * prize_nums[0] + inverse_matrix[1][1] * prize_nums[1]
    print(x_pushes, y_pushes)
    return x_pushes, y_pushes


def part_1(machines):
    tokens = 0
    for machine in machines:
        a, b = calculate_equations(machine)
        if is_valid_answer(a) and is_valid_answer(b):
            print(machine)
            a, b = int(round(a)), int(round(b))
            tokens += a * 3
            tokens += b
    return tokens







if __name__ == '__main__':
    with open('day_13.input') as f:
        lines = f.read().split("\n\n")
        machines = [line.split("\n") for line in lines]
    f.close()
    print(part_1(machines))