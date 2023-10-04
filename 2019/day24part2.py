data = [line.rstrip("\n") for line in open("input24.txt")]

grid = [[char for char in line] for line in data]
width = len(grid[0])
height = len(grid)

depth = 110
layers = [grid]
for _ in range(depth):
	layers.insert(0, [["." for x in range(width)] for y in range(height)])
	layers.append([["." for x in range(width)] for y in range(height)])

for layer in layers:
	layer[2][2] = "?"

def printGrid(grid):
	for y in range(height):
		for x in range(width):
			print(grid[y][x], end="")
		print()
	print()

def getNeighbors(layers, layerIndex, y, x):
	if layerIndex == 0 or layerIndex == len(layers) - 1: #i hate myself
		return 0

	count = 0
	neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	for point in neighbors:
		test = (y + point[0], x + point[1])
		if test[0] < 0:
			if layers[layerIndex - 1][1][2] == "#":
				count += 1
		elif test[0] > height - 1:
			if layers[layerIndex - 1][3][2] == "#":
				count += 1
		elif test[1] < 0:
			if layers[layerIndex - 1][2][1] == "#":
				count += 1
		elif test[1] > width - 1:
			if layers[layerIndex - 1][2][3] == "#":
				count += 1
		elif test[0] == 2 and test[1] == 2:
			if y == 1:
				for i in range(5):
					if layers[layerIndex + 1][0][i] == "#":
						count += 1
			if y == 3:
				for i in range(5):
					if layers[layerIndex + 1][4][i] == "#":
						count += 1

			if x == 1:
				for i in range(5):
					if layers[layerIndex + 1][i][0] == "#":
						count += 1
			if x == 3:
				for i in range(5):
					if layers[layerIndex + 1][i][4] == "#":
						count += 1
		else:
			if layers[layerIndex][test[0]][test[1]] == "#":
				count += 1

	return count

def advance(layers):
	if countBugs(layers[1]) > 0 or countBugs(layers[-2]) > 0:
		print("need more depth")
		raise SystemExit

	new = []
	for i, layer in enumerate(layers):
		newGrid = [line.copy() for line in layer]
		for y in range(height):
			for x in range(width):
				if not (x == 2 and y == 2):
					count = getNeighbors(layers, i, y, x)
					if layer[y][x] == "." and (count == 1 or count == 2):
						newGrid[y][x] = "#"
					if layer[y][x] == "#" and count != 1:
						newGrid[y][x] = "."
		new.append(newGrid)
	return new

def printLayers(layers):
	for i in range(5):
		for j, layer in enumerate(layers):
			print(str(j) + " " + "".join(layer[i]), end="   ")
		print()

def countBugs(layer):
	return sum(["".join(line).count("#") for line in layer])

for i in range(200):
	layers = advance(layers)
	print("layer", i + 1)

total = 0
for layer in layers:
	total += countBugs(layer)

print(total)

