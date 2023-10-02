from helper import *

with open("input15.txt", "r") as file:
	data = file.read().split("\n")

sensors = []

for line in data:
    sx, sy, bx, by = parse_ints(line)

    dist = abs(sx - bx) + abs(sy - by)

    sensors.append((sx, sy, dist))

# returns num of excluded points on given row (can be used for inefficient solution to part 2)
def check_row(y):
    ins = []

    for s in sensors:
        d_line = abs(s[1] - y)
        if s[2] > d_line:
            d_x = abs(d_line - s[2])
            interval = (s[0] + d_x, s[0] - d_x)
            interval = (min(interval), max(interval))

            ins.append((interval[0], 1))
            ins.append((interval[1], -1))

    ins.sort(key=lambda x: (x[0], -x[1]))

    total = 0
    prev = ins[0][0]
    overlap = 1
    for x, change in ins[1:]:
        if overlap > 0:
            total += x - prev

        prev = x
        overlap += change

    return total

def find_distress():
    # slopes created by edge of square of exclusion around each beacon
    pos = set()
    neg = set()

    for sx, sy, d in sensors:
        up = sy + d
        down = sy - d

        pos |= {up - sx, down - sx}
        neg |= {up + sx, down + sx}

    # look for gap of 1 unit between sensor regions
    for slope in pos:
        if slope + 2 in pos:
            m1 = slope + 1
            break
    for slope in neg:
        if slope + 2 in neg:
            m2 = slope + 1
            break

    # return intersect between these two gaps
    y = (m1 + m2) // 2
    return (y - m1) * 4000000 + y

print("Part 1:", check_row(2000000))
print("Part 2:", find_distress())

    