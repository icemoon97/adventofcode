data = "130254-678275"
data = data.split("-")

start = int(data[0])
end = int(data[1])

def valid(n):
	n = str(n)
	double = False
	noDecrease = True
	for i in range(len(n) - 1):
		if n[i] == n[i + 1]:
			double = True
		if i < len(n) - 1 and int(n[i]) > int(n[i + 1]):
			noDecrease = False

	return double and noDecrease


count = 0

for i in range(start, end):
	if valid(i):
		count += 1

print(count)
