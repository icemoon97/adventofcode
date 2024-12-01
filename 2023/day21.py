from collections import defaultdict

with open("input21.txt", "r") as file:
    data = file.read().split("\n")

dim = (len(data), len(data[0]))
print(dim)

grid = {}
start = (-1, -1)

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
            char = "."
        
        grid[(i,j)] = char

def neighbors(point):
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        test = (point[0] + dx, point[1] + dy)
        test_mod = (test[0] % dim[0], test[1] % dim[1])
        if grid[test_mod] == ".":
            yield test

cur = set([start])
steps_count = [1]

for i in range(1):
    print(i)

    next = set()
    for p in cur:
        next |= set(neighbors(p))
    cur = next

    steps_count.append(len(cur))

# print(steps_count)

# steps_count = defaultdict(lambda: 0)
# steps_max = 330

# queue = [(0, start)]
# visited = set()

# while queue:
#     steps, cur = queue.pop(0)

#     if (steps, cur) in visited:
#         continue
#     visited.add((steps, cur))

#     if steps_count[steps] == 0:
#         print(steps)

#     steps_count[steps] += 1
#     if steps == steps_max:
#         continue

#     for p in neighbors(cur):
#         queue.append((steps+1, p))

# print(steps_count[6])
# print(steps_count[10])
# print(steps_count[50])

# print(steps_count)
# print(steps_count[65], steps_count[dim[0] + 65], steps_count[dim[0] * 2 + 65])

# from wolfram alpha:
# (14655 x^2)/17161 + (30375 x)/17161 - 52830/17161

def f(x):
    return (14655 * x**2)/17161 + (30375 * x)/17161 - 52830/17161

print("Part 2:", f(26501365))
