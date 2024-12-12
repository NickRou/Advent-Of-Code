def part_1(left_numbers, right_numbers):
    if len(left_numbers) != len(right_numbers):
        return

    left_numbers.sort()
    right_numbers.sort()

    total = 0
    for i in range(len(left_numbers)):
        left, right = left_numbers[i], right_numbers[i]
        if left > right:
            total += left - right
        else:
            total += right - left
    return total

def part_2(left_numbers, right_numbers):
    if len(left_numbers) != len(right_numbers):
        return
    
    total = 0
    for i in range(len(left_numbers)):
        left = left_numbers[i]
        same_nums = 0
        for j in range(len(right_numbers)):
            right = right_numbers[j]
            if left == right:
                same_nums += 1
        total += left * same_nums

    return total


if __name__ == '__main__':
    with open('day_01.input') as f:
        lines = f.read().splitlines()
        left_numbers = []
        right_numbers = []
        for line in lines:
            left, right = map(int, line.split())
            left_numbers.append(left)
            right_numbers.append(right)
    f.close()
    print(part_1(left_numbers, right_numbers))
    print(part_2(left_numbers, right_numbers))