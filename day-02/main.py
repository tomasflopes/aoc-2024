data = []

with open(0, "r") as f:
    data = f.read().splitlines()

safe_levels = 0
part_2_safe_levels = 0


def get_unsafe_index(level):
    for i in range(len(level) - 2):
        if abs(level[i] - level[i + 1]) > 3 or abs(level[i] - level[i + 1]) <= 0:
            return i

        if level[i] > level[i + 1] and level[i + 1] < level[i + 2]:
            return i

        if level[i] < level[i + 1] and level[i + 1] > level[i + 2]:
            return i

    if abs(level[-2] - level[-1]) > 3 or abs(level[-2] - level[-1]) <= 0:
        return len(level) - 2

    return -1


for line in data:
    level = line.split()
    level = [int(x) for x in level]

    unsafe_index = get_unsafe_index(level)

    if unsafe_index == -1:
        safe_levels += 1
        continue

    new_level = level.copy()
    new_level.pop(unsafe_index)

    if get_unsafe_index(new_level) == -1:
        part_2_safe_levels += 1
        continue

    new_level = level.copy()
    new_level.pop(unsafe_index + 1)

    if get_unsafe_index(new_level) == -1:
        part_2_safe_levels += 1
        continue

    level.pop(unsafe_index + 2)
    if get_unsafe_index(level) == -1:
        part_2_safe_levels += 1
        continue


print("Part 1: ", safe_levels)
print("Part 2: ", safe_levels + part_2_safe_levels)
