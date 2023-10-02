data = [line.rstrip("\n") for line in open("input11.txt")]

grid = {}

for x, line in enumerate(data):
	for y, char in enumerate(line):
		grid[(x,y)] = int(char)


def neighbors(grid, point):
	lst = []
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if x == 0 and y == 0:
				continue

			test = (point[0] + x, point[1] + y)
			if test in grid:
				lst.append(test)

	return lst


def printGrid(grid):
	for x in range(10):
		for y in range(10):
			print(grid[(x,y)], end="")

		print()


flashes = 0
for step in range(500):
	for point in grid:
		grid[point] += 1

	to_flash = []
	for point in grid:
		if grid[point] > 9:
			to_flash.append(point)
			grid[point] = 0
			
	while len(to_flash) > 0:
		flashes += 1
		point = to_flash.pop()
		grid[point] = 0
		for n in neighbors(grid, point):
			if grid[n] != 0:
				grid[n] += 1
				if grid[n] > 9:
					to_flash.append(n)
					grid[n] = 0


	if all([grid[point] == 0 for point in grid]):
		print("ALL FLASHED:", step + 1)
		break


print(flashes)
						








