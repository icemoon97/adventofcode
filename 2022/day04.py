from helper import *

with open("input04.txt", "r") as file:
    data = file.read().split("\n")

p1 = 0
p2 = 0

for line in data:
    # a, b = line.split(",")

    # a1, a2 = [int(x) for x in a.split("-")]
    # b1, b2 = [int(x) for x in b.split("-")]

    a1, a2, b1, b2 = parse_ints(line.replace("-", " "))

    if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
        p1 += 1
    if not (a2 < b1 or a1 > b2):
        p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)

