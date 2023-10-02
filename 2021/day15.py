from queue import PriorityQueue

data = [line.rstrip("\n") for line in open("input15.txt")]

n = len(data)
grid = {}

for x, line in enumerate(data):
	for y, char in enumerate(line):
		grid[(x,y)] = int(char)

def printGrid(grid, n):
	for x in range(n):
		for y in range(n):
			print(grid[(x,y)], end="")

		print()

def search(grid, start):
	risk = {}
	for point in grid:
		risk[point] = 9999999999999999999999

	queue = PriorityQueue()
	queue.put((0, start))
	risk[start] = 0

	while not queue.empty():
		val, point = queue.get()

		for d in [(1,0), (0,1), (-1,0), (0,-1)]:
			test = (point[0] + d[0], point[1] + d[1])
			if test not in grid:
				continue

			r = grid[test] + risk[point]
			if r < risk[test]:
				risk[test] = r
				queue.put((r, test))

	return risk

risks = search(grid, (0,0))
print("Part 1:", risks[(n-1,n-1)])

big_grid = {}
for point, val in grid.items():
	for x in range(5):
		for y in range(5):
			p = (n * x + point[0], n * y + point[1])
			n_val = val + x + y
			if n_val > 9:
				n_val -= 9
			big_grid[p] = n_val

big_risks = search(big_grid, (0,0))
print("Part 2:", big_risks[(n * 5 - 1, n * 5 -1)])
