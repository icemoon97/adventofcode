data = [line.rstrip("\n") for line in open("input06.txt")]

data = " ".join(data).split("  ")

total = 0

for group in data:
	group = [list(x) for x in group.split()]

	shared = set(group[0])
	for x in group:
		shared = shared.intersection(x)

	total += len(shared)
	

print(total)

