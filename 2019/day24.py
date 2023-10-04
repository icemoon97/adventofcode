data = [line.rstrip("\n") for line in open("input24.txt")]

grid = [[char for char in line] for line in data]
width = len(grid[0])
height = len(grid)

def printGrid(grid):
	for y in range(height):
		for x in range(width):
			print(grid[y][x], end="")
		print()

def getNeighbors(grid, y, x):
	count = 0
	for y1 in range(-1, 2):
		for x1 in range(-1, 2):
			if y1 == 0 and x1 == 0:
				continue

			if y1 != 0 and x1 != 0:
				continue

			if y + y1 < 0 or y + y1 > height - 1 or x + x1 < 0 or x + x1 > width - 1:
				continue

			if grid[y + y1][x + x1] == "#":
				count += 1
	return count

def advance(grid):
	newGrid = [line.copy() for line in grid]
	for y in range(height):
		for x in range(width):
			count = getNeighbors(grid, y, x)
			if grid[y][x] == "." and (count == 1 or count == 2):
				newGrid[y][x] = "#"
			if grid[y][x] == "#" and count != 1:
				newGrid[y][x] = "."
	return newGrid


history = set()

while str(grid) not in history:
	history.add(str(grid))
	grid = advance(grid)


i = 0
rating = 0
for y in range(height):
	for x in range(width):
		if grid[y][x] == "#":
			rating += 2 ** i
		i += 1

print(rating)



