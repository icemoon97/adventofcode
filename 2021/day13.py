data = "\n".join([line.rstrip("\n") for line in open("input13.txt")])

points, folds = data.split("\n\n")
points = points.split("\n")
folds = folds.split("\n")

grid = set()

for p in points:
	x,y = p.split(",")
	x = int(x)
	y = int(y)
	grid.add((x,y))

for fold in folds:
	fold = fold.split()[2]
	axis, val = fold.split("=")
	val = int(val)

	next_grid = set()

	if axis == "x":
		for p in grid:
			if p[0] > val:
				new_p = (p[0] - 2 * (p[0] - val), p[1])
				next_grid.add(new_p)
			else:
				next_grid.add(p)
	else:
		for p in grid:
			if p[1] > val:
				new_p = (p[0], p[1] - 2 * (p[1] - val))
				next_grid.add(new_p)
			else:
				next_grid.add(p)

	grid = next_grid

print(grid)
print(len(grid))

def printGrid(grid):
	for x in range(8):
		for y in range(50):
			if (y,x) in grid:
				print("#", end="")
			else:
				print(".", end="")

		print()

printGrid(grid)
