from helper import *
from collections import defaultdict

with open("input14.txt", "r") as file:
	data = file.read().split("\n")

grid = defaultdict(lambda: " ")

for line in data:
    coords = line.split("->")

    for i in range(1, len(coords)):
        x1, y1 = parse_ints(coords[i-1])
        x2, y2 = parse_ints(coords[i])

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(y,x)] = "#"

source = (0, 500)
bottom = max([x[0] for x in grid.keys()]) + 2

def calc_next(grid, sand, part2=True):
    if part2 and sand[0] + 1 >= bottom:
        return sand, False

    for dir in [(1,0), (1,-1), (1,1)]:
        test = (sand[0] + dir[0], sand[1] + dir[1])
        if grid[test] == " ":
            return test, True

    return sand, False

def drop_sand(grid, source, part2=True):
    sand = source
    sand, changed = calc_next(grid, sand, part2=part2)

    if part2 and not changed:
        return False

    while changed:
        sand, changed = calc_next(grid, sand, part2=part2)

        if sand[0] > bottom:
            return False

    grid[sand] = "o"
    return True

def count_sand(part2=True):
    g = grid.copy()

    count = 0
    while drop_sand(g, source, part2=part2):
        count += 1

    return count

print("Part 1:", count_sand(part2=False))
print("Part 2:", count_sand() + 1)