from collections import defaultdict

data = []

# STEPS = 10
STEPS = 2000


def mix(secret, x):
    return x ^ secret


def prune(x):
    return x % 16777216


buyers = []


def encode(x):
    buyer = [x % 10]
    secret = x
    for _ in range(STEPS):
        v = secret * 64
        secret = mix(secret, v)
        secret = prune(secret)
        v = secret // 32
        secret = mix(secret, v)
        secret = prune(secret)
        v = secret * 2048
        secret = mix(secret, v)
        secret = prune(secret)
        buyer.append(secret % 10)

    buyers.append(buyer)

    return secret


with open(0, "r") as f:
    data = [int(x) for x in f.readlines()]

print("Part 1:", sum(encode(x) for x in data))

# Part 2
sequence_score = defaultdict(int)

for buyer in buyers:
    seen = set()
    for i in range(len(buyer) - 4):
        seq = []
        for j in range(i, i + 4):
            seq.append(buyer[j + 1] - buyer[j])
        seq = tuple(seq)
        if seq in seen:
            continue
        seen.add(seq)
        sequence_score[seq] += buyer[i + 4]

print("Part 2:", max(sequence_score.values()))
