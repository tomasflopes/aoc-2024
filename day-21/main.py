from collections import deque
from itertools import product

data = []

door_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

directional_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

directions = [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]


def solve(string, keypad):
    pos = {}
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] != None:
                pos[keypad[i][j]] = (i, j)

    paths = {}
    for i in pos:
        for j in pos:
            if i == j:
                paths[(i, j)] = ["A"]
                continue
            possible_paths = []
            q = deque([(pos[i], "")])
            optimal = float("inf")
            while q:
                (x, y), path = q.popleft()
                for dx, dy, direction in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        nx < 0
                        or nx >= len(keypad)
                        or ny < 0
                        or ny >= len(keypad[0])
                        or keypad[nx][ny] == None
                    ):
                        continue
                    if keypad[nx][ny] == j:
                        if optimal < len(path) + 1:
                            break

                        optimal = len(path) + 1
                        possible_paths.append(path + direction + "A")
                    else:
                        q.append(((nx, ny), path + direction))
                else:
                    continue
                break
            paths[(i, j)] = possible_paths

    opts = []
    for i in range(len(string)):
        opts.append(paths[(string[i - 1], string[i])])

    return ["".join(x) for x in product(*opts)]


with open(0, "r") as f:
    data = [x.strip() for x in f.readlines()]

p1 = 0
for line in data:
    door_robot = solve(line, door_keypad)
    robot = door_robot
    for _ in range(2):
        possible_robot = []
        for combination in robot:
            possible_robot.extend(solve(combination, directional_keypad))

        m = min([len(x) for x in possible_robot])
        robot = [x for x in possible_robot if len(x) == m]
    p1 += len(robot[0]) * int(line[:-1])

print("Part 1:", p1)
