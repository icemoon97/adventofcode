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

def runProgram(phaseSetting, programInput):
	data = original.copy()

	phaseSettingEntered = False

	i = 0
	while i < len(data):
		command = interpretOpcode(data[i])
		
		opcode = command[0]
		parameterModes = command[1]

		if opcode == 99:
			break
		elif opcode == 1:
			index = getWriteParameter(data, i, 2, parameterModes)
			data[index] = getReadParameter(data, i, 0, parameterModes) + getReadParameter(data, i, 1, parameterModes)
			i += 4
		elif opcode == 2:
			index = getWriteParameter(data, i, 2, parameterModes)
			data[index] = getReadParameter(data, i, 0, parameterModes) * getReadParameter(data, i, 1, parameterModes)
			i += 4
		elif opcode == 3:
			index = getWriteParameter(data, i, 0, parameterModes)
			if phaseSettingEntered:
				data[index] = programInput
			else:
				data[index] = phaseSetting
				phaseSettingEntered = True
			i += 2
		elif opcode == 4:
			value = getReadParameter(data, i, 0, parameterModes)
			return value
			i += 2
		elif opcode == 5:
			if getReadParameter(data, i, 0, parameterModes) != 0:
				i = getReadParameter(data, i, 1, parameterModes)
			else:
				i += 3
		elif opcode == 6:
			if getReadParameter(data, i, 0, parameterModes) == 0:
				i = getReadParameter(data, i, 1, parameterModes)
			else:
				i += 3
		elif opcode == 7:
			index = getWriteParameter(data, i, 2, parameterModes)
			if getReadParameter(data, i, 0, parameterModes) < getReadParameter(data, i, 1, parameterModes):
				data[index] = 1
			else:
				data[index] = 0
			i += 4
		elif opcode == 8:
			index = getWriteParameter(data, i, 2, parameterModes)
			if getReadParameter(data, i, 0, parameterModes) == getReadParameter(data, i, 1, parameterModes):
				data[index] = 1
			else:
				data[index] = 0
			i += 4

biggest = 0

for phaseSetting in itertools.permutations([0, 1, 2, 3, 4]):					
	output = runProgram(phaseSetting[0], 0)

	for amp in range(4):
		output = runProgram(phaseSetting[amp + 1], output)

	biggest = max(output, biggest)
	print(phaseSetting)

print(biggest)
