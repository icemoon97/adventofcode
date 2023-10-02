from helper import *
from queue import PriorityQueue

with open("input12.txt", "r") as file:
	data = file.read().split("\n")

grid = read_grid(data)

def b_search(start):
    searched = {start}
    best = {k: 9999999999999 for k in grid}

    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        steps, cur = q.get()

        best[cur] = steps

        for test in get_neighbors4(grid, cur):
            if test in searched:
                continue

            if ord(grid[cur]) <= ord(grid[test]) + 1:
                q.put((steps + 1, test))
                searched.add(test)

    return best

for p in grid:
    if grid[p] == "S":
        start = p
        grid[p] = "a"
    elif grid[p] == "E":
        end = p
        grid[p] = "z"

shortest = b_search(end)

print("Part 1:", shortest[start])
print("Part 2:", min([shortest[p] for p in grid if grid[p] == "a"]))




# def search(start, end):
#     searched = {start}

#     q = PriorityQueue()
#     q.put((0, start))

#     while not q.empty():
#         steps, pos = q.get()

#         if pos == end:
#             return steps

#         for test in get_neighbors4(grid, pos):
#             if test in searched:
#                 continue

#             if ord(grid[test]) <= ord(grid[pos]) + 1:
#                 q.put((steps + 1, test))
#                 searched.add(test)

#     return 999999999999

# print("Part 1:", search(start, end))

# best = 99999999999
# for pos, char in grid.items():
#     if char == "a":
#         steps = search(pos, end)
#         best = min(steps, best)
# print("Part 2:", best)
