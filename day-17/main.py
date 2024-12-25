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
    a, b, c = regs

    while ip < len(instructions):
        instruction = instructions[ip]
        literal = instructions[ip + 1]
        combo = (
            literal if literal < 4 else a if literal == 4 else b if literal == 5 else c
        )
        match instruction:
            case 0:
                a >>= combo
            case 1:
                b = b ^ literal
            case 2:
                b = combo % 8
            case 3:
                if a == 0:
                    ip += 2
                    continue
                ip = combo - 2
            case 4:
                b = b ^ c
            case 5:
                output.append(combo % 8)
            case 6:
                b = a >> combo
            case 7:
                c = a >> combo

        ip += 2

    return output


print("Part 1:", ",".join(str(x) for x in run(registers)))


# Part 2
# Program: 2,4,1,1,7,5,1,5,4,0,0,3,5,5,3,0
# do
#   b = a % 8     2,4
#   b = b ^ 1     1,1
#   c = a >> b    7,5
#   b = b ^ 5     1,5
#   b = b ^ c     4,0
#   a = a >> 3    0,3
#   out b % 8     5,5
# while a != 0    3,0


def find(instructions, ans):
    if instructions == []:
        return ans

    for k in range(8):
        a = ans << 3 | k
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ 5
        b = b ^ c
        if b % 8 != instructions[-1]:
            continue
        subprogram = find(instructions[:-1], a)
        if subprogram is not None:
            return subprogram


print("Part 2:", find(instructions, 0))
