from math import prod

with open("input19.txt", "r") as file:
    data = file.read().split("\n\n")

raw_flows, inputs = data

# name -> (dest, var, comp), if var and comp exist
flows = {}

for line in raw_flows.split("\n"):
    name, parts = line.split("{")
    parts = parts.rstrip("}").split(",")

    f = []
    for p in parts:
        if ":" in p:
            comp, dest = p.split(":")
            var, op, n = comp[0], comp[1], comp[2:]
            f.append((dest, var, op, int(n)))
        else:
            f.append((p))

    flows[name] = f

# segs are [inclusive, exclusive)
def go(segs, f_name):
    if f_name == "A":
        return prod(b - a for a, b in segs.values())
    elif f_name == "R":
        return 0

    total = 0

    for p in flows[f_name]:
        match p:
            case [dest, var, op, n]:
                start, end = segs[var]
                
                if op == "<" and start < n:
                    new_segs = segs.copy()
                    new_segs[var] = [start, n]
                    total += go(new_segs, dest)

                    segs[var] = [n, end]
                elif op == ">" and end > n:
                    new_segs = segs.copy()
                    new_segs[var] = [n+1, end]
                    total += go(new_segs, dest)

                    segs[var] = [start, n+1]
                
            case dest:
                total += go(segs, dest)

    return total

print("Part 2:", go({"x": [1, 4001], "m": [1, 4001], "a": [1, 4001], "s": [1, 4001]}, "in"))

# for line in inputs.split("\n"):
#     d = {}
#     for ele in line[1:-1].split(","):
#         var, n = ele.split("=")
#         d[var] = int(n)


