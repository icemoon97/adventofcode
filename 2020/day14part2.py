data = [line.rstrip("\n") for line in open("input14.txt")]

mem = {}

mask = ""

def write(address, n):
	for i in range(len(address)):
		if address[i] == "X":
			address = list(address)
			address[i] = "1"
			address = "".join(address)

			write(address, n)

			address = list(address)
			address[i] = "0"
			address = "".join(address)

			write(address, n)

			return

	mem[int(address, 2)] = n


for line in data:
	line = line.split(" = ")
	if line[0] == "mask":
		mask = line[1]
	else:
		address = int(line[0].split("[")[1][:-1])
		n = int(line[1])

		address = bin(address)[2:].zfill(len(mask))

		for i in range(len(mask)):
			if mask[i] != "0":
				address = list(address)
				address[i] = mask[i]
				address = "".join(address)

		write(address, n)


print(sum(mem.values()))

