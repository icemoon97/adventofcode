data = [line.rstrip("\n") for line in open("input02.txt")]
data = data[0]
data = data.split(",")

for i in range(len(data)):
	data[i] = int(data[i])

data[1] = 12
data[2] = 2

i = 0
while i < len(data):
	command = data[i]
	print("command", command)

	if command == 99:
		break
	elif command == 1:
		read1 = int(data[i + 1])
		read2 = int(data[i + 2])
		write = int(data[i + 3])
		data[write] = data[read1] + data[read2]
	elif command == 2:
		read1 = int(data[i + 1])
		read2 = int(data[i + 2])
		write = int(data[i + 3])
		data[write] = data[read1] * data[read2]


	i += 4

print(data)