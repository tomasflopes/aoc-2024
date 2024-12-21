data = []

with open(0, "r") as f:
    data = f.read().strip()

registers = data.split("\n\n")[0]
instructions = [int(x) for x in data.split("\n\n")[1].split(":")[1].split(",")]
registers = [
    int(registers.split(":")[1].split()[0]) for registers in registers.split("\n")
]

ip = 0
output = ""

while ip < len(instructions):
    instruction = instructions[ip]
    literal = instructions[ip + 1]
    combo = literal if literal < 4 else registers[literal - 4]
    match instruction:
        case 0:
            registers[0] = (int)(registers[0] / pow(2, combo))
        case 1:
            registers[1] = registers[1] ^ literal
        case 2:
            registers[1] = combo % 8
        case 3:
            if registers[0] == 0:
                ip += 2
                continue
            ip = combo - 2
        case 4:
            registers[1] = registers[1] ^ registers[2]
        case 5:
            output += str(combo % 8) + ","
        case 6:
            registers[1] = (int)(registers[0] / pow(2, combo))
        case 7:
            registers[2] = (int)(registers[0] / pow(2, combo))

    ip += 2

print("Part 1:", output[:-1])
