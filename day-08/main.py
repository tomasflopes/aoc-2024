data = []


def is_valid(pos, data, key):
    x, y = pos
    return (
        x >= 0 and x < len(data) and y >= 0 and y < len(data[0]) and data[x][y] != key
    )


def draw_map(data, anti_nodes):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in anti_nodes:
                print("#", end="")
            else:
                print(data[i][j], end="")
        print()


with open(0, "r") as f:
    data = [x.strip() for x in f.readlines()]

nodes = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != ".":
            if data[i][j] not in nodes:
                nodes[data[i][j]] = [(i, j)]
            else:
                nodes[data[i][j]].append((i, j))

anti_nodes = set()
for key in nodes:
    numbers = nodes[key]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            x, y = numbers[i]
            dx, dy = (x - numbers[j][0], y - numbers[j][1])
            v1 = (x + dx, y + dy)
            v2 = (x - dx, y - dy)

            if is_valid(v1, data, key):
                anti_nodes.add(v1)
            if is_valid(v2, data, key):
                anti_nodes.add(v2)

print("Part 1:", len(anti_nodes))

anti_nodes = set()
for key in nodes:
    numbers = nodes[key]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            x, y = numbers[i]
            anti_nodes.add((x, y))
            dx, dy = (x - numbers[j][0], y - numbers[j][1])
            v1 = (x + dx, y + dy)
            v2 = (x - dx, y - dy)

            while is_valid(v1, data, key):
                anti_nodes.add(v1)
                v1 = (v1[0] + dx, v1[1] + dy)
            while is_valid(v2, data, key):
                anti_nodes.add(v2)
                v2 = (v2[0] - dx, v2[1] - dy)

print("Part 2:", len(anti_nodes))
