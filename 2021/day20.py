data = "\n".join([line.rstrip("\n") for line in open("input20.txt")])

algo, image = data.split("\n\n")

grid = {}

for x, line in enumerate(image.split("\n")):
	for y, char in enumerate(line):
		grid[(x,y)] = char

def neighbors(point):
	lst = []
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			p = (point[0] + x, point[1] + y)
			lst.append(p)

	return lst

def algoIndex(point, lit, default="0"):
	b = ""

	for p in neighbors(point):
		if p in grid:
			b += "1" if grid[p] == "#" else "0"
		else:
			b += default

	return int(b, 2)

def minMaxPoints(s):
	min_p = (99999999, 99999999)
	max_p = (-99999999, -99999999)

	for p in s:
		min_p = (min(min_p[0], p[0]), min(min_p[1], p[1]))
		max_p = (max(max_p[0], p[0]), max(max_p[1], p[1]))

	return min_p, max_p

def process(grid, algo, default="0"):
	result = {}

	min_p, max_p = minMaxPoints(grid)

	for x in range(min_p[0] - 2, max_p[0] + 3):
		for y in range(min_p[1] - 2, max_p[1] + 3):
			i = algoIndex((x,y), grid, default)
			result[(x,y)] = algo[i]

	return result

def printGrid(grid, default):
	min_p, max_p = minMaxPoints(grid)

	for x in range(min_p[0] - 2, max_p[0] + 3):
		for y in range(min_p[1] - 2, max_p[1] + 3):
			if (x,y) in grid:
				print(grid[(x,y)], end="")
			else:
				print(default, end="")
		print()

for step in range(50):
	print(step)
	if step % 2 == 0:
		default = "0"
	else:
		default = "1"

	grid = process(grid, algo, default)

n = 0
for val in grid.values():
	if val == "#":
		n += 1

print("Part 2:", n)