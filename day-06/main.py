from collections import defaultdict

data = []

with open(0, "r") as f:
    data = f.readlines()

starting_pos = (0, 0)
for i in range(len(data)):
    data[i] = data[i].strip()

    for c in data[i]:
        if c == "^":
            starting_pos = (i, data[i].index(c))
            break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

current_pos = starting_pos
dir_counter = 0
seen_p1 = set()

while True:
    x, y = current_pos
    seen_p1.add((x, y))

    next_pos = (x + directions[dir_counter][0], y + directions[dir_counter][1])
    if next_pos[0] < 0 or next_pos[0] >= len(data) or next_pos[1] < 0 or next_pos[1] >= len(data[0]): break

    if data[next_pos[0]][next_pos[1]] == "#":
        dir_counter = (dir_counter + 1) % 4

    current_pos = (x + directions[dir_counter][0], y + directions[dir_counter][1])

print("Part 1: ", len(seen_p1))

p2 = 0

matrix = defaultdict(lambda: defaultdict(str))
for i in range(len(data)):
    for j in range(len(data[0])):
        matrix[i][j] = data[i][j]

for i, j in seen_p1:
    x, y = starting_pos
    seen = set()
    dir_counter = 0

    matrix[i][j] = "#"
    while True:
        if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]): break
        if matrix[x][y] == "#":
            x, y = x - directions[dir_counter][0], y - directions[dir_counter][1]
            dir_counter = (dir_counter + 1) % 4
            continue

        if (x, y, directions[dir_counter]) in seen:
            p2 += 1
            break

        seen.add((x, y, directions[dir_counter]))
        x, y = x + directions[dir_counter][0], y + directions[dir_counter][1]

    matrix[i][j] = "."

print("Part 2: ", p2)
