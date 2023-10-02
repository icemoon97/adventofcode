data = [line.rstrip("\n") for line in open("input09.txt")]

grid = {}

for x, line in enumerate(data):
	for y, char in enumerate(line):
		grid[(x,y)] = char

def is_low(grid, point):
	for d in [(1,0), (0,1), (-1,0), (0,-1)]:
		test = (point[0] + d[0], point[1] + d[1])

		if test in grid:
			if grid[test] <= grid[point]:
				return False

	return True

low_points = []
for point in grid:
	if is_low(grid, point):
		low_points.append(point)

print("Part 1:", sum([int(grid[p]) for p in low_points]) + len(low_points))

def find_basin(grid, point, basin):
	for d in [(1,0), (0,1), (-1,0), (0,-1)]:
		test = (point[0] + d[0], point[1] + d[1])
		if test not in basin and test in grid and grid[test] != "9":
			basin.append(test)
			find_basin(grid, test, basin)
		

basin_lens = []
for low in low_points:
	basin = []
	find_basin(grid, low, basin)
	basin_lens.append(len(basin))

basin_lens.sort()
p = 1
for n in basin_lens[-3:]:
	p *= n

print("Part 2:", p)

