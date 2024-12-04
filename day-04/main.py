import re


FILE = 'input.txt'
diffs = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, -1), (-1, 0)] 
x_diffs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

data = []
print()

with open(FILE, 'r') as f:
    data = f.readlines()


def find_xmas_occ(matrix, x, y):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return 0
    
    count = 0
    for diff in diffs:
        dx, dy = diff
        if x + 3 * dx < 0 or y + 3 * dy < 0 or x + 3 * dx >= len(matrix) or y + 3 * dy >= len(matrix[0]):
            continue
        if matrix[x][y] == 'X' and matrix[x + dx][y + dy] == 'M' and matrix[x + 2 * dx][y + 2 * dy] == 'A' and matrix[x + 3 * dx][y + 3 * dy] == 'S':
            count += 1

    return count


def find_x_occ(matrix, x, y):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return 0
    
    count = 0
    
    if matrix[x][y] != 'A':
        return 0

    mas_count = 0
    for diff in x_diffs:
        dx, dy = diff
        if x + dx < 0 or y + dy < 0 or x + dx >= len(matrix) or y + dy >= len(matrix[0]) or x - dx < 0 or y - dy < 0 or x - dx >= len(matrix) or y - dy >= len(matrix[0]):
            continue

        if matrix[x + dx][y + dy] == 'M' and matrix[x-dx][y-dy] == 'S':
            mas_count += 1

    if mas_count == 2:
        return 1
        
    return 0


count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        count += find_xmas_occ(data, i, j)

print("Part 1: ", count)

count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        count += find_x_occ(data, i, j)

print("Part 2: ", count)

# 2035 high
