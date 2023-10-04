original = [line.rstrip("\n") for line in open("input09.txt")]
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

def getReadParameter(data, i, n, parameterModes, base):
	if parameterModes[n] == 0:
		index = data[i + n + 1]
		return data[index]
	elif parameterModes[n] == 1:
		return data[i + n + 1]
	elif parameterModes[n] == 2:
		index = data[i + n + 1] + base
		return data[index]

def getWriteParameter(data, i, n, parameterModes, base):
	if parameterModes[n] == 0:
		return data[i + n + 1]
	elif parameterModes[n] == 2:
		return data[i + n + 1] + base

def runProgram(programInput):
	data = original.copy()

	for i in range(5000):
		data.append(0)

	base = 0

	i = 0
	while i < len(data):
		command = interpretOpcode(data[i])
		
		opcode = command[0]
		parameterModes = command[1]

		if opcode == 99:
			break
		elif opcode == 1:
			index = getWriteParameter(data, i, 2, parameterModes, base)
			data[index] = getReadParameter(data, i, 0, parameterModes, base) + getReadParameter(data, i, 1, parameterModes, base)
			i += 4
		elif opcode == 2:
			index = getWriteParameter(data, i, 2, parameterModes, base)
			data[index] = getReadParameter(data, i, 0, parameterModes, base) * getReadParameter(data, i, 1, parameterModes, base)
			i += 4
		elif opcode == 3:
			data[getWriteParameter(data, i, 0, parameterModes, base)] = programInput
			i += 2
		elif opcode == 4:
			value = getReadParameter(data, i, 0, parameterModes, base)
			print("OUTPUT:", value)
			i += 2
		elif opcode == 5:
			if getReadParameter(data, i, 0, parameterModes, base) != 0:
				i = getReadParameter(data, i, 1, parameterModes, base)
			else:
				i += 3
		elif opcode == 6:
			if getReadParameter(data, i, 0, parameterModes, base) == 0:
				i = getReadParameter(data, i, 1, parameterModes, base)
			else:
				i += 3
		elif opcode == 7:
			index = getWriteParameter(data, i, 2, parameterModes, base)
			if getReadParameter(data, i, 0, parameterModes, base) < getReadParameter(data, i, 1, parameterModes, base):
				data[index] = 1
			else:
				data[index] = 0
			i += 4
		elif opcode == 8:
			index = getWriteParameter(data, i, 2, parameterModes, base)
			if getReadParameter(data, i, 0, parameterModes, base) == getReadParameter(data, i, 1, parameterModes, base):
				data[index] = 1
			else:
				data[index] = 0
			i += 4
		elif opcode == 9:
			base += getReadParameter(data, i, 0, parameterModes, base)
			i += 2

runProgram(2)
