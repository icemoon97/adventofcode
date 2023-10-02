from math import ceil

data = [line.rstrip("\n") for line in open("input18.txt")]

# takes string version of snail num
def explode_str(num):
	def leftVal(num, index):
		i = index - 1
		while not num[i].isnumeric():
			i -= 1
			if i < 0:
				return False
		j = i
		while num[j].isnumeric():
			j -= 1
		return [j + 1, i + 1]

	def rightVal(num, index):
		i = index + 1
		while not num[i].isnumeric():
			i += 1
			if i >= len(num):
				return False

		j = i
		while num[j].isnumeric():
			j += 1
		return [i,j]

	def remove(num, start, end):
		return num[:start] + num[end:]

	def insert(num, i, char):
		return num[:i] + str(char) + num[i:]

	count = 0

	#print("explode_str:", num)

	for i, char in enumerate(num):
		if char == "[":
			count += 1
		elif char == "]":
			count -= 1

		if count == 5:
			j = num.find("]", i)

			a, b = num[i+1:j].split(",")

			l_val = leftVal(num, i)

			if l_val:
				l_val_literal = int(num[l_val[0]:l_val[1]])
				s = int(a) + l_val_literal
				num = remove(num, l_val[0], l_val[1])
				num = insert(num, l_val[0], s)

				i += len(str(s)) - len(str(l_val_literal))

			j = num.find("]", i)
			r_val = rightVal(num, j)

			if r_val:
				s = int(b) + int(num[r_val[0]:r_val[1]])
				num = remove(num, r_val[0], r_val[1])
				num = insert(num, r_val[0], s)
				
			num = remove(num, i, j + 1)
			num = insert(num, i, "0")

			return num

	return num

def explode(num):
	str_num = str(num).replace(" ", "")
	str_num = explode_str(str_num)
	#print(str_num)
	return parse(str_num)

def parse(snail):
	if snail.isnumeric():
		return int(snail)

	i = 0
	count = 0

	while i < len(snail):
		char = snail[i]

		if char == "[":
			count += 1
		elif char == "]":
			count -= 1
		elif char == "," and count == 1:
			break

		i += 1

	left = snail[1:i]
	right = snail[i + 1:-1]

	return [parse(left), parse(right)]

def split(num):
	if isinstance(num, int):
		if num > 9:
			return [num // 2, ceil(num / 2.0)], True
		else:
			return num, False

	left, changed = split(num[0])
	if changed:
		return [left, num[1]], True

	right, changed = split(num[1])
	return [left, right], changed

def reduce(num):
	#print("reducing:", num)
	test = explode(num)

	if test != num:
		#print("exploded")
		return reduce(test)

	test, changed = split(num)
	if test != num:
		#print("split")
		return reduce(test)

	return num

def add(a, b):
	return reduce([a,b])

def magnitude(num):
	if isinstance(num, int):
		return num

	return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

def part1(data):
	snail = parse(data[0])

	for i in range(1, len(data)):
		num = parse(data[i])

		snail = add(snail, num)

	print(snail)
	print(magnitude(snail))


best = 0
data = [parse(x) for x in data]

for snail in data:
	for other in data:
		if snail == other:
			continue

		m = magnitude(add(snail, other))
		print(m)
		best = max(m, best)

print("Part 2:", best)