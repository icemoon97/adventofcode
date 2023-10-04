from collections import defaultdict

data = [line.rstrip("\n") for line in open("input7.txt")]

order = defaultdict(list)
weightTable = {}

for line in data:
	line = line.split("->")
	line[0] = line[0].split(" ")

	parent = line[0][0]
	weight = int(line[0][1][1:-1])

	weightTable[parent] = weight

	if len(line) > 1:
		line[1] = [word.strip(" ") for word in line[1].split(",")]
		order[parent] = line[1]


for key in order.keys(): #gets a starting point
	node = key
	break

def getParent(name):
	for key in order.keys():
		if name in order[key]:
			return key
	return False

while getParent(node):
	node = getParent(node)

root = node

def getWeight(node):
	if node in order.keys():
		childWeights = [getWeight(child) for child in order[node]]
		if len(set(childWeights)) != 1:
			print(node, "is unbalanced!", childWeights, weightTable[node])
			print("children:", order[node])
			print()
		return sum(childWeights) + weightTable[node]
	else:
		return weightTable[node]
	
getWeight(root)

print(weightTable['aobgmc'] - 8)