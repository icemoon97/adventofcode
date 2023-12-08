from math import lcm

with open("input08.txt", "r") as file:
    data = file.read().split("\n\n")

seq, node_data = data

nodes = {}
for i, line in enumerate(node_data.split("\n")):
    name, links = line.split(" = ")
    l, r = links[1:-1].split(", ")

    nodes[name] = (l, r)

def walk_path(start, end_condition):
    i = 0
    current = start
    while not end_condition(current):
        dir = seq[i % len(seq)]

        if dir == "L":
            current = nodes[current][0]
        elif dir == "R":
            current = nodes[current][1]
        
        i += 1
    
    return i

print("Part 1:", walk_path("AAA", lambda n: n == "ZZZ"))

starts = [n for n in nodes if n[-1] == "A"]
cycles = [walk_path(n, lambda n: n[-1] == "Z") for n in starts]
print("Part 2:", lcm(*cycles))
