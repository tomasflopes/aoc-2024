data = []

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()
regions = []

with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]


def flood_fill(start, data):
    q = [start]
    region = set()

    while q:
        x, y = q.pop()
        if (x, y) in visited: continue

        visited.add((x, y))
        region.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and (nx, ny) not in visited and data[nx][ny] == data[x][y]:
                q.append((nx, ny))

    return region


def perimeter_diff(region):
    count = 0

    for x, y in region:
        if (x - 1, y) in region:
            if (x, y - 1) not in region and (x - 1, y - 1) not in region: count += 1
            if (x, y + 1) not in region and (x - 1, y + 1) not in region: count += 1

        if (x, y - 1) in region:
            if (x - 1, y) not in region and (x - 1, y - 1) not in region: count += 1
            if (x + 1, y) not in region and (x + 1, y - 1) not in region: count += 1

    return count


def perimeter(region, data):
    perimeter = 0

    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(data) and 0 <= ny < len(data[0])) or data[nx][ny] != data[x][y]:
                perimeter += 1

    return perimeter


for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) not in visited:
            region = flood_fill((i, j), data)
            regions.append(region)

p1 = sum(len(region) * perimeter(region, data) for region in regions)
print("Part 1:", p1)

p2 = sum(len(region) * (perimeter(region, data) - perimeter_diff(region)) for region in regions)
print("Part 2:", p2)
