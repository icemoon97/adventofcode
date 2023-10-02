data = [line.rstrip("\n") for line in open("input06.txt")]
data = [int(x) for x in data[0].split(",")]

count = [0 for _ in range(9)]

for n in data:
	count[n] += 1

def sim(count, cycles):
	for cycle in range(cycles):
		next_count = [0 for _ in range(9)]

		for i in range(8, 0, -1):
			next_count[i - 1] = count[i]

		next_count[6] += count[0]
		next_count[8] += count[0]

		count = next_count

	return sum(count)

print("Part 1:", sim(count.copy(), 80))
print("Part 2:", sim(count.copy(), 256))