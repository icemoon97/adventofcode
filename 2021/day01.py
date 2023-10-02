data = [line.rstrip("\n") for line in open("input01.txt")]
data = [int(x) for x in data]

def n_increment(data, window_size):
	n = 0
	prev = data[0]
	for i in range(window_size, len(data)):
		if data[i] > prev:
			n += 1

		prev = data[i - window_size + 1]

	return n

print("Part 1:", n_increment(data, 1))
print("Part 2:", n_increment(data, 3))