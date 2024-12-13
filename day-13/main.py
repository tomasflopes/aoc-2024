import numpy as np
import re


data = []
PART_2_OFFSET = 10000000000000

with open(0, 'r') as f:
    data = [line.strip() for line in f.readlines()]

def is_valid_part1(x, y):
    return not (x == -1 and y == -1 or x % 1 != 0 or y % 1 != 0 or x > 100 or y > 100)


def is_valid_part2(x, y):
    return not (x == -1 and y == -1 or x % 1 != 0 or y % 1 != 0)


def solve_linear_system(A, B):
    try:
        solution = np.linalg.solve(A, B)
        return np.around(solution, 2)
    except np.linalg.LinAlgError:
        return -1, -1


p1 = 0
p2 = 0
for i in range(0, len(data), 4):
    xa, ya, xb, yb, res_x, res_y = map(int, re.findall(r"(\d+)", "".join(data[i:i+3])))
    
    A = np.array([[xa, xb], [ya, yb]])
    B1 = np.array([res_x, res_y])
    B2 = np.array([res_x + PART_2_OFFSET, res_y + PART_2_OFFSET])

    x, y = solve_linear_system(A, B1)
    if is_valid_part1(x, y):
        p1 += x * 3 + y

    x, y = solve_linear_system(A, B2)
    if is_valid_part2(x, y):
        p2 += x * 3 + y

print("Part 1:", int(p1))
print("Part 2:", int(p2))
