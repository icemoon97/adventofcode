import random

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

data = [line.rstrip("\n") for line in open("input15.txt")][0]

com = IC(data)

grid = [["?" for x in range(44)] for y in range(44)]

pos = (len(grid) // 2, len(grid[0]) // 2)

def printGrid(grid):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			print(grid[y][x], end=" ")
		print()

dirs = {
	1 : (-1, 0),
	2 : (1, 0),
	3 : (0, -1),
	4 : (0, 1)
}

opposite = {
	1 : 2,
	2 : 1,
	3 : 4,
	4 : 3
}

searched = set()

def search(pos):
	searched.add(pos)

	for direction in range(1, 5):
		com.input = direction
		com.run(1)
		output = com.output[0]
		com.output = []

		pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])

		if output == 0:
			grid[pos[0]][pos[1]] = "#"
		elif output == 1:
			grid[pos[0]][pos[1]] = "."

			if not pos in searched:
				search(pos)

			com.input = opposite[direction]
			com.run(1)
			com.output = []
		elif output == 2:
			grid[pos[0]][pos[1]] = "E"

			if not pos in searched:
				search(pos)

			com.input = opposite[direction]
			com.run(1)
			com.output = []

		pos = (pos[0] - dirs[direction][0], pos[1] - dirs[direction][1])

search(pos)

printGrid(grid)

oxygen = (-1, -1)

for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == "E":
			oxygen = (y, x)


distances = [[-1 for x in range(44)] for y in range(44)]
distances[oxygen[0]][oxygen[1]] = 0

queue = []
queue.append(oxygen)

while len(queue) > 0:
	node = queue[0]
	queue.pop(0)

	for direction in range(1, 5):
		test = (node[0] + dirs[direction][0], node[1] + dirs[direction][1])
		if distances[test[0]][test[1]] == -1 and grid[test[0]][test[1]] in ".E":
			distances[test[0]][test[1]] = distances[node[0]][node[1]] + 1
			queue.append(test)

biggest = 0
for y in range(len(distances)):
	for x in range(len(distances[0])):
		biggest = max(distances[y][x], biggest)

print(biggest)