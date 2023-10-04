data = [line.rstrip("\n") for line in open("input05.txt")]
data = data[0]
data = data.split(",")

for i in range(len(data)):
	data[i] = int(data[i])

def interpretOpcode(code):
	code = str(code)
	while len(code) < 5:
		code = "0" + code
	code = list(code)
	opcode = int("".join(code[3:]))
	parameterModes = [int(i) for i in code[:3]]
	parameterModes.reverse()
	return [opcode, parameterModes]

def getParameter(i, n, parameterMode):
	if parameterModes[n] == 0:
		return data[data[i + n + 1]]
	else:
		return data[i + n + 1]

programInput = 1

i = 0
while i < len(data):
	command = interpretOpcode(data[i])
	
	opcode = command[0]
	parameterModes = command[1]

	if opcode == 99:
		break
	elif opcode == 1:
		parameters = []
		for j in range(2):
			parameters.append(getParameter(i, j, parameterModes))
		parameters.append(data[i + 3])
		data[parameters[2]] = parameters[0] + parameters[1]
		i += 4
	elif opcode == 2:
		parameters = []
		for j in range(2):
			parameters.append(getParameter(i, j, parameterModes))
		parameters.append(data[i + 3])
		data[parameters[2]] = parameters[0] * parameters[1]
		i += 4
	elif opcode == 3:
		index = int(data[i + 1])
		data[index] = programInput
		i += 2
	elif opcode == 4:
		index = int(data[i + 1])
		print(data[index])
		i += 2

print(data)