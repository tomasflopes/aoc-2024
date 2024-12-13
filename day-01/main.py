data = []

with open(0, "r") as f:
    data = f.read().splitlines()

left, right = [], []
for line in data:
    l, r = line.split()

    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

if len(left) != len(right):
    print("lengths of left and right are not the same")
    exit()

# Part 1
diffs = []

for i in range(len(left)):
    diffs.append(abs(left[i] - right[i]))

print("Part 1: ", sum(diffs))

# Part 2
similarity_score = 0
for x in left:
    similarity_score += x * right.count(x)

print("Part 2: ", similarity_score)
