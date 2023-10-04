from collections import defaultdict

data = [line.rstrip("\n") for line in open("input16.txt")]
data = [line.split("\n") for line in "\n".join(data).split("\n\n")]

rules = data[0]
my_ticket = data[1][1:]
tickets = data[2][1:]

def t():
	return False

valid = defaultdict(t)

for rule in rules:
	rule = [x.strip(" ") for x in rule.split(":")]

	range1 = [int(x) for x in rule[1].split(" or ")[0].split("-")]
	range2 = [int(x) for x in rule[1].split(" or ")[1].split("-")]

	for i in range(range1[0], range1[1] + 1):
		valid[i] = True
	for i in range(range2[0], range2[1] + 1):
		valid[i] = True

error = 0

for ticket in tickets:
	ticket = [int(x) for x in ticket.split(",")]
	
	for n in ticket:
		if not valid[n]:
			error += n

print(error)
