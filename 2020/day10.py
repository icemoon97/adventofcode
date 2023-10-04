data = [line.rstrip("\n") for line in open("input10.txt")]

adapters = [int(x) for x in data]
adapters.sort()

adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)

diffs = []

for i in range(1, len(adapters)):
	diff = adapters[i] - adapters[i - 1]
	diffs.append(diff)

print("Part 1:", diffs.count(1) * diffs.count(3))

paths = {}
for i in range(-3, max(adapters)):
	paths[i] = 0

paths[0] = 1

for a in adapters[1:]:
	paths[a] = paths[a - 1] + paths[a - 2] + paths[a - 3]

print("Part 2:", max(paths.values()))