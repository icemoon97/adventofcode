import string
import itertools

grid = [line.rstrip("\n") for line in open("input18.txt")]

width = len(grid[0])
height = len(grid)

def printGrid(grid):
	for y in range(height):
		for x in range(width):
			print(grid[y][x], end=" ")
		print()

keys = {}
doors = {}
start = ""

for y in range(height):
	for x in range(width):
		if grid[y][x] in string.ascii_uppercase:
			doors[(y, x)] = grid[y][x]
		if grid[y][x] in string.ascii_lowercase:
			keys[(y, x)] = grid[y][x]
		if grid[y][x] == "@":
			start = (y, x)

dirs = {
	0 : (-1, 0),
	1 : (0, 1),
	2 : (1, 0),
	3 : (0, -1)
}

def search(start, keys, doors):
	distances = [[-1 for x in range(width)] for y in range(height)]
	distances[start[0]][start[1]] = 0
	queue = [start]

	possibleKeys = {}

	while len(queue) > 0:
		node = queue[0]
		queue.pop(0)

		if node in keys.keys():
			possibleKeys[node] = distances[node[0]][node[1]]

		for direction in range(4):
			test = (node[0] + dirs[direction][0], node[1] + dirs[direction][1])
			if distances[test[0]][test[1]] == -1 and grid[test[0]][test[1]] != "#" and test not in doors.keys():
				distances[test[0]][test[1]] = distances[node[0]][node[1]] + 1

				queue.append(test)

	return possibleKeys

def getKey(pos, key, steps, keysLeft, doorsLeft):
	distances = search(pos, keysLeft, doorsLeft)

	pos = key
	steps += distances[key]

	for item in doorsLeft.keys():
		if keysLeft[key].upper() == doorsLeft[item]:
			doorsLeft.pop(item)
			break

	keysLeft.pop(key)

	possibleKeys = search(pos, keysLeft, doorsLeft)

	if len(possibleKeys) == 0:
		return steps

	possible = []

	for key in possibleKeys.keys():
		possible.append(getKey(pos, key, steps, keysLeft.copy(), doorsLeft.copy()))

	return min(possible)

possibleKeys = search(start, keys, doors)

for key in possibleKeys.keys():
	print(getKey(start, key, 0, keys.copy(), doors.copy()))






