data = []


directions = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}

expansions = {"#": "##", "O": "[]", ".": "..", "@": "@."}


def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end="")
        print()


def apply_move_p1(grid, start_pos, direction):
    x, y = start_pos
    dx, dy = direction

    move = True
    nx, ny = x, y
    moves = []
    while True:
        nx, ny = nx + dx, ny + dy
        obj = grid[nx][ny]
        if obj == "#":
            move = False
            break
        if obj == ".":
            break
        if obj == "O":
            moves.append((nx, ny))

    if not move:
        return grid, start_pos

    grid[x][y] = "."
    grid[x + dx][y + dy] = "@"
    for mx, my in moves:
        grid[mx + dx][my + dy] = "O"

    return grid, (x + dx, y + dy)


def apply_move_p2(grid, start_pos, direction):
    x, y = start_pos
    dx, dy = direction

    move = True
    nx, ny = x, y
    moves = [(x, y)]
    for ox, oy in moves:
        nx, ny = ox + dx, oy + dy
        if (nx, ny) in moves:
            continue
        obj = grid[nx][ny]
        if obj == "#":
            move = False
            break
        if obj == "[":
            moves.append((nx, ny))
            moves.append((nx, ny + 1))
        if obj == "]":
            moves.append((nx, ny))
            moves.append((nx, ny - 1))

    if not move:
        return grid, start_pos

    ggrid = [list(row) for row in grid]
    grid[x][y] = "."
    grid[x + dx][y + dy] = "@"
    for mx, my in moves[1:]:
        grid[mx][my] = "."

    for mx, my in moves[1:]:
        grid[mx + dx][my + dy] = ggrid[mx][my]

    return grid, (x + dx, y + dy)


def directions_to_vectors(dirs):
    return [directions[dir] for dir in dirs]


def grid_score(grid, c):
    s = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == c:
                s += i * 100 + j

    return s


with open(0, "r") as f:
    data = [line.strip() for line in f.readlines()]

empty_line = 0
start_pos = None
for i, line in enumerate(data):
    if line == "":
        empty_line = i
        break
    for j, char in enumerate(line):
        if char == "@":
            start_pos = (i, j)

grid = [list(row) for row in data[:empty_line]]
dirs = directions_to_vectors("".join(data[empty_line + 1 :]))

current_grid = grid
current_pos = start_pos
for direction in dirs:
    current_grid, current_pos = apply_move_p1(current_grid, current_pos, direction)

print("Part 1:", grid_score(current_grid, "O"))

# Part 2
current_grid = [list(row) for row in data[:empty_line]]
current_grid = [list("".join(expansions[c] for c in line)) for line in current_grid]
for i in range(len(current_grid)):
    for j in range(len(current_grid[i])):
        if current_grid[i][j] == "@":
            current_pos = (i, j)

for direction in dirs:
    current_grid, current_pos = apply_move_p2(current_grid, current_pos, direction)

print("Part 2:", grid_score(current_grid, "["))
