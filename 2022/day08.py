import math
from helper import *

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

# def cache_max(grid, x_range, y_range, d):
# 	m = grid.copy()
# 	for i in x_range:
# 		for j in y_range:
# 			prev = (i + d[0], j + d[1])
# 			m[(i,j)] = max(m[(i,j)], m[prev])
# 	return m

# up = cache_max(grid, range(1, n), range(0, m), (-1, 0))
# down = cache_max(grid, range(n-2, -1, -1), range(0, m), (1, 0))
# left = cache_max(grid, range(0, n), range(1, m), (0, -1))
# right = cache_max(grid, range(0, n), range(m-2, -1, -1), (0, 1))

# visible = 0

# for p in grid:
# 	if p[0] == 0 or p[0] == n - 1 or p[1] == 0 or p[1] == m - 1:
# 		visible += 1
# 		continue

# 	for d in [(1,0,down), (0,1,right), (-1,0,up), (0,-1,left)]:
# 		test = (p[0] + d[0], p[1] + d[1])
# 		if d[2][test] < grid[p]:
# 			visible += 1
# 			break

# print(visible)
		
