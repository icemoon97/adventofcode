data = [line.rstrip("\n") for line in open("input03.txt")]
data = [[int(x) for x in line] for line in data]


bits = len(data[0])

def find(data, gt, lt):
	for i in range(bits):
		ones = sum([line[i] for line in data])
		zeros = len(data) - ones

		if ones >= zeros:
			remove = gt
		else:
			remove = lt

		temp = data.copy()
		for j in range(len(temp) - 1, -1, -1):
			if temp[j][i] != remove:
				temp.pop(j)

		if len(temp) == 1:
			return int("".join([str(x) for x in temp[0]]), 2)

		data = temp

oxy = find(data.copy(), 1, 0)
co2 = find(data.copy(), 0, 1)

print(oxy * co2)