from collections import defaultdict
from copy import deepcopy

with open("input22test.txt", "r") as file:
# with open("input22.txt", "r") as file:
    data = file.read().split("\n")

bricks = []
# z level -> dict of {brick id -> rect bound}
z_slices = defaultdict(dict)

for i, line in enumerate(data):
    b1, b2 = line.split("~")
    x1, y1, z1 = [int(x) for x in b1.split(",")]
    x2, y2, z2 = [int(x) for x in b2.split(",")]

    assert x1 <= x2 and y1 <= y2 and z1 <= z2

    bricks.append(((x1, y1, z1), (x2, y2, z2)))
    for z in range(z1, z2+1):
        z_slices[z][i] = (x1, y1, x2, y2)

# sort bricks by lower z coord so they fall properly
bricks.sort(key=lambda b: b[0][2])

def rect_intersect(rect1, rect2):
    return not (rect1[0] > rect2[2] or rect1[2] < rect2[0] or rect1[1] > rect2[3] or rect1[3] < rect2[1])

def slice_clear(slice, b_rect, ignore=-1):
    for other_id, r in slice.items():
        if other_id == ignore:
            continue
        if rect_intersect(r, b_rect):
            return False
    return True
    
def settle(bricks, z_slices, ignore=-1):
    for i, b in enumerate(bricks):
        if i == ignore:
            continue

        (x1, y1, z1), (x2, y2, z2) = b

        test = z1
        while test > 1 and slice_clear(z_slices[test-1], (x1, y1, x2, y2), ignore=ignore):
            test -= 1

        # update z slices
        b_height = z2 - z1
        for d in z_slices.values():
            d.pop(i, 0)
        for z in range(test, test + b_height + 1):
            z_slices[z][i] = (x1, y1, x2, y2)
        # update bricks
        bricks[i] = ((x1, y1, test), (x2, y2, test+b_height))

settle(bricks, z_slices)

total = 0
for i, b in enumerate(bricks):
    (x1, y1, z1), (x2, y2, z2) = b
    print("testing dis for brick", i)

    temp_slices = deepcopy(z_slices)
    for d in temp_slices.values():
        d.pop(i, 0)
    temp_bricks = bricks.copy()

    settle(temp_bricks, temp_slices, ignore=i)

    for j, (b1, b2) in enumerate(zip(bricks, temp_bricks)):
        if b1 != b2:
            total += 1

print(total)
