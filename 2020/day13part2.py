data = [line.rstrip("\n") for line in open("input13.txt")]

ids = data[1].split(",")
buses = []

for i in range(len(ids)):
	if ids[i] != "x":
		ids[i] = int(ids[i])
		buses.append(int(ids[i]))

gap = 0
offset = 0
cycle = buses[0]

for bus in buses[1:]:
	gap = ids.index(bus)

	for i in range(bus):
		n = i * cycle + offset
		if (n + gap) % bus == 0:
			offset = n
			break

	cycle *= bus

print(offset)