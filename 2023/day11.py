import itertools

with open("input11.txt", "r") as file:
    data = file.read().split("\n")

dim = (len(data), len(data[0]))

stars = []
grid = {}

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "#":
            stars.append((i, j))
        grid[(i,j)] = char

empty_rows = []
for i in range(dim[0]):
    if all(c == "." for c in data[i]):
        empty_rows.append(i)
empty_cols = []
for i in range(dim[1]):
    if all(c == "." for c in [line[i] for line in data]):
        empty_cols.append(i)

def total_dist(gap=2):
    expanded = []
    for x, y in stars:
        x += sum(x > i for i in empty_rows) * (gap - 1)
        y += sum(y > i for i in empty_cols) * (gap - 1)
        expanded.append((x, y))

    total = 0
    for a, b in itertools.combinations(expanded, 2):
        dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
        total += dist
    return total

print("Part 1:", total_dist())
print("Part 2:", total_dist(gap=1000000))