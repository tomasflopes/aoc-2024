FILE = 'input.txt'

data = []
print()

with open(FILE, 'r') as f:
    data = f.readlines()

ordering_rules = {}

i = 0
for line in data:
    i+=1
    line = line.strip()
    if line == "":
        break
    parts = line.split("|")
    
    if parts[0] not in ordering_rules:
        ordering_rules[parts[0]] = []
   
    ordering_rules[parts[0]].append(parts[1])

pages =[]    
for line in data[i:]:
    pages.append(line.strip().split(","))

sum = 0
for page in pages:
    valid = True
    for n in page:
        if n in ordering_rules:
            for rule in ordering_rules[n]:
                if rule in page[:page.index(n)]:
                    valid = False
                    break
    
    if valid:
        sum += int(page[len(page) // 2])

print("Part 1:", sum)

sum = 0
for page in pages:
    valid = True
    i = 0
    while i < len(page):
        n = page[i]
        if n in ordering_rules:
            for rule in ordering_rules[n]:
                if rule in page[:i]:
                    valid = False
                    j = page.index(rule)
                    page[i], page[i-1] = page[i-1], page[i]
                    i=0
                    break

        i+=1
    
    if not valid:
        print(page)
        sum += int(page[len(page) // 2])

print("Part 2: ", sum)
