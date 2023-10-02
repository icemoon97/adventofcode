from helper import *

with open("input17.txt", "r") as file:
	data = file.read().split("\n\n")

jets = data[0].rstrip("\n")

rocks = []
for line in data[1:]:
	line = line.split("\n")
	rock = set()
	
	for i, row in enumerate(line):
		for j, char in enumerate(row):
			if char == "#":
				rock.add((i,j))
	
	rocks.append(rock)

# returns next position of rock after attempted move in direction d, 
# with bool if rock changed position or not
def try_move(grid, rock, d):
	new_rock = set()
	for p in rock:
		test = (p[0] + d[0], p[1] + d[1])
		if test in grid or test[0] >= 0 or test[1] not in range(7):
			return rock, False

		new_rock.add(test)

	return new_rock, True

# simulates next rock falling, returns jet index after rock stops moving
def sim_rock(grid, count, jet_i, height):
	shape = rocks[count % len(rocks)]
	start = (height - max([p[0] for p in shape]) - 4, 2)
	rock = set()
	for p in shape:
		rock.add((p[0] + start[0], p[1] + start[1]))

	while True:
		d = (0, 1 if jets[jet_i % len(jets)] == ">" else -1)
		rock, _ = try_move(grid, rock, d)

		jet_i += 1

		rock, changed = try_move(grid, rock, (1, 0))
		if not changed:
			grid |= rock
			return jet_i, min(height, min([p[0] for p in rock]))

def part1():
	grid = set()
	jet_i = 0
	height = 0

	for count in range(2022):
		jet_i, height = sim_rock(grid, count, jet_i, height)

	return -height

def part2():
	grid = set()	
	count = 0
	jet_i = 0
	height = 0

	history = {}

	while True:
		jet_i, height = sim_rock(grid, count, jet_i, height)
		count += 1

		pattern = ""
		for row in range(5):
			pattern += "".join(["#" if (height + row, i) in grid else "." for i in range(7)])
		ri = count % len(rocks)
		ji = jet_i % len(jets)

		# cycle is identified by last 5 rows, shape index, and jet index
		id = (pattern, ri, ji)
		if id in history:
			prev_height, prev_count = history[id]

			cycle = count - prev_count
			change = abs(height - prev_height)

			while (1000000000000 - count) % cycle != 0:
				jet_i, height = sim_rock(grid, count, jet_i, height)
				count += 1

			return -height + ((1000000000000 - count) // cycle) * change

		history[id] = (height, count)

print("Part 1:", part1())
print("Part 2:", part2())
