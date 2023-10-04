data = [line.rstrip("\n") for line in open("input17.txt")]

start = [[data[x][y] for y in range(len(data[x]))] for x in range(len(data))]
s = len(start)

grid = [[["." for y in range(s + 12)] for x in range(s + 12)] for z in range(s + 12)]

def print_slice(grid):
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			print(grid[x][y], end="")
		print()

for x in range(len(start)):
	for y in range(len(start[x])):
		grid[6][x + 6][y + 6] = start[x][y]

def adj(z, x, y):
	adj = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				if i == 0 and j == 0 and k == 0:
					continue

				try:
					if grid[z + k][x + i][y + j] == "#":
						adj += 1
				except:
					pass

	return adj

for step in range(6):
	next_grid = [[["." for y in range(s + 12)] for x in range(s + 12)] for z in range(s + 12)]

	for z in range(len(grid)):
		for x in range(len(grid[z])):
			for y in range(len(grid[z][x])):
				a = adj(z,x,y)

				if grid[z][x][y] == "." and a == 3:
					next_grid[z][y][x] = "#"
				if grid[z][x][y] == "#" and (a == 3 or a == 2):
					next_grid[z][y][x] = "#"

	grid = next_grid

s = 0
for z in range(len(grid)):
	for x in range(len(grid[z])):
		for y in range(len(grid[z][x])):
			if grid[z][y][x] == "#":
				s += 1

print(s)