class IC:
	def __init__(self, program):
		self.data = [int(i) for i in program.split(",")]
		self.i = 0
		self.base = 0

		self.input = 0
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
				self.data[index] = self.input
				self.i += 2
			elif opcode == 4:
				value = self.getReadParameter(0, parameterModes)
				self.output.append(value)
				self.i += 2
				if len(self.output) >= numOutputs:
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

data = [line.rstrip("\n") for line in open("input13.txt")][0]

com = IC(data)

grid = [[0 for x in range(40)] for y in range(25)]

while not com.done:
	com.run(3)

	if com.done:
		break

	x = com.output[0]
	y = com.output[1]
	tileID = com.output[2]
	com.output = []

	grid[y][x] = tileID

total = 0
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == 2:
			total += 1
		print(grid[y][x], end="")
	print()

print(total)

