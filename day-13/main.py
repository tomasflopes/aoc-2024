import numpy as np
import re


data = []

with open(0, 'r') as f:
    data = [line.strip() for line in f.readlines()]


def solve_linear_system(A, B):
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        return -1, -1
    
    A_x = A.copy()
    A_x[:, 0] = B 
    
    A_y = A.copy()
    A_y[:, 1] = B  
    
    det_A_x = np.linalg.det(A_x)
    det_A_y = np.linalg.det(A_y)
    
    x = det_A_x / det_A
    y = det_A_y / det_A
    
    return round(x, 2), round(y, 2)

p1 = 0
p2 = 0
for i in range(0, len(data), 4):
    button_a, button_b, prize = data[i], data[i+1], data[i+2]
    xa, ya = re.findall(r'(\d+)', button_a)
    xb, yb = re.findall(r'(\d+)', button_b)
    res_x, res_y = re.findall(r'(\d+)', prize) 
    res_x, res_y = int(res_x), int(res_y)
    
    A = np.array([[int(xa), int(xb)], [int(ya), int(yb)]])
    B1 = np.array([res_x, res_y])
    B2 = np.array([res_x + 10000000000000, res_y + 10000000000000])

    x, y = solve_linear_system(A, B1)

    valid = True
    if x == -1 and y == -1:
        valid = False
    if x % 1 != 0 or y % 1 != 0:
        valid = False
    if x > 100 or y > 100:
        valid = False

    p1 += x * 3 + y if valid else 0

    # Part 2
    x, y = solve_linear_system(A, B2)

    valid = True
    if x == -1 and y == -1:
        valid = False
    if x % 1 != 0 or y % 1 != 0:
        valid = False

    p2 += x * 3 + y if valid else 0

print("Part 1:", int(p1))
print("Part 2:", int(p2))
