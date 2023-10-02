from helper import *
from queue import PriorityQueue

input_file = "input24.txt"

# input_file = "input24test.txt"

with open(input_file, "r") as file:
	data = file.read().split("\n")

grid = {}
bliz = []

for i, line in enumerate(data):
	for j, char in enumerate(line):
		if char in [">", "<", "v", "^"]:
			match char:
				case ">":
					d = (0,1)
				case "<":
					d = (0,-1)
				case "v":
					d = (1,0)
				case "^":
					d = (-1,0)
			
			bliz.append(((i,j), d))
			char = "."
		grid[(i,j)] = char

print_grid(grid)

def sim_bliz(bliz):
	result = []
	for b in bliz:
		pos, d = b

		test = (pos[0] + d[0], pos[1] + d[1])
		assert test in grid
		if grid[test] != ".":
			if d == (1, 0):
				test = (min([x[0] for x in grid.keys() if x[1] == test[1] and grid[x] == "."]), test[1])
			elif d == (-1, 0):
				test = (max([x[0] for x in grid.keys() if x[1] == test[1] and grid[x] == "."]), test[1])
			elif d == (0, 1):
				test = (test[0], min([x[1] for x in grid.keys() if x[0] == test[0] and grid[x] == "."]))
			elif d == (0, -1):
				test = (test[0], max([x[1] for x in grid.keys() if x[0] == test[0] and grid[x] == "."]))

		assert grid[test] == "."

		result.append((test, d))

	return result
	
def compute_next_bliz(bliz_states, bliz_sets):
	# print("precomputing blizzard", len(bliz_states))
	b = sim_bliz(bliz_states[-1])
	bliz_states.append(b)
	bliz_sets.append(set([x[0] for x in b]))

bliz_states = [bliz]
bliz_sets = [set([x[0] for x in bliz])]	
	
def h(point, goal):
	return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

best_cost = {p : 999999 for p in grid if grid[p] == "."}

start = (0, 1)
end = (len(data) - 1, len(data[0]) - 2)

def search(start, end, bliz_i=0):
	q = PriorityQueue()
	q.put((h(start, end), 0, start)) # heuristic, steps, position

	seen = {(0, start)}

	searched = 0

	while not q.empty() and searched <= 100000:
		if searched % 10000 == 0:
			print(searched)
		searched += 1

		_, steps, cur = q.get()
		while steps + 1 + bliz_i >= len(bliz_sets):
			compute_next_bliz(bliz_states, bliz_sets)
		cur_bliz = bliz_sets[steps + 1 + bliz_i]

		if cur == end:
			return steps

		# print("current:", steps, cur)

		for d in [(1,0), (0,1), (-1,0), (0,-1), (0,0)]:
			test = (cur[0] + d[0], cur[1] + d[1])
			# print("test:", test)
			if test not in grid or grid[test] != ".":
				# print(test, "not valid square")
				continue
			if test in cur_bliz:
				# print(test, "in blizzard")
				continue
			if (steps + 1, test) in seen:
				continue

			guess = steps + 1 + h(test, end)

			# print("guess:", test, guess, steps + 1)

			q.put((guess, steps + 1, test))
			seen.add((steps + 1, test))

there = search(start, end)
back = search(end, start, bliz_i=there)
there2 = search(start, end, bliz_i=(there + back))

print(there, back, there2)
print(there + back + there2)