import heapq


data = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# GOOD_CHEAT = 40
GOOD_CHEAT = 100

with open(0, "r") as f:
    data = [x.strip() for x in f.readlines()]

start_pos = (0, 0)
end_pos = (0, 0)
grid = [[0] * (len(data)) for _ in range(len(data[0]))]


def print_grid(grid, path=[]):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if (i, j) in path:
                print("O", end="")
            elif char == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()


def dijkstra(grid, start, end):
    q = []
    heapq.heappush(q, (0, start, [start]))
    visited = set()

    while q:
        cost, current, path = heapq.heappop(q)

        if current == end:
            return path

        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                continue

            if grid[nx][ny] == 1 or (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            heapq.heappush(q, (cost + 1, (nx, ny), path + [(nx, ny)]))

    return None


for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "S":
            start_pos = (i, j)
        elif char == "E":
            end_pos = (i, j)
        elif char == "#":
            grid[i][j] = 1

path = dijkstra(grid, start_pos, end_pos)

good_cheats = []
for i, (x, y) in enumerate(path):
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
            continue

        if (nx, ny) in path:
            index = path.index((nx, ny))
            diff = index - i - 2
            if diff >= GOOD_CHEAT:
                good_cheats.append({"to": (nx, ny), "from": (x, y), "diff": diff})

print(good_cheats)
print("Part 1:", len(good_cheats))
