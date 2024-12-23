data = []

# STEPS = 10
STEPS = 2000


def mix(secret, x):
    return x ^ secret


def prune(x):
    return x % 16777216


def encode(x):
    secret = x
    for i in range(STEPS):
        v = secret * 64
        secret = mix(secret, v)
        secret = prune(secret)
        v = secret // 32
        secret = mix(secret, v)
        secret = prune(secret)
        v = secret * 2048
        secret = mix(secret, v)
        secret = prune(secret)

    return secret


with open(0, "r") as f:
    data = [int(x) for x in f.readlines()]

print("Part 1:", sum(encode(x) for x in data))
