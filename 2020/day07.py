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
		child = " ".join(child.split(" ")[2:4])

		info[child].add(parent)
		

gold_parents = set()

def search(bag):
	for parent in info[bag]:
		if parent not in gold_parents:
			gold_parents.add(parent)
			search(parent)

search("shiny gold")

print(len(gold_parents))	