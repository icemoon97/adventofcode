data = [line.rstrip("\n") for line in open("input03.txt")]
data = [[int(x) for x in line] for line in data]


bits = len(data[0])
gamma = ""
epsilon = ""

for i in range(bits):
	ones = sum([line[i] for line in data])
	zeros = len(data) - ones

	if ones > zeros:
		gamma += "1"
		epsilon += "0"
	else:
		epsilon += "1"
		gamma += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)