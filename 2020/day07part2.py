from collections import defaultdict

data = [line.rstrip("\n") for line in open("input07.txt")]

info = defaultdict(set)

for line in data:
	parent = line.split("contain")[0]
	children = line.split("contain")[1].split(",")
	
	if children == [' no other bags.']:
		continue

	parent = parent[:parent.index("bag")].strip(" ")

	for child in children:
		child = child.split(" ")
		
		info[parent].add((int(child[1]), " ".join(child[2:4])))

def search(bag):
	total = 1
	for child in info[bag]:
		total += child[0] * search(child[1])
	return total

print(search("shiny gold") - 1)