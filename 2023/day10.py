from collections import defaultdict, Counter
from math import prod

with open("input10.txt", "r") as file:
    data = file.read().split("\n")

def print_grid(grid: dict, end="", default=" "):
    x = [x[0] for x in grid.keys()]
    x = (min(x), max(x))
    y = [x[1] for x in grid.keys()]
    y = (min(y), max(y))

    for i in range(x[0], x[1] + 1):
        for j in range(y[0], y[1] + 1):
            print(str(grid[(i,j)]) if (i,j) in grid else default, end=end)
            # print(grid[(i,j)], end=end)
        print()

grid = defaultdict(lambda: ".")
start = (-1, -1)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
        grid[(i,j)] = char

print(start)
print_grid(grid)

dirs = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}

# for d, dir in dirs.items():
#     test = (start[0] + dir[0], start[1] + dir[1])
#     grid[test] = d

tile_key = {
    # "S": ["N", "S", "E", "W"],
    "S": ["W", "E"],
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
}

visited = set()
queue = [(0, start)]
while queue:
    steps, cur = queue.pop(0)
    if cur in visited:
        continue

    visited.add(cur)

    char = grid[cur]
    if char not in tile_key:
        continue

    adj = tile_key[char]
    # print(steps, cur, char, adj)

    for a in adj:
        dir = dirs[a]

        test = (cur[0] + dir[0], cur[1] + dir[1])

        queue.append((steps+1, test))

print(len(visited))

loop = {k:v for k,v in grid.items() if k in visited}

max_x = max([x[0] for x in grid])
max_y = max([x[1] for x in grid])
print(max_x, max_y)

print_grid(loop)

enclosed = 0
for (x, y), char in grid.items():
    if (x, y) in loop:
        continue

    count = 0

    rx, ry = x, y
    while rx < max_x + 1 and ry < max_y + 1:
        if (rx, ry) in loop and not (grid[(rx, ry)] == "L" or grid[(rx, ry)] == "7"):
            count += 1
        rx += 1
        ry += 1

    if count % 2 == 1:
        enclosed += 1

print(enclosed)

# from queue import PriorityQueue

# flood_visited = set()
# costs = {}
# flood = PriorityQueue()
# flood.put((0, (-1, -1)))

# while not flood.empty():
#     cost, cur = flood.get()

#     if cur in flood_visited:
#         continue

#     if cur[0] < -2 or cur[0] > max_x + 2 or cur[1] < -1 or cur[1] > max_y + 2:
#         continue

#     flood_visited.add(cur)
#     costs[cur] = cost

#     # print(cost, cur, grid[cur])

#     for dir in dirs.values():
#         test = (cur[0] + dir[0], cur[1] + dir[1])

#         char = grid[test]
#         if char in tile_key:
#             price = 1
#         else:
#             price = 0

#         flood.put((cost+price, test))
        
# enclosed = 0
# for p, c in costs.items():
#     if grid[p] == "." and c % 2 == 1:
#         print(p, c)
#         enclosed += 1

# to_draw = {k:v for k, v in costs.items() if grid[k] == "."}
# print(enclosed)
# print_grid(to_draw)
