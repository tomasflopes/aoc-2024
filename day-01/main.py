with open(0, "r") as f:
  data = [line.split() for line in f.read().splitlines()]

left, right = sorted(map(int, (l for l, _ in data))), sorted(map(int, (r for _, r in data)))

print("Part 1:", sum(abs(l - r) for l, r in zip(left, right)))
print("Part 2:", sum(x * right.count(x) for x in left))
