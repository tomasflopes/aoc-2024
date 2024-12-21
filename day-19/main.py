from functools import cache

with open(0, "r") as f:
    towels, _, *patterns = [x.strip().split(", ") for x in f.readlines()]


@cache
def is_possible(pattern):
    res = 0
    if pattern == "":
        res = 1

    for towel in towels:
        if pattern.startswith(towel):
            res += is_possible(pattern[len(towel) :])

    return res


print("Part 1:", sum(1 if is_possible(pattern[0]) > 0 else 0 for pattern in patterns))
print("Part 2:", sum(is_possible(pattern[0]) for pattern in patterns))
