import string

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

def getReachableKeys(start, keyInfo, doorInfo):
	distances = [[-1 for x in range(width)] for y in range(height)]
	distances[start[0]][start[1]] = 0
	queue = [start]

	reachableKeys = {}

	while len(queue) > 0:
		node = queue[0]
		queue.pop(0)

		if node in keyInfo:
			reachableKeys[node] = distances[node[0]][node[1]]

		for direction in range(4):
			test = (node[0] + dirs[direction][0], node[1] + dirs[direction][1])
			if distances[test[0]][test[1]] == -1 and grid[test[0]][test[1]] != "#" and test not in doorInfo:
				distances[test[0]][test[1]] = distances[node[0]][node[1]] + 1

				queue.append(test)

	return reachableKeys

print("Start:", start)
print("Keys:", keys)
print("Doors:", doors)

seen = {}

def search(start, steps, keysLeft, doorsLeft, keysHeld):
	reachableKeys = getReachableKeys(start, keysLeft, doorsLeft)
	state = f"{start} {keysHeld}"
	#print(state)

	if state in seen and seen[state] <= steps:
		return 9999999

	seen[state] = steps

	if len(reachableKeys) == 0:
		return steps

	results = []

	for key in reachableKeys:
		distance = reachableKeys[key]
		
		kh = keysHeld.copy()
		kh.add(keysLeft[key])

		# opening door
		dl = doorsLeft.copy()
		for pos in dl:
			if keysLeft[key].upper() == dl[pos]:
				dl.pop(pos)
				break

		kl = keysLeft.copy()
		kl.pop(key)

		results.append(search(key, steps + distance, kl, dl, kh))

	result = min(results)

	return result

best = search(start, 0, keys, doors, set())
print("Best:", best)

for key in seen:
	print(key, seen[key])