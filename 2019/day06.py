data = [line.rstrip("\n") for line in open("input06.txt")]

orbits = {}

for line in data:
	line = line.split(")")

	parent = line[0]
	child = line[1]

	orbits[child] = parent

def numOrbits(obj):
	count = 0
	while obj in orbits.keys():
		obj = orbits[obj]
		count += 1
	return count

total = 0
for orbit in orbits:
	total += numOrbits(orbit)

print(total)