from collections import defaultdict

with open("input14.txt", "r") as file:
    data = file.read().split("\n")

grid = defaultdict(lambda: "#")
rocks = []

dim = (len(data), len(data[0]))

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "O":
            rocks.append((i, j))
            grid[(i,j)] = "."
        else:
            grid[(i,j)] = char

def tilt(grid, dir, rocks):
    # sort rocks so we move them in the correct order
    rocks.sort(key=lambda r: r[0] * -dir[0] + r[1] * -dir[1])

    temp = grid.copy()
    next = []

    for x, y in rocks:
        i = 0
        while temp[(x + dir[0] * (i+1), y + dir[1] * (i+1))] == ".":
            i += 1

        r = (x + dir[0] * i, y + dir[1] * i)
        temp[r] = "O"
        next.append(r)

    return next

def load(rocks):
    return sum(dim[0] - x for x, _ in rocks)

part1 = tilt(grid, (-1, 0), rocks)
print("Part 1:", load(part1))

def cycle(grid, rocks):
    for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        rocks = tilt(grid, d, rocks)

    return rocks

# state -> last seen
history = {}
# simulate until we find a cycle
for i in range(1000):
    rocks = cycle(grid, rocks)

    state = str(rocks)
    if state in history:
        # print("repeat!", i - history[state])
        cycle_len = i - history[state]
        remaining = (1000000000 - i - 1) % cycle_len
        
        for _ in range(remaining):
            rocks = cycle(grid, rocks)
        
        break

    history[state] = i

print("Part 2:", load(rocks)) 