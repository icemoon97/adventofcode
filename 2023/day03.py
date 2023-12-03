from collections import defaultdict

with open("input03.txt", "r") as file:
    data = file.read().split("\n")

grid = defaultdict(lambda: ".")
for i, line in enumerate(data):
    for j, char in enumerate(line):
        grid[(i, j)] = char

part1 = 0
gears = defaultdict(list)

for i, line in enumerate(data):
    for j, char in enumerate(line):

        if not char.isdigit() or grid[(i, j-1)].isdigit():
            continue

        end = j+1
        while grid[(i, end)].isdigit():
            end += 1
        num = int(line[j:end])
        
        part_num = False
        # check bounding box around number
        for x in range(i-1, i+2):
            for y in range(j-1, end+1):
                s = grid[(x, y)]
                if not (s.isdigit() or s == "."):
                    part_num = True

                if s == "*":
                    gears[(x, y)].append(num)

        if part_num:
            part1 += num

print("Part 1:", part1)

part2 = 0
for adj in gears.values():
    if (len(adj)) == 2:
        part2 += adj[0] * adj[1]

print("Part 2:", part2)
