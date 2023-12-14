
def min_max(l):
	return min(l), max(l)

##
## Parsing helpers
##

# returns list of all ints in given string (works with negatives, not decimals)
def parse_ints(s: str):
	s = "".join([c if c.isdigit() or c == "-" else " " for c in s])
	s = [int(x) for x in s.split()]
	return s


##
## 2D grid related helpers
##

# TODO: make read grid and print grid better, more adaptable to fixed vs variable grids, formats, etc
# TODO: make seperate get_neighbors for just wanting different directions, or wanting within given grid, or some other check

# reads in standard advent grid of nums, chars, etc as dict of (x,y) -> char
# can pass an interp function to do some processing on each input
def read_grid(data: list, interp=lambda x: x):
	grid = {}

	for i, line in enumerate(data):
		for j, char in enumerate(line):
			grid[(i,j)] = interp(char)

	return grid

# prints grid (assumes grid is dict of (x,y) -> ?) with given end character after each element
def print_grid(grid: dict, end="", default=" "):
	x = [x[0] for x in grid.keys()]
	x = (min(x), max(x))
	y = [x[1] for x in grid.keys()]
	y = (min(y), max(y))

	for i in range(x[0], x[1] + 1):
		for j in range(y[0], y[1] + 1):
			# print(str(grid[(i,j)]) if (i,j) in grid else default, end=end)
			print(grid[(i,j)], end=end)
		print()

# returns 4 neighbors: up left down right
def get_neighbors4(grid:dict, point: tuple[int, int]):
	neighbors = []
	for d in [(1,0), (0,1), (-1,0), (0,-1)]:
		test = (point[0] + d[0], point[1] + d[1])
		if test in grid:
			neighbors.append(test)
	return neighbors

# returns 8 neighbors (includes diagonals)
def get_neighbors8(grid:dict, point: tuple[int, int]):
	neighbors = []
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if x == 0 and y == 0:
				continue
			test = (point[0] + x, point[1] + y)
			if test in grid:
				neighbors.append(test)
	return neighbors

