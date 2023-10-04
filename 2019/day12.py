data = [line.rstrip("\n") for line in open("input12.txt")]

class Moon:
	def __init__(self, pos, other):
		self.pos = pos
		self.vel = [0,0,0]
		self.other = other

	def updateVel(self):
		for moon in self.other:
			for i in range(3):
				if moon.pos[i] < self.pos[i]:
					self.vel[i] -= 1
				elif moon.pos[i] > self.pos[i]:
					self.vel[i] += 1

	def updatePos(self):
		for i in range(3):
			self.pos[i] += self.vel[i]

	def __str__(self):
		return "pos: " + str(self.pos) + ", vel: " + str(self.vel)

	def getEnergy(self):
		potential = 0
		for i in range(3):
			potential += abs(self.pos[i])
		kinetic = 0
		for i in range(3):
			kinetic += abs(self.vel[i])
		return potential * kinetic

moons = []

for line in data:
	line = line.split(",")
	x = int(line[0][3:])
	y = int(line[1][3:])
	z = int(line[2][3:len(line[2]) - 1])
	moons.append(Moon([x,y,z], moons))



for i in range(1000):
	for moon in moons:
		moon.updateVel()
	for moon in moons:
		moon.updatePos()

	print("AFTER STEP", i + 1)

	total = 0
	for moon in moons:
		print(moon)
		total += moon.getEnergy()
	print(total)
