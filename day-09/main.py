data = []

with open(0, "r") as f:
    data = f.readline().strip()

disk = []
id = 0
is_free_space = True
for c in data:
    n = int(c)
    is_free_space = not is_free_space
    if n == 0: continue

    disk.append("." * n if is_free_space else [id] * n)
    if not is_free_space: id += 1

disk = [item for sublist in disk for item in sublist]
disk_p2 = disk.copy()

j = 0
for i in range(len(disk) - 1, -1, -1):
    while disk[j] != "." and j <= i:
        j += 1
    disk[j] = disk[i]

disk = disk[:j] + ["."] * (len(disk) - j)

dict = {}
empty = []
file = True
id = 0
i = 0
for c in data:
    if file:
        dict[id] = int(c)
        i += int(c)
        file = False
    else:
        empty.append((i, int(c)))
        i += int(c)
        file = True
        id += 1

i = len(disk_p2) - 1
while i >= 0:
    if disk_p2[i] == ".":
        i -= 1
        continue

    length = dict[disk_p2[i]]
    empty_index = next((j for j, (pos, empty_len) in enumerate(empty) if empty_len >= length and pos < i), -1)

    if empty_index != -1:
        k, pos = empty.pop(empty_index)
        for f in range(length):
            disk_p2[k] = disk_p2[i - f]
            disk_p2[i - f] = "."
            k += 1
        if length < pos:
            empty.insert(empty_index, (k, pos - length))
    i -= length

p1 = sum(disk[i] * i for i in range(len(disk)) if disk[i] != ".")
p2 = sum(disk_p2[i] * i for i in range(len(disk_p2)) if disk_p2[i] != ".")

print("Part 1:", p1)
print("Part 2:", p2)
