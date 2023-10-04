data = [line.rstrip("\n") for line in open("input02.txt")]
data = data[0]
data = data.split(",")

for i in range(len(data)):
	data[i] = int(data[i])

target = 19690720
noun = 0
verb = 0

for noun in range(100):
	for verb in range(100):

		memory = []
		for i in range(len(data)):
			memory.append(data[i])

		memory[1] = noun
		memory[2] = verb
		print("noun:", noun, "  verb:", verb)

		i = 0
		while i < len(memory):
			command = memory[i]

			if command == 99:
				break
			elif command == 1:
				read1 = int(memory[i + 1])
				read2 = int(memory[i + 2])
				write = int(memory[i + 3])
				memory[write] = memory[read1] + memory[read2]
			elif command == 2:
				read1 = int(memory[i + 1])
				read2 = int(memory[i + 2])
				write = int(memory[i + 3])
				memory[write] = memory[read1] * memory[read2]

			i += 4

		if memory[0] == target:
			print("DONE")
			stop #yay workarounds

