from helper import *
from collections import deque

with open("input18.txt", "r") as file:
	data = file.read().split("\n")

cubes = set()

for line in data:
    x,y,z = parse_ints(line)
    cubes.add((x,y,z))

def full_surface(cubes):
    surface = 0

    for x,y,z in cubes:
        for offset in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            test = (x + offset[0], y + offset[1], z + offset[2])

            if test not in cubes:
                surface += 1

    return surface

def outer_surface(cubes):
    surface = 0

    upper = tuple([max([x[i] for x in cubes]) + 1 for i in range(3)])
    lower = tuple([min([x[i] for x in cubes]) - 1 for i in range(3)])

    q = deque()
    q.append(lower)
    seen = {lower}

    while q:
        x,y,z = q.popleft()

        for offset in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            test = (x + offset[0], y + offset[1], z + offset[2])

            if test in seen:
                continue
            if any([test[i] > upper[i] for i in range(3)]) or any([test[i] < lower[i] for i in range(3)]):
                continue
            if test in cubes:
                surface += 1
                continue

            q.append(test)
            seen.add(test)

    return surface

print("Part 1:", full_surface(cubes))
print("Part 2:", outer_surface(cubes))

