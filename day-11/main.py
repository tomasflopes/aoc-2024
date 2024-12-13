from functools import cache


data = []
ITERATIONS_P1, ITERATIONS_P2 = 25, 75

@cache
def count_occ(n, steps):
    if steps == 0:
        return 1
    if n == 0:
        return count_occ(1, steps - 1)
    if len(str(n)) % 2 == 0:
        first_half = int(str(n)[: len(str(n)) // 2])
        second_half = int(str(n)[len(str(n)) // 2 :])
        return count_occ(first_half, steps - 1) + count_occ(second_half, steps - 1)

    return count_occ(n * 2024, steps - 1)


with open(0, "r") as f:
    data = [int(x) for x in f.readline().strip().split()]

p1 = sum(count_occ(x, ITERATIONS_P1) for x in data)
print("Part 1:", p1)
p2 = sum(count_occ(x, ITERATIONS_P2) for x in data)
print("Part 2:", p2)
