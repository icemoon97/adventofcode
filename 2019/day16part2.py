data = [line.rstrip("\n") for line in open("input16.txt")][0]

basePattern = [0, 1, 0, -1]

def getPattern(n, length):
	lst = []
	sign = 0
	for i in range(1, length + 1):
		if i % n == 0:
			sign = (sign + 1) % 4
		lst.append(basePattern[sign])
	return lst

digits = [int(i) for i in data] * 10000

for phase in range(100):
	print(phase)
	newLst = []
	for i in range(len(digits)):
		pattern = getPattern(i + 1, len(digits))
		total = 0
		for i, n in enumerate(pattern):
			total += digits[i] * n
		newLst.append(abs(total) % 10)
	digits = newLst
		
print("".join([str(i) for i in digits[:8]]))