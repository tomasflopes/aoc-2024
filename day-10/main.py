from collections import defaultdict


data = []

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

trailheads = defaultdict(set)
trailheads_p2 = defaultdict(list)


def walk(i, j, data, origin):
    if data[i][j] == 9:
        trailheads[(i, j)].add(origin)
        trailheads_p2[(i, j)].append(origin)

    for dx, dy in directions:
        x, y = i + dx, j + dy
        if (
            0 <= x < len(data)
            and 0 <= y < len(data[0])
            and data[x][y] - data[i][j] == 1
        ):
            walk(x, y, data, origin)


with open(0, "r") as f:
    data = [[int(x) for x in list(line.strip())] for line in f]

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            walk(i, j, data, (i, j))

print("Part 1:", sum([len(x) for x in trailheads.values()]))
print("Part 2:", sum([len(x) for x in trailheads_p2.values()]))
