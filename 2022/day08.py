from helper import *
import math

with open("input08.txt", "r") as file:
	data = file.read().split("\n")

n, m = len(data), len(data[0])
grid = read_grid(data)

def visible_trees(grid, point, d):
	n = 0
	test = (point[0] + d[0], point[1] + d[1])

	while test in grid:
		if grid[test] >= grid[point]:
			return n + 1, False
		n += 1
		test = (test[0] + d[0], test[1] + d[1])

	return n, True

def is_visible(grid, point):
	return any([visible_trees(grid, point, d)[1] for d in [(1,0), (0,1), (-1,0), (0,-1)]])

def scenic_score(grid, point):
	trees = [visible_trees(grid, point, d)[0] for d in [(1,0), (0,1), (-1,0), (0,-1)]]
	return math.prod(trees)

visible = 0
best = 0

for point in grid:
	if is_visible(grid, point):
		visible += 1

	best = max(best, scenic_score(grid, point))

print("Part 1:", visible)
print("Part 2:", best)	
