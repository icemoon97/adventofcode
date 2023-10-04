data = [line.rstrip("\n") for line in open("input01.txt")]
data = [int(x) for x in data]

for i in data:
	for j in data:
		if i != j and i + j == 2020:
			print("Part 1", i * j)
		for k in data:
			if i != j and j != k and i + j + k == 2020:
				print("Part 2", i * j * k)
