def is_valid(pos, data, key):
    x, y = pos
    return 0 <= x < len(data) and 0 <= y < len(data[0]) and data[x][y] != key


def draw_map(data, anti_nodes):
    for row in data:
        print("".join("#" if (i, j) in anti_nodes else data[i][j] for j, _ in enumerate(row)))


with open(0, "r") as f:
    data = [x.strip() for x in f.readlines()]

nodes = {}
for i, row in enumerate(data):
    for j, val in enumerate(row):
        if val != ".":
            nodes.setdefault(val, []).append((i, j))

anti_nodes = set()
for key, positions in nodes.items():
    for (x, y) in positions:
        for (i, j) in positions:
            if (x, y) != (i, j):
                dx, dy = x - i, y - j
                v1, v2 = (x + dx, y + dy), (x - dx, y - dy)
                for v in [v1, v2]:
                    if is_valid(v, data, key):
                        anti_nodes.add(v)

print("Part 1:", len(anti_nodes))

anti_nodes.clear()
for key, positions in nodes.items():
    for (x, y) in positions:
        anti_nodes.add((x, y))
        for (i, j) in positions:
            if (x, y) != (i, j):
                dx, dy = x - i, y - j
                v1, v2 = (x + dx, y + dy), (x - dx, y - dy)

                while is_valid(v1, data, key):
                    anti_nodes.add(v1)
                    v1 = (v1[0] + dx, v1[1] + dy)
                while is_valid(v2, data, key):
                    anti_nodes.add(v2)
                    v2 = (v2[0] - dx, v2[1] - dy)

print("Part 2:", len(anti_nodes))
