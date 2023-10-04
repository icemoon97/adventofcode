data = [line.rstrip("\n") for line in open("input14.txt")]

mem = {}

mask = ""

for line in data:
	line = line.split(" = ")
	if line[0] == "mask":
		mask = line[1]
	else:
		address = int(line[0].split("[")[1][:-1])
		n = int(line[1])

		b = bin(n)[2:].zfill(len(mask))
		
		for i in range(len(mask)):
			if mask[i] != "X":
				b = list(b)
				b[i] = mask[i]
				b = "".join(b)

		mem[address] = int(b, 2)

print(sum(mem.values()))

