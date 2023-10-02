data = [line.rstrip("\n") for line in open("input22.txt")]

class Cube:
	def __init__(self, low, high):
		self.low = low
		self.high = high
		self.d = (high[0] - low[0], high[1] - low[1], high[2] - low[2])
		self.v = (self.d[0] + 1) * (self.d[1] + 1) * (self.d[2] + 1)

	def overlap(self, other):
		return all([other.high[i] > self.low[i] and other.low[i] < self.high[i] for i in range(3)])

	def __str__(self):
		return f"[{self.low}, {self.high}]"

	def get_overlap(self, other):
		h = [min(self.high[i], other.high[i]) for i in range(3)]
		l = [max(self.low[i], other.low[i]) for i in range(3)]
		
		return Cube(l, h)

	def split(self, point):
		c1 = Cube(self.low, point)

		c2 = Cube((point[0] + 1, self.low[1], self.low[2]), (self.high[0], point[1], point[2]))
		c3 = Cube((self.low[0], point[1] + 1, self.low[2]), (point[0], self.high[1], point[2]))
		c4 = Cube((self.low[0], self.low[1], point[2] + 1), (point[0], point[1], self.high[2]))

		c5 = Cube((point[0] + 1, point[1] + 1, self.low[2]), (self.high[0], self.high[1], point[2]))
		c6 = Cube((point[0] + 1, self.low[1], point[2] + 1), (self.high[0], point[1], self.high[2]))
		c7 = Cube((self.low[0], point[1] + 1, point[2] + 1), (point[0], self.high[1], self.high[2]))

		c8 = Cube([point[i] + 1 for i in range(3)], self.high)

		cubes = [c1, c2, c3, c4, c5, c6, c7, c8]
		for i in range(len(cubes)):
			c = cubes[i]

			cubes[i] = Cube([max(self.low[i], c.low[i]) for i in range(3)], [min(self.high[i], c.high[i]) for i in range(3)])


		lst = []
		for c in cubes:
			if c.v <= 0 or any([c.low[i] > c.high[i] for i in range(3)]):
				continue

			lst.append(c)
		
		return lst

cubes = []

for line in data:
	op, coords = line.split()

	x, y, z = coords.split(",")

	x1, x2 = x.split("=")[1].split("..")
	y1, y2 = y.split("=")[1].split("..")
	z1, z2 = z.split("=")[1].split("..")
	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	z1 = int(z1)
	z2 = int(z2)

	c = Cube((x1,y1,z1), (x2,y2,z2))
	#print(c)

	cubes.append(c)



print(cubes[0])
print(cubes[1])

s = cubes[1].split(cubes[0].high)
print([str(x) for x in s])

for c in s:
	if c.overlap(cubes[0]):
		print(c)
	