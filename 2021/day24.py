data = [line.rstrip("\n") for line in open("input24.txt")]

def run(instructions, inputs, skip=0):
	mem = {
		"x" : 0,
		"y" : 0,
		"z" : 0,
		"w" : 0
	}

	inputs = [int(x) for x in list(str(inputs))]

	skips = []
	for i, line in enumerate(instructions):
		if line == "inp w":
			skips.append(i)

	#print(skips)

	if skip > 0:
		mem["x"] = 1
		mem["y"] = inputs[0] + 1
		mem["z"] = inputs[0] + 1
	if skip > 1:
		mem["y"] = inputs[1] + 11
		mem["z"] *= 26
		mem["z"] += mem["y"]
	if skip > 2:
		mem["y"] = inputs[2] + 1
		mem["z"] *= 26
		mem["z"] += mem["y"]
	if skip > 3:
		mem["y"] = inputs[3] + 11
		mem["z"] *= 26
		mem["z"] += mem["y"]
	if skip > 4:
		if (mem["z"] % 26) - 8 == inputs[4]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["z"] *= 25 + mem["x"]
		mem["y"] = (inputs[4] + 2) * mem["x"]
		mem["z"] += mem["y"]

	if skip > 5:
		if (mem["z"] % 26) - 5 == inputs[5]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["y"] = 25 * mem["x"] + 1
		mem["z"] *= mem["y"]
		mem["y"] = (inputs[5] + 9) * mem["x"]
		mem["z"] += mem["y"]

	if skip > 6:
		mem["x"] = 1
		mem["z"] *= 26
		mem["y"] = inputs[6] + 7
		mem["z"] += mem["y"]
	if skip > 7:
		if (mem["z"] % 26) - 13 == inputs[7]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["y"] = 25 * mem["x"] + 1
		mem["z"] *= mem["y"]
		mem["y"] = (inputs[7] + 11) * mem["x"]
		mem["z"] += mem["y"]
	if skip > 8:
		mem["x"] = 1
		mem["z"] *= 26
		mem["y"] = inputs[7] + 6
		mem["z"] += mem["y"]
	if skip > 9:
		if (mem["z"] % 26) - 1 == inputs[9]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["y"] = 25 * mem["x"] + 1
		mem["z"] *= mem["y"]
		mem["y"] = (inputs[9] + 15) * mem["x"]
		mem["z"] += mem["y"]
	if skip > 10:
		mem["x"] = 1
		mem["z"] *= 26
		mem["y"] = inputs[10] + 7
		mem["z"] += mem["y"]
	if skip > 11:
		if (mem["z"] % 26) - 5 == inputs[11]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["y"] = 25 * mem["x"] + 1
		mem["z"] *= mem["y"]
		mem["y"] = (inputs[11] + 1) * mem["x"]
		mem["z"] += mem["y"]
	if skip > 12:
		if (mem["z"] % 26) - 4 == inputs[12]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["y"] = 25 * mem["x"] + 1
		mem["z"] *= mem["y"]
		mem["y"] = (inputs[12] + 8) * mem["x"]
		mem["z"] += mem["y"]
	if skip > 13:
		if (mem["z"] % 26) - 8 == inputs[13]:
			mem["x"] = 0
		else:
			mem["x"] = 1

		mem["z"] = mem["z"] // 26
		mem["y"] = 25 * mem["x"] + 1
		mem["z"] *= mem["y"]
		mem["y"] = (inputs[13] + 6) * mem["x"]
		mem["z"] += mem["y"]


	for _ in range(skip):
		inputs.pop(0)

	for i, line in enumerate(instructions[skips[skip]:]):
		if line == "":
			continue
		if line[0] == "#":
			continue

		if i + skips[skip] in skips:
			#print(skips.index(i + skips[skip]), mem)
			pass

		line = line.split()

		if len(line) == 2:
			op, var = line

			mem[var] = int(inputs.pop(0))
		elif len(line) == 3:
			op, des, var = line

			if var.replace("-","").isnumeric():
				var = int(var)
			else:
				var = mem[var]

			if op == "add":
				mem[des] += var
			elif op == "mul":
				mem[des] *= var
			elif op == "div":
				mem[des] = mem[des] // var
			elif op == "mod":
				mem[des] %= var
			elif op == "eql":
				mem[des] = int(mem[des] == var)

	return mem

def run_sim(model_num):
	inputs = [int(x) for x in list(str(model_num))]

	x = y = z = 0

	# 1
	x = 1
	y = inputs[0] + 1
	z = inputs[0] + 1
	# 2
	y = inputs[1] + 11
	z *= 26
	z += y
	# 3
	y = inputs[2] + 1
	z *= 26
	z += y
	# 4
	y = inputs[3] + 11
	z *= 26
	z += y
	# 5
	if (z % 26) - 8 == inputs[4]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[4] + 2) * x
	z += y
	# 6
	if (z % 26) - 5 == inputs[5]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[5] + 9) * x
	z += y
	# 7
	x = 1
	z *= 26
	y = inputs[6] + 7
	z += y
	# 8
	if (z % 26) - 13 == inputs[7]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[7] + 11) * x
	z += y
	# 9
	x = 1
	z *= 26
	y = inputs[8] + 6
	z += y
	# 10
	if (z % 26) - 1 == inputs[9]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[9] + 15) * x
	z += y
	# 11
	x = 1
	z *= 26
	y = inputs[10] + 7
	z += y
	# 12
	if (z % 26) - 5 == inputs[11]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[11] + 1) * x
	z += y
	# 13
	if (z % 26) - 4 == inputs[12]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[12] + 8) * x
	z += y
	# 14
	if (z % 26) - 8 == inputs[13]:
		x = 0
	else:
		x = 1

	z = z // 26
	y = 25 * x + 1
	z *= y
	y = (inputs[13] + 6) * x
	z += y

	return {"x" : x, "y" : y, "z" : z}

max_key = 92969593497992

mem = run(data, max_key)
print(mem)
mem = run_sim(max_key)
print(mem)

min_key = 81514171161381

mem = run(data, min_key)
print(mem)
mem = run_sim(min_key)
print(mem)