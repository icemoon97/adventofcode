data = [line.rstrip("\n") for line in open("input24.txt")]

size = 150
grid = [[False for y in range(size)] for x in range(size)]

for line in data:
	pos = (size // 2, size // 2)

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

"""
for x in range(len(grid[40:60])):
	for y in range(len(grid[0][40:60])):
		print(1 if grid[x + 40][y + 40] else 0,end="")
	print()
"""

s = 0
for line in grid:
	s += sum([1 if x else 0  for x in line])
print(s)

for i in range(100):
	next_grid = [[False for y in range(size)] for x in range(size)]

	for x in range(1, len(grid) - 1):
		for y in range(1, len(grid[x]) - 1):

			adj = 0

			if x % 2 == 0:
				for n in [(-1, 0), (-1, 1), (1, 0), (1, 1), (0, 1), (0, -1)]:
					if grid[x + n[0]][y + n[1]]:
						adj += 1
			else:
				for n in [(-1, -1), (-1, 0), (1, -1), (1, 0), (0, 1), (0, -1)]:
					if grid[x + n[0]][y + n[1]]:
						adj += 1
		
			if adj > 0 and (x < 5 or x > size - 5 or y < 5 or y > size - 5):
				print("oh no, grid too small")
				raise SystemExit

			if grid[x][y] and (adj == 0 or adj > 2):
				next_grid[x][y] = False
			elif not grid[x][y] and adj == 2:
				next_grid[x][y] = True
			else:
				next_grid[x][y] = grid[x][y]

	grid = next_grid

	s = 0
	for line in grid:
		s += sum([1 if x else 0  for x in line])
	print(i, s)
