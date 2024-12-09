FILE = 'test.txt'

data = []
print()

with open(FILE, 'r') as f:
    data = f.readline().strip()

disk = []
id = 0
is_free_space = True
for c in data:
    n = int(c)
    is_free_space = not is_free_space
    if n == 0:
        continue
    if is_free_space:
        disk.append("." * n)
        continue
    disk.append([id] * n)
    id += 1

disk = [item for sublist in disk for item in sublist]
disk_p2 = disk.copy()
    
j = 0
for i in range(len(disk) - 1, -1, -1):
    while disk[j] != '.' and j <= i:
        j += 1

    disk[j] = disk[i]

disk = disk[:j] + ['.'] * (len(disk) - j)
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
    empty_index = -1
    for j, element in enumerate(empty):
        pos, empty_len = element
        if empty_len >= length and pos < i:
            empty_index = j
            break
    if empty_index != -1:
        k, pos = empty.pop(empty_index)
        for f in range(length):
            disk_p2[k] = disk_p2[i - f]
            disk_p2[i - f] = "."
            k += 1
        if length < pos:
            empty.insert(empty_index, (k, pos-length))
    i -= length

p1, p2 = 0, 0
for i in range(len(disk)):
    if disk[i] != '.':
        p1 += disk[i] * i
    if disk_p2[i] != '.':
        p2 += disk_p2[i] * i

print("Part 1:", p1)
print("Part 2:", p2)

