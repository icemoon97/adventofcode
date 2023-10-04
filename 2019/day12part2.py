from math import gcd

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

moons = []

for line in data:
	line = line.split(",")
	x = int(line[0][3:])
	y = int(line[1][3:])
	z = int(line[2][3:len(line[2]) - 1])
	moons.append(Moon([x,y,z], moons))

xHistory = set()
xCycle = False
yHistory = set()
yCycle = False
zHistory = set()
zCycle = False

for i in range(1000000):
	for moon in moons:
		moon.updateVel()
	for moon in moons:
		moon.updatePos()

	if not xCycle:
		xState = str([[moon.pos[0], moon.vel[0]] for moon in moons])
		if xState in xHistory:
			xCycle = i
		xHistory.add(xState)
	if not yCycle:
		yState = str([[moon.pos[1], moon.vel[1]] for moon in moons])
		if yState in yHistory:
			yCycle = i
		yHistory.add(yState)
	if not zCycle:
		zState = str([[moon.pos[2], moon.vel[2]] for moon in moons])
		if zState in zHistory:
			zCycle = i
		zHistory.add(zState)

	if xCycle and yCycle and zCycle:
		break
	
cycles = [xCycle, yCycle, zCycle]
print(cycles)
 
lcm = cycles[0]
for i in cycles[1:]:
	lcm = lcm * i // gcd(lcm, i)
print(lcm)