import heapq


data = []

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def map_data(data):
    maze = []
    start_pos = None
    for i, line in enumerate(data):
        r = []
        for j, char in enumerate(line):
            if char == "S":
                start_pos = (i, j)
            if char == "E":
                end_pos = (i, j)
            r.append(1 if char == "#" else 0)
        maze.append(r)
    return maze, start_pos, end_pos


def print_maze(maze, visited):
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            print("#" if c == 1 else "@" if (i, j) in visited else ".", end="")
        print()


def path_from_to(maze, start_pos, end_pos):
    q = []
    heapq.heappush(q, (0, [], directions[0], start_pos))

    visited = set()

    while q:
        turns, path, last_direction, current_pos = heapq.heappop(q)

        if current_pos == end_pos:
            return path, turns

        for direction in directions:
            x, y = current_pos
            dx, dy = direction
            nx, ny = x + dx, y + dy

            if (
                nx < 0
                or nx >= len(maze)
                or ny < 0
                or ny >= len(maze[0])
                or maze[nx][ny] == 1
                or (nx, ny) in visited
            ):
                continue

            visited.add((nx, ny))

            heapq.heappush(
                q,
                (
                    (turns + 1 if direction != last_direction else turns),
                    path + [current_pos],
                    direction,
                    (nx, ny),
                ),
            )

    return None, None


with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]

maze, start_pos, end_pos = map_data(data)
path, turns = path_from_to(maze, start_pos, end_pos)
best_score = turns * 1000 + len(path)
print("Part 1:", best_score)

best_paths = set(path)
best_paths.add(start_pos)
best_paths.add(end_pos)

for pos in path:
    x, y = pos
    maze[x][y] = 1
    path, turns = path_from_to(maze, start_pos, end_pos)
    if path:
        score = turns * 1000 + len(path)
        if score == best_score:
            for c in path:
                best_paths.add(c)
    maze[x][y] = 0

print("Part 2:", len(best_paths))
