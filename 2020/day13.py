data = [line.rstrip("\n") for line in open("input13.txt")]

start = int(data[0])

ids = []

for i in data[1].split(","):
	if i != "x":
		ids.append(int(i))

min_time = 9999999999999999
best_bus = -1

for bus in ids:
	time = bus - start % bus
	
	if time < min_time:
		min_time = time
		best_bus = bus

print(min_time * best_bus)