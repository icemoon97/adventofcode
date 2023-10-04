import string

data = [line.rstrip("\n") for line in open("input20.txt")]

grid = [[line[i] for i in range(len(line))] for line in data]
for line in grid:
	line.insert(0, " ")
	line.append(" ")
grid.insert(0, [" " for i in range(len(grid[0]))])
grid.append([" " for i in range(len(grid[0]))])

width = len(grid[0])
height = len(grid)

def printGrid(grid):
	for y in range(height):
		for x in range(width):
			print(grid[y][x], end=" ")
		print()

printGrid(grid)

dirs = {
	0 : (-1, 0),
	1 : (0, 1),
	2 : (1, 0),
	3 : (0, -1)
}

start = (-1, -1)
end = (-1, -1)
portals = {}
half = {}

for y in range(height):
	for x in range(width):
		char = grid[y][x]

		if not char in string.ascii_uppercase:
			continue

		for direction in range(4):
			test = grid[y + dirs[direction][0]][x + dirs[direction][1]]
			if not test in string.ascii_uppercase:
				continue

			portalName = char + test

			





