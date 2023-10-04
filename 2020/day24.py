data = [line.rstrip("\n") for line in open("input24.txt")]

grid = [[False for y in range(100)] for x in range(100)]

for line in data:
	pos = (50, 50)

	i = 0
	while i < len(line):
		if line[i] == "n":
			instruction = line[i:i + 2]
			i += 2
		elif line[i] == "s":
			instruction = line[i:i + 2]
			i += 2
		else:
			instruction = line[i]
			i += 1

		if pos[0] % 2 == 0:
			dirs = {"nw": (-1, 0), "ne": (-1, 1), "sw": (1, 0), "se": (1, 1), "e": (0, 1), "w": (0, -1)}
		else:
			dirs = {"nw": (-1, -1), "ne": (-1, 0), "sw": (1, -1), "se": (1, 0), "e": (0, 1), "w": (0, -1)}

		d = dirs[instruction]
		pos = (pos[0] + d[0], pos[1] + d[1])

	grid[pos[0]][pos[1]] = not grid[pos[0]][pos[1]]

s = 0
for line in grid:
	s += sum([1 if x else 0  for x in line])
print(s)

