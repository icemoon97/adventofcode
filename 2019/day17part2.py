class IC:
	def __init__(self, program):
		self.data = [int(i) for i in program.split(",")]
		self.i = 0
		self.base = 0

		self.input = []
		self.output = []

		self.done = False

		for i in range(10000):
			self.data.append(0)

	def interpretOpcode(self, code):
		code = str(code)
		while len(code) < 5:
			code = "0" + code
		code = list(code)
		opcode = int("".join(code[3:]))
		parameterModes = [int(i) for i in code[:3]]
		parameterModes.reverse()
		return [opcode, parameterModes]

	def getReadParameter(self, n, parameterModes):
		if parameterModes[n] == 0:
			index = self.data[self.i + n + 1]
			return self.data[index]
		elif parameterModes[n] == 1:
			return self.data[self.i + n + 1]
		elif parameterModes[n] == 2:
			index = self.data[self.i + n + 1] + self.base
			return self.data[index]

	def getWriteParameter(self, n, parameterModes):
		if parameterModes[n] == 0:
			return self.data[self.i + n + 1]
		elif parameterModes[n] == 2:
			return self.data[self.i + n + 1] + self.base

	def run(self, numOutputs):
		while self.i < len(self.data):
			command = self.interpretOpcode(self.data[self.i])
			
			opcode = command[0]
			parameterModes = command[1]

			if opcode == 99:
				break
			elif opcode == 1:
				index = self.getWriteParameter(2, parameterModes)
				self.data[index] = self.getReadParameter(0, parameterModes) + self.getReadParameter(1, parameterModes)
				self.i += 4
			elif opcode == 2:
				index = self.getWriteParameter(2, parameterModes)
				self.data[index] = self.getReadParameter(0, parameterModes) * self.getReadParameter(1, parameterModes)
				self.i += 4
			elif opcode == 3:
				index = self.getWriteParameter(0, parameterModes)
				self.data[index] = self.input.pop(0)
				self.i += 2
			elif opcode == 4:
				value = self.getReadParameter(0, parameterModes)
				self.output.append(value)
				self.i += 2
				if len(self.output) == numOutputs:
					return
			elif opcode == 5:
				if self.getReadParameter(0, parameterModes) != 0:
					self.i = self.getReadParameter(1, parameterModes)
				else:
					self.i += 3
			elif opcode == 6:
				if self.getReadParameter(0, parameterModes) == 0:
					self.i = self.getReadParameter(1, parameterModes)
				else:
					self.i += 3
			elif opcode == 7:
				index = self.getWriteParameter(2, parameterModes)
				if self.getReadParameter(0, parameterModes) < self.getReadParameter(1, parameterModes):
					self.data[index] = 1
				else:
					self.data[index] = 0
				self.i += 4
			elif opcode == 8:
				index = self.getWriteParameter(2, parameterModes)
				if self.getReadParameter(0, parameterModes) == self.getReadParameter(1, parameterModes):
					self.data[index] = 1
				else:
					self.data[index] = 0
				self.i += 4
			elif opcode == 9:
				self.base += self.getReadParameter(0, parameterModes)
				self.i += 2

		self.done = True

data = [line.rstrip("\n") for line in open("input17.txt")][0]

com = IC(data)
com.data[0] = 2

"""
while not com.done:
	com.run(1)

cameraView = "".join([chr(i) for i in com.output])
com.output = []

grid = [[line[i] for i in range(len(line))] for line in cameraView.split("\n")]
grid.pop()
grid.pop()

for line in grid:
	line.insert(0, ".")
	line.append(".")
grid.insert(0, ["." for i in range(len(grid[0]))])
grid.append(["." for i in range(len(grid[0]))])

def printGrid():
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			print(grid[y][x], end="")
		print()
"""

def getAllCommands():
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] in "^<>v":
				pos = (y, x)

	dirs = {
		0 : (-1, 0),
		1 : (0, 1),
		2 : (1, 0),
		3 : (0, -1)
	}

	right = [(0, 1), (1, 2), (2, 3), (3, 0)]
	left = [(0, 3), (3, 2), (2, 1), (1, 0)]

	direction = 0

	seen = set()

	commands = []

	for _ in range(100):
		for i in range(4):
			test = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
			if grid[test[0]][test[1]] == "#" and not test in seen:
				if (direction, i) in right:
					commands.append("R")
				elif (direction, i) in left:
					commands.append("L")
				else:
					print("bad")
					raise SystemExit

				direction = i
				steps = 0

				while grid[test[0]][test[1]] == "#":
					steps += 1
					pos = test
					test = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
					seen.add(pos)

				commands.append(str(steps))
				break

	return commands

A = "R,12,L,6,R,12"
B = "L,8,L,6,L,10"
C = "R,12,L,10,L,6,R,10"

mainRoutine = "A,B,A,C,B,C,B,C,A,C"

for char in mainRoutine:
	com.input.append(ord(char))
com.input.append(10)

def inputFunction(function):
	for instruction in function:
		com.input.append(ord(instruction))
	com.input.append(10)	

inputFunction(A)
inputFunction(B)
inputFunction(C)

com.input.append(ord("n"))
com.input.append(10)

while not com.done:
	com.run(1)

print(com.output[-1])

