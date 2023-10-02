data = [line.rstrip("\n") for line in open("input05.txt")]

grid = {}

n = 0

for i, line in enumerate(data):
	line = line.split(" -> ")
	x1, y1 = [int(x) for x in line[0].split(",")]
	x2, y2 = [int(x) for x in line[1].split(",")]

	dif = (x1 - x2, y1 - y2)
	mag = max(abs(dif[0]), abs(dif[1]))
	d = (dif[0] / mag, dif[1] / mag)
	d = (int(d[0]), int(d[1]))

	for i in range(mag + 1):
		point = (x1 - d[0] * i, y1 - d[1] * i)
		if point in grid:
			grid[point] += 1
		else:
			grid[point] = 1

for point in grid:
	if grid[point] > 1:
		n += 1
print(n)
