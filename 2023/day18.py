with open("input18.txt", "r") as file:
    data = file.read().split("\n")

dirs = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}
dirs_lst = ["R", "D", "L", "U"]

def trench(data, part2=False):
    x, y = 0, 0
    corners = [(x, y)]
    for line in data:
        dir_c, n, color = line.split()
        n = int(n)
        dir = dirs[dir_c]

        if part2:
            color = color[2:-1]
            n, dir = color[:-1], color[-1]
            
            dir = dirs[dirs_lst[int(dir)]]
            n = int(n, base=16)

        x += dir[0] * n
        y += dir[1] * n
        corners.append((x, y))

    perim = 0
    area = 0
    for i in range(len(corners)-1):
        x1, y1 = corners[i]
        x2, y2 = corners[(i+1)%len(corners)]

        area += x1 * y2
        area -= y1 * x2

        perim += abs(x1 - x2) + abs(y1 - y2)

    return abs(area) // 2 + perim // 2 + 1

print("Part 1:", trench(data))
print("Part 2:", trench(data, part2=True))


# My original solution for part 1 (storing perimeter in 2D grid and doing flood fill)

# from collections import defaultdict
# grid = defaultdict(lambda: ".")

# x, y = 0, 0
# grid[(x, y)] = "#"
# for _, line in enumerate(data):
#     dir_c, n, color = line.split()
#     n = int(n)
#     dir = dirs[dir_c]

#     for i in range(n):
#         x, y = x + dir[0], y + dir[1]
#         grid[(x, y)] = "#"

# outline_n = len(grid)

# flooded = set()
# flood = [(1, 1)]
# while flood:
#     cur = flood.pop(0)

#     flooded.add(cur)
#     grid[cur] = "#"

#     if len(flooded) > 100000:
#         print("outside")
#         break

#     for dx, dy in dirs.values():
#         test = (cur[0] + dx, cur[1] + dy)
#         if grid[test] == ".":
#             grid[test] = "#"
#             flood.append(test)

# print(len(flooded) + outline_n)
