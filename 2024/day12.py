
# N, E, S, W
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

from pathlib import Path

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    grid = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            grid[(i,j)] = char


    regions = {}
    all_regions = set()

    part1 = 0
    part2 = 0

    for p in grid:

        if p in all_regions:
            continue

        c = grid[p]
        r = set()
        per = 0

        sides = {d: [] for d in DIRS}

        queue = [p]
        while queue:
            x, y = queue.pop(0)

            if (x, y) in r:
                continue
            r.add((x, y))

            for dx, dy in DIRS:
                test = (x + dx, y + dy)

                if test in grid and grid[test] == c:
                    queue.append(test)
                else:
                    per += 1                            
                    sides[(dx, dy)].append((x, y))
                    
      
        regions[c] = r
        all_regions |= r

        # print(c, per, len(r), r)
        part1 += per * len(r)

        # n_sides = 0
        # DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

        # for d, lst in sides.items():
        #     counted = set()

        #     for potential in lst:
        #         x, y = potential
            
        #         if d == DIRS[0] or d == DIRS[2]:
        #             if not any(x == x1 and abs(y - y1) == 1 for x1, y1 in counted):
        #                 n_sides += 1
        #         elif d == DIRS[1] or d == DIRS[3]:
        #             if not any(y == y1 and abs(x - x1) == 1 for x1, y1 in counted):
        #                 n_sides += 1
        #         counted.add(potential)

        side_count = 0
        for dx, dy in DIRS:
            side = {(x + dx, y + dy) for x, y in r}
            side -= r

            double_count = {(x + dy, y + dx) for x, y in side}

            side_count += len(side - double_count)

        # n_sides2 = 0
        # for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #     side = set()
        #     for xy in r:
        #         temp = xy[0] + d[0], xy[1] + d[1]
        #         if temp not in r:
        #             side.add(temp)
        #     to_remove = set()
        #     for xy in side:
        #         temp = xy[0] + d[1], xy[1] + d[0]
        #         while temp in side:
        #             to_remove.add(temp)
        #             temp = temp[0] + d[1], temp[1] + d[0]
        #     n_sides2 += len(side) - len(to_remove)
        

        part2 += side_count * len(r)

    print(part1)
    print(part2)

if __name__ == "__main__":
    DAY = 12
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")