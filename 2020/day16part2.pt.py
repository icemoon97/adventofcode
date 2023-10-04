from collections import defaultdict

data = [line.rstrip("\n") for line in open("input16.txt")]
data = [line.split("\n") for line in "\n".join(data).split("\n\n")]

rules = data[0]
my_ticket = [int(x) for x in data[1][1].split(",")]
tickets = data[2][1:]

def t():
	return False

valid = defaultdict(t)

for i in range(len(rules)):
	rule = rules[i]
	rule = [x.strip(" ") for x in rule.split(":")]

	range1 = [int(x) for x in rule[1].split(" or ")[0].split("-")]
	range2 = [int(x) for x in rule[1].split(" or ")[1].split("-")]

	rules[i] = (rule[0], range1, range2)

	for i in range(range1[0], range1[1] + 1):
		valid[i] = True
	for i in range(range2[0], range2[1] + 1):
		valid[i] = True

valid_tickets = []

tickets = [[int(x) for x in ticket.split(",")] for ticket in tickets]

for ticket in tickets:
	if all([valid[n] for n in ticket]):
		valid_tickets.append(ticket)


valid_rules = defaultdict(set)

for col in range(len(tickets[0])):
	nums = [ticket[col] for ticket in valid_tickets]
	
	for rule in rules:
		range1 = [n >= rule[1][0] and n <= rule[1][1] for n in nums]
		range2 = [n >= rule[2][0] and n <= rule[2][1] for n in nums]
		in_range = [range1[i] or range2[i] for i in range(len(range1))]

		if all(in_range):
			valid_rules[col].add(rule[0])

for i in range(len(valid_rules)):
	for rules in valid_rules.values():
		if len(rules) == 1:
			for key in valid_rules.keys():
				if valid_rules[key] != rules:
					valid_rules[key].discard(list(rules)[0])

product = 1

for key in valid_rules.keys():
	if "departure" in list(valid_rules[key])[0]:
		product *= my_ticket[key]

print(product)