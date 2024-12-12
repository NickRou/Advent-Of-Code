def is_line_safe(line: list[int]) -> bool:
    increasing = all(line[i] < line[i+1] and line[i+1] - line[i] <= 3 for i in range(len(line) - 1))
    decreasing = all(line[i] > line[i+1] and line[i] - line[i+1] <= 3 for i in range(len(line) - 1))
    return increasing or decreasing

def can_be_safe(line: list[int]) -> bool:
    for i in range(len(line)):
        num = line[i]
        new_line = line.copy()
        new_line.remove(num)
        if is_line_safe(new_line):
            return True
    return False


def part_1(lines):
    safe_reports = 0
    for line in lines:
        line = list(map(int, line))
        if is_line_safe(line):
            safe_reports += 1
        
    return safe_reports

def part_2(lines):
    safe_reports = 0
    for line in lines:
        line = list(map(int, line))
        if is_line_safe(line):
            safe_reports += 1
        elif can_be_safe(line):
            safe_reports += 1
        
    return safe_reports


if __name__ == '__main__':
    with open('day_02.input') as f:
        lines = f.read().splitlines()
        lines = [line.split() for line in lines]
    f.close()
    print(part_1(lines))
    print(part_2(lines))