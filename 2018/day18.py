from collections import defaultdict

data = [line.rstrip("\n") for line in open("input18.txt")]

grid = defaultdict(lambda: defaultdict(lambda: "."))

n, m = len(data), len(data[0])

for i, line in enumerate(data):
    for j, val in enumerate(line):
        grid[i][j] = val

def get_neighbors(grid, pos):
    counts = {".": 0, "#": 0, "|": 0}
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            counts[grid[pos[0] + x][pos[1] + y]] += 1

    return counts

def step(grid):
    next = defaultdict(lambda: defaultdict(lambda: "."))
    for i in range(n):
        for j in range(m):
            counts = get_neighbors(grid, (i,j))

            if grid[i][j] == ".":
                next[i][j] = "|" if counts["|"] >= 3 else "."
            elif grid[i][j] == "|":
                next[i][j] = "#" if counts["#"] >= 3 else "|"
            else:
                next[i][j] = "#" if (counts["#"] >= 1 and counts["|"] >= 1) else "."

    return next
        
def get_value(grid):
    counts = {".": 0, "#": 0, "|": 0}
    for i in range(n):
        for j in range(m):
            counts[grid[i][j]] += 1

    return counts["|"] * counts["#"]

def printGrid(grid):
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end="")
        print()

for _ in range(580):
    grid = step(grid)

print(get_value(grid))

# i = 0
# history = []
# s = str(grid)
# while s not in history:
#     print(i)
#     history.append(s)
#     grid = step(grid)
#     s = str(grid)
#     i += 1

# printGrid(grid)
# print(get_value(grid))
# print()
# for _ in range(140):
#     grid = step(grid)
# printGrid(grid)
# print(get_value(grid))

print((1000000000 - 500) % 140)

# cycle length: 140

