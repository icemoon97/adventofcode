data = [line.rstrip("\n") for line in open("input02.txt")]

def part1(data):
	depth = 0
	pos = 0

	for line in data:
		line = line.split()
		d = line[0]
		n = int(line[1])

		if d == "forward":
			pos += n
		elif d == "up":
			depth -= n
		elif d == "down":
			depth += n

	return depth * pos

def part2(data):
	depth = 0
	pos = 0
	aim = 0
	for line in data:
		line = line.split()
		d = line[0]
		n = int(line[1])

		if d == "forward":
			pos += n
			depth += aim * n
		elif d == "up":
			aim -= n
		elif d == "down":
			aim += n

	return depth * pos

print("Part 1:", part1(data))
print("Part 2:", part2(data))