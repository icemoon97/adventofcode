import math

data = [line.rstrip("\n") for line in open("input10.txt")]

width = len(data[0])
height = len(data)
grid = [["" for x in range(width)] for y in range(height)]

for y in range(height):
	for x in range(width):
		grid[y][x] = data[y][x]

def printGrid(grid):
	for y in range(height):
		for x in range(width):
			print(grid[y][x], end="")
		print()

asteroids = set()
for y in range(height):
	for x in range(width):
		if grid[y][x] == "#":
			asteroids.add((y, x))

def getCanSee(asteroid):
	canSee = [[1 for x in range(width)] for y in range(height)]
	canSee[asteroid[0]][asteroid[1]] = 0

	vectors = {}
	for other in asteroids:
		if other != asteroid:
			vector = (other[0] - asteroid[0], other[1] - asteroid[1])
			gcd = math.gcd(vector[0], vector[1])
			vector = (int(vector[0] / gcd), int(vector[1] / gcd))

			vectors[other] = vector

			test = (other[0] + vector[0], other[1] + vector[1])
			while 0 <= test[0] < height and 0 <= test[1] < width:
				canSee[test[0]][test[1]] = 0
				test = (test[0] + vector[0], test[1] + vector[1])

	return canSee

def getAsteroidsSeen(asteroid):
	canSee = getCanSee(asteroid)

	total = 0
	for y in range(height):
		for x in range(width):
			if canSee[y][x] == 1 and grid[y][x] == "#":
				total += 1

	return total

best = 0
for asteroid in asteroids:
	best = max(best, getAsteroidsSeen(asteroid))

print(best)

