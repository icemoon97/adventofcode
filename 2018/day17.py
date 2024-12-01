from collections import defaultdict

def min_max(l):
    return min(l), max(l)

def parse_ints(s: str):
    s = "".join([c if c.isdigit() or c == "-" else " " for c in s])
    s = [int(x) for x in s.split()]
    return s

data = [line.rstrip("\n") for line in open("input17.txt")]

grid = defaultdict(lambda: " ")

for line in data:
    a, b, c = parse_ints(line)

    if line[0] == "x":
        for i in range(b, c+1):
            grid[(a, i)] = "#"
    else:
        for i in range(b, c+1):
            grid[(i, a)] = "#"

y_bound = min_max([x[1] for x in grid])

print(y_bound)

start = (500, 0)
queue = [start]

def settle(cx, cy, dir):
    while grid[(cx + dir, cy)] != "#":
        cx += dir
        under = grid[(cx, cy + 1)]
        if under == " ":
            queue.append((cx, cy))
            return cx, True
        elif grid[(cx, cy)] == "|" and under == "|":
            return cx, True
    
    return cx, False

while queue:
    cx, cy = queue.pop(0)
    # print(cx, cy)

    if cy > y_bound[1]:
        continue

    if grid[(cx, cy)] in "~":
        continue

    if grid[(cx, cy + 1)] in "#~":
        # look left
        # look right
        left, left_o = settle(cx, cy, -1)
        right, right_o = settle(cx, cy, 1)

        if not left_o and not right_o:
            queue.append((cx, cy - 1))

        for i in range(left, right+1):
            grid[(i, cy)] = "|" if (left_o or right_o) else "~"

    else:
        grid[(cx, cy)] = "|"
        queue.append((cx, cy + 1))


def print_grid(grid):
    x_bound = min_max([x[0] for x in grid])

    for i in range(y_bound[0], y_bound[1]+1):
        for j in range(x_bound[0], x_bound[1]+1):
            print(grid[(j, i)], end="")
        print()
        
print_grid(grid)


tiles = sum(k[1] >= y_bound[0] and k[1] <= y_bound[1] and v in "~|" for k, v in grid.items())
print("Part 1:", tiles)