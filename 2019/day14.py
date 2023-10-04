import math

data = [line.rstrip("\n") for line in open("input14.txt")]

rs = []

for line in data:
	reaction =  line.split("=>")
	reaction[0] = reaction[0].split(",")

	for i in range(len(reaction[0])):
		item = reaction[0][i]
		item = item.strip(" ")
		item = item.split(" ")
		item = (item[1], int(item[0]))
		reaction[0][i] = item

	reaction[1] = reaction[1].strip(" ")
	reaction[1] = reaction[1].split(" ")
	reaction[1] = (reaction[1][1], int(reaction[1][0]))
	reaction = (reaction[0], reaction[1])

	rs.append(reaction)

def findReaction(output):
	if output == "ORE":
		return ([("ORE", 1)], ("ORE"), 1)

	for r in rs:
		if r[1][0] == output:
			return r

needed = {}

needed["ORE"] = 0
for r in rs:
	item = r[1][0]
	needed[item] = 0

def check():
	for item in needed.keys():
		if needed[item] > 0 and item != "ORE":
			return False
	return True

needed["FUEL"] = 1

while not check():
	for item in needed.keys():
		if item != "ORE":
			if needed[item] > 0:
				reaction = findReaction(item)
				numReactions = math.ceil(needed[item] / reaction[1][1])
				for reactant in reaction[0]:
					needed[reactant[0]] += reactant[1] * numReactions
				needed[item] -= reaction[1][1] * numReactions


ore = needed["ORE"]
print(ore)