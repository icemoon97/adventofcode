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

def initializeNeeded():
	needed = {}
	needed["ORE"] = 0
	for r in rs:
		item = r[1][0]
		needed[item] = 0
	return needed

def check(needed):
	for item in needed.keys():
		if needed[item] > 0 and item != "ORE":
			return False
	return True

def findOreRequired(numFuel):
	needed = initializeNeeded()
	needed["FUEL"] = numFuel
	while not check(needed):
		for item in needed.keys():
			if item != "ORE":
				if needed[item] > 0:
					reaction = findReaction(item)
					numReactions = math.ceil(needed[item] / reaction[1][1])
					for reactant in reaction[0]:
						needed[reactant[0]] += reactant[1] * numReactions
					needed[item] -= reaction[1][1] * numReactions

	return needed["ORE"]

digits = [0 for i in range(8)]

for i in range(len(digits)):
	while findOreRequired(int("".join([str(i) for i in digits]))) < 1000000000000:
		digits[i] += 1
	digits[i] -= 1

print(int("".join([str(i) for i in digits])))