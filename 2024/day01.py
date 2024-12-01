from collections import Counter

with open("input01.txt", "r") as file:
    data = file.read().split("\n")

left = []
right = []
for line in data:
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

print("Part 1:", sum([abs(a - b) for a, b in zip(sorted(left), sorted(right))]))

counts = Counter(right)

print("Part 2:", sum([counts[a] * a for a in left]))

