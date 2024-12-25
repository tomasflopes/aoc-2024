with open(0, "r") as f:
    locks = [line.strip().split("\n") for line in f.read().split("\n\n")]

locks_map, keys_map = [], []
for lock in locks:
    l = []
    for j in range(len(lock[0])):
        s = 0
        for i in range(1, len(lock) - 1):
            if lock[i][j] == "#":
                s += 1
        l.append(s)
    if lock[0][0] == "#":
        locks_map.append(l)
    else:
        keys_map.append(l)

p1 = 0
for lock in locks_map:
    for key in keys_map:
        if all(lock[i] + key[i] < 6 for i in range(len(lock))):
            p1 += 1

print("Part 1:", p1)
