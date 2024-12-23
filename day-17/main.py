data = []

with open(0, "r") as f:
    data = f.read().strip()

registers = data.split("\n\n")[0]
instructions = [int(x) for x in data.split("\n\n")[1].split(":")[1].split(",")]
registers = [
    int(registers.split(":")[1].split()[0]) for registers in registers.split("\n")
]


def run(regs):
    ip = 0
    output = []

    while ip < len(instructions):
        instruction = instructions[ip]
        literal = instructions[ip + 1]
        combo = literal if literal < 4 else regs[literal - 4]
        match instruction:
            case 0:
                regs[0] = (int)(regs[0] / pow(2, combo))
            case 1:
                regs[1] = regs[1] ^ literal
            case 2:
                regs[1] = combo % 8
            case 3:
                if regs[0] == 0:
                    ip += 2
                    continue
                ip = combo - 2
            case 4:
                regs[1] = regs[1] ^ regs[2]
            case 5:
                output.append(combo % 8)
            case 6:
                regs[1] = (int)(regs[0] / pow(2, combo))
            case 7:
                regs[2] = (int)(regs[0] / pow(2, combo))

        ip += 2

    return output


def find(a, i):
    if run([a, registers[1], registers[2]]) == instructions:
        return a

    if run([a, registers[1], registers[2]]) == instructions[-i:] or not i:
        for n in range(8):
            find(registers[0] * 8 + n, i + 1)


print("Part 1:", ",".join(str(x) for x in run(registers)))
print("Part 2:", find(2024, 0))
