import re


data = []

with open(0, 'r') as f:
    data = f.readlines()
    data = "".join(data)

sum = 0
p = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(p, data)

for match in matches:
    sum += int(match[0]) * int(match[1])

print("Part 1: ", sum)

p = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
matches = re.findall(p, data)

multiply = True
sum = 0

for exp in matches:
    match exp[0]:
        case "do()":
            multiply = True
        case "don't()":
            multiply = False
        case _:
            if multiply:
                sum += int(exp[1]) * int(exp[2])

print("Part 2: ", sum)

