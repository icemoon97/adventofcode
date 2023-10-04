import numpy

data = [line.rstrip("\n") for line in open("input03.txt")]

grid = [[x for x in line] for line in data]

counts = [0, 0, 0, 0, 0]

for y in range(len(grid)):
	if grid[y][y % len(grid[0])] == "#":
		counts[0] += 1
	if grid[y][y * 3 % len(grid[0])] == "#":
		counts[1] += 1
	if grid[y][y * 5 % len(grid[0])] == "#":
		counts[2] += 1
	if grid[y][y * 7 % len(grid[0])] == "#":
		counts[3] += 1

for y in range(0, len(grid), 2):
	if grid[y][int(y / 2) % len(grid[0])] == "#":
		counts[4] += 1

print(counts)
print(numpy.prod(counts))
