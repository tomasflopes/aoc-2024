import heapq

data = []
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# SIZE = 7
SIZE = 71
# BYTES = 12
BYTES = 1024


def print_grid(grid, path):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if (i, j) in path:
                print("O", end="")
            elif char == 0:
                print(".", end="")
            elif char == 1:
                print("#", end="")

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
            if nx < 0 or nx >= SIZE or ny < 0 or ny >= SIZE:
                continue

            if grid[nx][ny] == 1 or (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            heapq.heappush(q, (cost + 1, (nx, ny), path + [(nx, ny)]))

    return None


with open(0, "r") as f:
    data = [line.strip().split(",") for line in f.readlines()]
    data = [[int(x) for x in line] for line in data]

grid = [[0] * (SIZE) for _ in range(SIZE)]
for y, x in data[:BYTES]:
    grid[x][y] = 1

start = (0, 0)
end = (SIZE - 1, SIZE - 1)

path = dijkstra(grid, start, end)
# print_grid(grid, path)
print("Part 1:", len(path) - 1)

# Part 2
left = BYTES
right = len(data)

while left < right:
    mid = (left + right) // 2

    grid = [[0] * (SIZE) for _ in range(SIZE)]
    for y, x in data[:mid]:
        grid[x][y] = 1

    path = dijkstra(grid, start, end)
    if not path:
        right = mid
    else:
        left = mid + 1

x, y = data[left - 1]
print("Part 2: " + str(left) + " " + str(x) + "," + str(y))
