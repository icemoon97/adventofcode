data = [line.rstrip("\n") for line in open("input08.txt")]

program = [(line.split(" ")[0], int(line.split(" ")[1])) for line in data]


def is_infinite(program):
	acc = 0
	pointer = 0
	visited = set()

	while pointer not in visited:
		visited.add(pointer)

		if pointer >= len(program):
			return (False, acc)

		command = program[pointer]
		if command[0] == "acc":
			acc += command[1]
			pointer += 1
		elif command[0] == "jmp":
			pointer += command[1]
		else:
			pointer += 1

	return (True, acc)


for i in range(len(program)):
	if program[i][0] == "nop":
		test = program.copy()
		test[i] = ("jmp", program[i][1])

		result = is_infinite(test)
		if result[0]:
			continue
		else:
			print(result[1])
	if program[i][0] == "jmp":
		test = program.copy()
		test[i] = ("nop", program[i][1])

		result = is_infinite(test)
		if result[0]:
			continue
		else:
			print(result[1])
