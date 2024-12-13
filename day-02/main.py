with open(0, "r") as f:
  data = [[int(x) for x in line.split()] for line in f.read().splitlines()]


def get_unsafe_index(level):
  for i in range(len(level) - 2):
    if abs(level[i] - level[i + 1]) > 3 or level[i] == level[i + 1]:
      return i
    if level[i] > level[i + 1] < level[i + 2] or level[i] < level[i + 1] > level[i + 2]:
      return i
  return len(level) - 2 if abs(level[-2] - level[-1]) > 3 or level[-2] == level[-1] else -1


safe_levels = sum(get_unsafe_index(level) == -1 for level in data)
part_2_safe_levels = sum(any(get_unsafe_index(level[:i] + level[i + 1:]) == -1 for i in range(len(level))) 
                      for level in data if get_unsafe_index(level) != -1)

print("Part 1: ", safe_levels)
print("Part 2: ", safe_levels + part_2_safe_levels)
