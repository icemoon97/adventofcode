import itertools

original = [line.rstrip("\n") for line in open("input07.txt")]
original = original[0]
original = original.split(",")

for i in range(len(original)):
	original[i] = int(original[i])

def interpretOpcode(code):
	code = str(code)
	while len(code) < 5:
		code = "0" + code
	code = list(code)
	opcode = int("".join(code[3:]))
	parameterModes = [int(i) for i in code[:3]]
	parameterModes.reverse()
	return [opcode, parameterModes]

def getReadParameter(data, i, n, parameterModes):
	if parameterModes[n] == 0:
		index = data[i + n + 1]
		return data[index]
	elif parameterModes[n] == 1:
		return data[i + n + 1]

def getWriteParameter(data, i, n, parameterModes):
	return data[i + n + 1]

class Amp:
	def __init__(self, name, phaseSetting):
		self.name = name
		self.phaseSetting = phaseSetting

		self.data = original.copy()
		self.i = 0
		self.inputBuffer = []
		self.done = False
		self.next = ""
		self.phaseSettingEntered = False

	def run(self):
		print("Amp", self.name, self.inputBuffer)
		while self.i < len(self.data):
			command = interpretOpcode(self.data[self.i])
			
			opcode = command[0]
			parameterModes = command[1]

			if opcode == 99:
				break
			elif opcode == 1:
				index = getWriteParameter(self.data, self.i, 2, parameterModes)
				self.data[index] = getReadParameter(self.data, self.i, 0, parameterModes) + getReadParameter(self.data, self.i, 1, parameterModes)
				self.i += 4
			elif opcode == 2:
				index = getWriteParameter(self.data, self.i, 2, parameterModes)
				self.data[index] = getReadParameter(self.data, self.i, 0, parameterModes) * getReadParameter(self.data, self.i, 1, parameterModes)
				self.i += 4
			elif opcode == 3:
				index = getWriteParameter(self.data, self.i, 0, parameterModes)
				if self.phaseSettingEntered:
					self.data[index] = self.inputBuffer[0]
					self.inputBuffer.pop(0)
				else:
					self.data[index] = self.phaseSetting
					self.phaseSettingEntered = True
				self.i += 2
			elif opcode == 4:
				value = getReadParameter(self.data, self.i, 0, parameterModes)
				self.next.inputBuffer.append(value)
				self.i += 2
				return
			elif opcode == 5:
				if getReadParameter(self.data, self.i, 0, parameterModes) != 0:
					self.i = getReadParameter(self.data, self.i, 1, parameterModes)
				else:
					self.i += 3
			elif opcode == 6:
				if getReadParameter(self.data, self.i, 0, parameterModes) == 0:
					self.i = getReadParameter(self.data, self.i, 1, parameterModes)
				else:
					self.i += 3
			elif opcode == 7:
				index = getWriteParameter(self.data, self.i, 2, parameterModes)
				if getReadParameter(self.data, self.i, 0, parameterModes) < getReadParameter(self.data, self.i, 1, parameterModes):
					self.data[index] = 1
				else:
					self.data[index] = 0
				self.i += 4
			elif opcode == 8:
				index = getWriteParameter(self.data, self.i, 2, parameterModes)
				if getReadParameter(self.data, self.i, 0, parameterModes) == getReadParameter(self.data, self.i, 1, parameterModes):
					self.data[index] = 1
				else:
					self.data[index] = 0
				self.i += 4

		self.done = True


biggest = 0

for phaseSetting in itertools.permutations([5, 6, 7, 8, 9]):	
	amps = [
		Amp("A", phaseSetting[0]), 
		Amp("B", phaseSetting[1]), 
		Amp("C", phaseSetting[2]), 
		Amp("D", phaseSetting[3]), 
		Amp("E", phaseSetting[4])]	
	amps[0].next = amps[1]
	amps[1].next = amps[2]
	amps[2].next = amps[3]
	amps[3].next = amps[4]
	amps[4].next = amps[0]

	amps[0].inputBuffer.append(0)

	while not amps[0].done:
		for amp in amps:
			if len(amp.inputBuffer) > 0:
				amp.run()

	biggest = max(biggest, amps[0].inputBuffer[0])
	

print(biggest)
