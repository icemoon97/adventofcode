from collections import Counter

with open("input23.txt", "r") as file:
	data = file.read().split("\n")

# with open("input23test.txt", "r") as file:
# 	data = file.read().split("\n")

def get_neighbors(point):
	neighbors = []
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if x == 0 and y == 0:
				continue
			neighbors.append((point[0] + x, point[1] + y))
	return neighbors

def calc_empty_space(elves):
	empty = 0

	x = [x[0] for x in elves]
	y = [x[1] for x in elves]
	for i in range(min(x), max(x) + 1):
		for j in range(min(y), max(y) + 1):
			if (i,j) not in elves:
				empty += 1
		
	return empty

elves = set()
for i, line in enumerate(data):
	for j, char in enumerate(line):
		if char == "#":
			elves.add((i,j))

# north, south, east, west
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
dir_i = 0

any_moved = True
round = 0

while any_moved:
	proposals = []

	for ex, ey in elves:
		if not any([n in elves for n in get_neighbors((ex, ey))]):
			continue

		for i in range(len(dirs)):
			dx, dy = dirs[(dir_i + i) % len(dirs)]
			if dy == 0:
				test = [(dx, dy - 1), (dx, dy), (dx, dy + 1)]
			else:
				test = [(dx - 1, dy), (dx, dy), (dx + 1, dy)]

			occupied = any([(ex + tx, ey + ty) in elves for tx, ty in test])

			if not occupied:
				proposals.append(((ex, ey), (ex + dx, ey + dy)))
				break

	c = Counter([p for _, p in proposals])

	any_moved = False

	for e, maybe in proposals:
		if c[maybe] == 1:
			elves.remove(e)
			elves.add(maybe)

			any_moved = True

	dir_i += 1
	round += 1

	if round == 10:
		print("Part 1:", calc_empty_space(elves))

print("Part 2:", round)