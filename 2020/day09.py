data = [line.rstrip("\n") for line in open("input09.txt")]
data = [int(x) for x in data]

def valid(lst, n):
	for i in lst:
		for j in lst:
			if i == j:
				continue
			if i + j == n:
				return True

	return False

length = 25
invalid = -1

for i in range(length, len(data)):
	lst = data[i - length:i]
	if not valid(lst, data[i]):
		invalid = data[i]

print("Part 1:", invalid)

for size in range(2, 25):
	for i in range(len(data) - size):
		section = data[i:i + size]
		if sum(section) == invalid:
			section.sort()
			print("Part 2:", section[0] + section[len(section) - 1])
			break

