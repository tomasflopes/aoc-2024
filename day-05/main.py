with open(0, "r") as f:
    data = f.readlines()

ordering_rules = {}
i = 0
for line in data:
    i += 1
    line = line.strip()
    if not line: break
    parts = line.split("|")
    ordering_rules.setdefault(parts[0], []).append(parts[1])

pages = [line.strip().split(",") for line in data[i:]]

p1, p2 = 0, 0
for page in pages:
    i, valid = 1, True
    while i < len(page):
        n = page[i]
        if n in ordering_rules:
            for rule in ordering_rules[n]:
                if rule in page[:i]:
                    valid = False
                    j = page.index(rule)
                    page[i], page[j] = page[j], page[i]
                    i = j - 1
                    break
        i += 1

    if valid:
        p1 += int(page[len(page) // 2])
    else:
        p2 += int(page[len(page) // 2])

print("Part 1:", p1)
print("Part 2:", p2)
