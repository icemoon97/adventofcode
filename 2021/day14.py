from collections import Counter
from collections import defaultdict

data = "\n".join([line.rstrip("\n") for line in open("input14.txt")])

start, info = data.split("\n\n")
info = info.split("\n")

rules = {}

for line in info:
	a,b = line.split(" -> ")
	rules[a] = b

pairs = {}
for rule in rules:
	pairs[rule] = 0

for i in range(1, len(start)):
	char = start[i-1:i+1]
	pairs[char] += 1

def process(steps, pairs):
	for step in range(steps):
		next_pairs = {}
		for rule in rules:
			next_pairs[rule] = 0

		for pair in pairs:
			middle = rules[pair]
			next_pairs[pair[0] + middle] += pairs[pair]
			next_pairs[middle + pair[1]] += pairs[pair]

		pairs = next_pairs

	counts = defaultdict(lambda : 0)

	for pair, val in pairs.items():
		counts[pair[0]] += val
		counts[pair[1]] += val

	counts[start[0]] += 1
	counts[start[-1]] += 1

	for char, val in counts.items():
		counts[char] = val // 2

	high = -1
	low = 9999999999999999999999999999999999999999999999999
	for char, val in counts.items(): 
		high = max(val, high)
		low = min(val, low)

	return high - low

print("Part 1:", process(10, pairs.copy()))
print("Part 2:", process(40, pairs.copy()))


