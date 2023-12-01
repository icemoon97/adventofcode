input_file = "input23.txt"
# input_file = "input23test.txt"
data = [line.rstrip("\n") for line in open(input_file, "r")]

bots = []
for line in data:
    pos = tuple(int(x) for x in line[line.index("<")+1:line.index(">")].split(","))
    r = int(line[line.index("r=")+2:])

    bots.append((pos, r))

strong = max(bots, key=lambda x: x[1])

def dist(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

# count = 0
# for b in bots:
#     d = dist(strong[0], b[0])
#     if d <= strong[1]:
#         count += 1

# print("Part 1:", count)

import itertools
from tqdm import tqdm

def all_points_in_range(r):
    for x in range(r + 1):
        for y in range(r - x + 1):
            for z in range(r - (x + y) + 1):
                yield (x, y, z)
                # will return duplicates if x, y, or z == 0
                # but whatever seems negligible
                yield (-x, y, z)
                yield (x, -y, z)
                yield (x, y, -z)
                yield (-x, -y, z)
                yield (-x, y, -z)
                yield (x, -y, -z)
                yield (-x, -y, -z)
                

offset = (0, 0, 0)
divisor = int(1e6) 

while divisor > 0:
    print("divisor:", divisor)

    shrunk_bots = [(tuple(n // divisor for n in p), r // divisor) for p, r in bots]
    # print(shrunk_bots)

    # search_range = range(-20, 20)
    best = (0, float("inf"), (0, 0)) # overlaps, dist to center, best_pos

    for pos in tqdm(all_points_in_range(50)):
        pos = (pos[0] + offset[0], pos[1] + offset[1], pos[2] + offset[2])
        overlaps = sum(dist(pos, b_pos) <= r for b_pos, r in shrunk_bots)
        to_center = dist(pos, (0,0,0))

        if overlaps > best[0]:
            best = (overlaps, to_center, pos)
        elif overlaps == best[0] and to_center < best[1]:
            best = (overlaps, to_center, pos)

    print(best)

    offset = tuple(o * 10 + bp for o, bp in zip(offset, best[2]))
    print("new offset:", offset)

    divisor //= 10
    

# 776 bots
# best = (2298619, 1871368, 2555502)
# overlaps = sum(dist(best, b_pos) <= r for b_pos, r in bots)

# print(overlaps)
# print(dist(best, (0,0,0)))

# 4181975 is too low
# 6725489 is too low