from helper import *
from queue import PriorityQueue

input_file = "input24.txt"
# input_file = "input24test.txt"

with open(input_file, "r") as file:
	data = file.read().split("\n")

dim = len(data), len(data[0])

# parsing grid size and blizzards
grid = {}
bliz = [] # tuples of (pos, direction)

bliz_directions = {
	">": (0,1),
	"<": (0,-1),
	"v": (1,0),
	"^": (-1,0),
}

for i, line in enumerate(data):
	for j, char in enumerate(line):
		if char in bliz_directions:
			bliz.append(((i,j), bliz_directions[char]))
			grid[(i,j)] = "."
		else:
			grid[(i,j)] = char

# all blizzards move one step (and wrap around if necessary)
def sim_bliz(bliz):
	result = []
	for b in bliz:
		pos, d = b
		test = (pos[0] + d[0], pos[1] + d[1])
		assert test in grid

		# if we hit a wall, wrap around
		if grid[test] != ".":
			if d == (1, 0):
				test = (1, test[1])
			elif d == (-1, 0):
				test = (dim[0] - 2, test[1])
			elif d == (0, 1):
				test = (test[0], 1)
			elif d == (0, -1):
				test = (test[0], dim[1] - 2)

		assert grid[test] == "."
		result.append((test, d))

	return result

# computes the next step blizzard series, updates list of states and set of blizzard positions
def compute_next_bliz(bliz_states, bliz_sets):
	b = sim_bliz(bliz_states[-1])
	bliz_states.append(b)
	bliz_sets.append(set([x[0] for x in b]))

bliz_states = [bliz]
bliz_sets = [set([x[0] for x in bliz])]	
	
# heuristic for A* search (manhattan distance)
def h(point, goal):
	return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

best_cost = {p : 999999 for p in grid if grid[p] == "."}

start = (0, 1)
end = (len(data) - 1, len(data[0]) - 2)

def search(start, end, bliz_i=0):
	q = PriorityQueue()
	q.put((h(start, end), 0, start)) # heuristic, steps, position

	seen = {(0, start)}

	# exit search if we search >500k states
	searched = 0
	while not q.empty() and searched <= 500000:
		searched += 1

		_, steps, cur = q.get()
		# only compute next blizzard state when necessary
		# might search states out of order because we are using heuristic
		while steps + 1 + bliz_i >= len(bliz_sets):
			compute_next_bliz(bliz_states, bliz_sets)
		cur_bliz = bliz_sets[steps + 1 + bliz_i]

		if cur == end:
			return steps

		for d in [(1,0), (0,1), (-1,0), (0,-1), (0,0)]:
			test = (cur[0] + d[0], cur[1] + d[1])

			if test not in grid or grid[test] != ".":
				continue
			if test in cur_bliz:
				continue
			if (steps + 1, test) in seen:
				continue

			guess = steps + 1 + h(test, end)

			q.put((guess, steps + 1, test))
			seen.add((steps + 1, test))

	print("no path found")
	return -1


there = search(start, end)

print("Part 1:", there)

back = search(end, start, bliz_i=there)
there_again = search(start, end, bliz_i=(there + back))

print("Part 2:", there + back + there_again)