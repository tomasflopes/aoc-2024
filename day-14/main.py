from math import prod
import re


data = []

# WIDTH, HEIGHT = 11, 7
WIDTH, HEIGHT = 101, 103
P1_SECONDS = 100
MIN_P2_LINE_LENGTH = 20
robots = []


def quadrants(grid):
    mid_row = HEIGHT // 2
    mid_col = WIDTH // 2

    sums = [0, 0, 0, 0]

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if row == mid_row or col == mid_col:
                continue

            if row < mid_row and col < mid_col:
                sums[0] += grid[row][col]
            elif row < mid_row and col > mid_col:
                sums[1] += grid[row][col]
            elif row > mid_row and col < mid_col:
                sums[2] += grid[row][col]
            elif row > mid_row and col > mid_col:
                sums[3] += grid[row][col]

    return sums


def print_grid(grid):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(grid[i][j] if grid[i][j] > 0 else ".", end="")
        print()


def check_line(grid):
    for i in range(HEIGHT):
        line_length = 0
        for j in range(WIDTH):
            if grid[i][j] > 0:
                line_length += 1
            else:
                line_length = 0
            if line_length >= MIN_P2_LINE_LENGTH:
                return True

    return False


def grid_on_second(robots, second):
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        y, x, vy, vx = map(int, re.findall(r"-?\d+", robot))
        vy = vy if vy >= 0 else WIDTH + vy
        vx = vx if vx >= 0 else HEIGHT + vx

        ex, ey = ((x + vx * second) % HEIGHT, (y + vy * second) % WIDTH)
        grid[ex][ey] += 1

    return grid


with open(0, "r") as f:
    robots = [line.strip() for line in f.readlines()]


print("Part 1:", prod(quadrants(grid_on_second(robots, P1_SECONDS))))

for i in range(WIDTH * HEIGHT):
    grid = grid_on_second(robots, i)

    if check_line(grid):
        print_grid(grid)
        print("? Possible ? Part 2:", i)
