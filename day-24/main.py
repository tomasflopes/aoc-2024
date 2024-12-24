with open(0, "r") as f:
    initial, transitions = [line.split("\n") for line in f.read().split("\n\n")]

values = {}
for line in initial:
    values[line.split(":")[0]] = int(line.split()[1])

transitions_map = []
for line in transitions:
    if line:
        frm, op, to, _, res = line.split()
        transitions_map.append({"from": frm, "to": to, "op": op, "res": res})

seen = set()
while len(seen) < len(transitions_map):
    for transition in transitions_map:
        if (
            transition["from"] not in values
            or transition["to"] not in values
            or transition["res"] in seen
        ):
            continue
        vf, vt = values[transition["from"]], values[transition["to"]]

        if transition["op"] == "AND":
            values[transition["res"]] = vf & vt
        elif transition["op"] == "OR":
            values[transition["res"]] = vf | vt
        elif transition["op"] == "XOR":
            values[transition["res"]] = vf ^ vt

        seen.add(transition["res"])

res = [{value: values[value]} for value in values if value.startswith("z")]

res.sort(key=lambda x: -int(list(x.keys())[0][1:]))
res = [list(x.values())[0] for x in res]
res = int("".join(map(str, res)), 2)

print("Part 1:", res)
