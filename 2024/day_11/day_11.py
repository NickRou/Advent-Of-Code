from collections import defaultdict

def process(lst):
    res = []
    for num in lst:
        if num == 0:
            res.append(1)
        elif len(str(num)) % 2 == 0:
            length = len(str(num))
            res.append(int(str(num)[0 : length // 2]))
            res.append(int(str(num)[length // 2 :]))
        else:
            res.append(num * 2024)
    return res

def run(input, iterations):
    d = defaultdict(int)
    for val in input:
        d[int(val)] = 1
    for _ in range(iterations):
        d2 = d.copy()
        for key in list(d):
            if d[key] > 0:
                num = d[key]
                d2[key] -= num
                res = process([key])
                for val in res:
                    d2[val] += num
        print("d2: " + str(d2))
        d = d2.copy()
    return sum(d.values())

input = open("day_11.input").readline().split(" ")
print(run(input, 3))