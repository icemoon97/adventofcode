from collections import defaultdict, Counter
from math import prod
import itertools
import numpy as np
from ast import literal_eval

def print_grid(grid: dict, end="", default=" "):
    x = [x[0] for x in grid.keys()]
    x = (min(x), max(x))
    y = [x[1] for x in grid.keys()]
    y = (min(y), max(y))

    for i in range(x[0], x[1] + 1):
        for j in range(y[0], y[1] + 1):
            # print(str(grid[(i,j)]) if (i,j) in grid else default, end=end)
            print(grid[(i,j)], end=end)
        print()

with open("input19.txt", "r") as file:
    data = file.read().split("\n\n")

raw_flows, inputs = data

# name -> (dest, var, comp), if var and comp exist
flows = {}

# px{a<2006:qkq,m>2090:A,rfg}
for line in raw_flows.split("\n"):
    name, parts = line.split("{")
    parts = parts.rstrip("}").split(",")
    print(name)

    f = []
    for p in parts:
        if ":" in p:
            comp, dest = p.split(":")
            if ">" in comp:
                var, n = comp.split(">")
                print(">", var, n)
                f.append((dest, var, ">", int(n)))
            elif "<" in comp:
                var, n = comp.split("<")
                print("<", var, n)
                f.append((dest, var, "<", int(n)))
            else:
                print("bad")
        else:
            f.append((p))

    flows[name] = f

print(flows)

def go(flows, d, f):
    print(d, f)
    for p in f:
        # print("p:", p)
        match p:
            case [dest, var, op, n]:
                # print(dest, var)
                print(d[var], op, n)
                if op == "<":
                    ans = d[var] < n
                else:
                    ans = d[var] > n
                print(d[var], op, n, ans)

                if ans:
                    print(dest)
                    if dest in ["A", "R"]:
                        return dest
                    else:
                        return go(flows, d, flows[dest])
                continue
            case dest:
                print(dest)
                if dest in ["A", "R"]:
                    return dest
                else:
                    return go(flows, d, flows[dest])

total = 0
for line in inputs.split("\n"):
    d = {}
    for ele in line[1:-1].split(","):
        var, n = ele.split("=")
        d[var] = int(n)

    f = flows["in"]
    result = go(flows, d, f)
    print("RESULT:", result)

    if result == "A":
        total += sum(d.values())
    
print("part 1:", total)


