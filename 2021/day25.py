data = [line.rstrip("\n") for line in open("input25.txt")]

grid = {}

print(len(data), len(data[0]))

for x, line in enumerate(data):
	for y, char in enumerate(line):
		grid[(x,y)] = char

state = str(grid)
print(state)

for step in range(10000):
	print(step)
	east = []
	south = []

	for point in grid:
		if grid[point] == ">":
			test = (point[0], (point[1] + 1) % len(data[0]))
			if grid[test] == ".":
				east.append(point)
		
	for point in east:
		grid[point] = "."
		test = (point[0], (point[1] + 1) % len(data[0]))
		grid[test] = ">"

	for point in grid:
		if grid[point] == "v":
			test = ((point[0] + 1) % len(data), point[1])
			if grid[test] == ".":
				south.append(point)

	for point in south:
		grid[point] = "."
		test = ((point[0] + 1) % len(data), point[1])
		grid[test] = "v"

	if str(grid) == state:
		print("done", step + 1)
		break

	state = str(grid)

def printGrid(grid, n, m):
	for x in range(n):
		for y in range(m):
			print(grid[(x,y)], end="")

		print()

#printGrid(grid, len(data), len(data[0]))