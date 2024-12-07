from operator import add, mul


FILE = 'input.txt'

data = []
print()

with open(FILE, 'r') as f:
    data = [x.strip() for x in f.readlines()]

def concat(a, b):
    return int(str(a) + str(b))


def solve_p1(numbers, target, ops):
    possible_results = [numbers[0]]

    for i in range(1, len(numbers)):
        for j in range(len(possible_results)):
            for op in ops:
                possible_results.append(op(possible_results[j], numbers[i]))
            
    final_results_count = 2 ** (len(numbers) - 1)
    possible_results = possible_results[-final_results_count:]

    if target in possible_results:
        return target

    return 0
        

def solve_p2(numbers, target, ops):
    if len(numbers) == 1:
        return target == numbers[0]

    for op in ops:
        res = op(numbers[0], numbers[1])
        if solve_p2([res] + numbers[2:], target, ops):
            return target
            
    return 0


p1 = 0
for line in data:
    numbers = [int(x) for x in line.split(":")[1].split()]
    target = int(line.split(":")[0])

    p1 += solve_p1(numbers, target, [add, mul])

print("Part 1: ", p1)

p2 = 0
for line in data:
    numbers = [int(x) for x in line.split(":")[1].split()]
    target = int(line.split(":")[0])

    p2 += solve_p2(numbers, target, [add, mul, concat])

print("Part 2: ", p2)
