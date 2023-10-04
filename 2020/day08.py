data = [line.rstrip("\n") for line in open("input08.txt")]

program = [(line.split(" ")[0], int(line.split(" ")[1])) for line in data]

acc = 0
pointer = 0
visited = set()

while pointer not in visited:
	visited.add(pointer)
	command = program[pointer]
	if command[0] == "acc":
		acc += command[1]
		pointer += 1
	elif command[0] == "jmp":
		pointer += command[1]
	else:
		pointer += 1

print(acc)
