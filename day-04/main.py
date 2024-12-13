diffs = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, -1), (-1, 0)]
x_diffs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

with open(0, "r") as f:
    data = f.readlines()

def find_xmas_occ(matrix, x, y):
    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])): return 0
    count = 0

    for dx, dy in diffs:
        if all(0 <= x + i * dx < len(matrix) and 0 <= y + i * dy < len(matrix[0]) for i in range(4)):
            if matrix[x][y] == "X" and matrix[x + dx][y + dy] == "M" and matrix[x + 2 * dx][y + 2 * dy] == "A" and matrix[x + 3 * dx][y + 3 * dy] == "S":
                count += 1
    return count


def find_x_occ(matrix, x, y):
    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])) or matrix[x][y] != "A": return 0
    count = 0

    for dx, dy in x_diffs:
        if all(0 <= x + i * dx < len(matrix) and 0 <= y + i * dy < len(matrix[0]) for i in [-1, 1]):
            if matrix[x + dx][y + dy] == "M" and matrix[x - dx][y - dy] == "S": count += 1
    return 1 if count == 2 else 0


count = sum(find_xmas_occ(data, i, j) for i in range(len(data)) for j in range(len(data[i])))
print("Part 1: ", count)

count = sum(find_x_occ(data, i, j) for i in range(len(data)) for j in range(len(data[i])))
print("Part 2: ", count)
