from collections import defaultdict

data = []

with open(0, "r") as f:
    data = [x.strip().split("-") for x in f.readlines()]

connections = defaultdict(set)
for x, y in data:
    connections[x].add(y)
    connections[y].add(x)

sets = set()
for origin in connections.keys():
    if not origin.startswith("t"):
        continue

    for middle in connections[origin]:
        for destination in connections[middle]:
            if origin in connections[destination]:
                s = set([origin, middle, destination])
                sets.add(tuple(sorted(s)))

print("Part 1:", len(sets))

# Part 2
cliques = set()

for origin in connections.keys():
    clique = set([origin])
    for other in connections[origin]:
        if origin in connections[other]:
            if all(other in connections[member] for member in clique):
                clique.add(other)
    cliques.add(tuple(sorted(clique)))

max_clique = max(cliques, key=lambda x: len(x))
print("Part 2:", ",".join(max_clique))
