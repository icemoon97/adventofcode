data = [line.rstrip("\n") for line in open("input02.txt")]

def part1(line):
	split = line.split()
	low = int(split[0].split("-")[0])
	high = int(split[0].split("-")[1])
	letter = split[1][0]
	password = split[2]

	return password.count(letter) >= low and password.count(letter) <= high

def part2(line):
	split = line.split()
	pos1 = int(split[0].split("-")[0])
	pos2 = int(split[0].split("-")[1])
	letter = split[1][0]
	password = split[2]


	return (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter)

	return False

part1_valid = 0
part2_valid = 0

for line in data:
	if part1(line):
		part1_valid += 1
	if part2(line):
		part2_valid += 1

print("Part 1:", part1_valid)
print("Part 2:", part2_valid)



