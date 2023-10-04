data = [line.rstrip("\n") for line in open("input03.txt")]

grid = [[x for x in line] for line in data]

trees = 0

for y in range(len(grid)):
	char = grid[y][y * 3 % len(grid[0])]

	if char == "#":
		trees += 1

print(trees)