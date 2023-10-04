with open("input19.txt", "r") as file:
	data = file.read().split("\n\n")

rules_data = data[0].split("\n")
messages = data[1].split("\n")

rules = {}

for line in rules_data:
	n, rule = line.split(": ")

	rule = [i.replace("\"", "").split() for i in rule.split("|")]
	rules[n] = rule

for rule_name, rule in rules.items():
	for part in rule:
		if len(part) != 2:
			print(rule_name, rule)

def check(msg, rules):
	if not msg:
		return False

	n = len(msg)

	grid = [[set() for _ in range(n)] for _ in range(n)]

	for i, char in enumerate(msg):
		for rule_name, rule in rules.items():
			if any([char in j for j in rule]):
				grid[0][i].add(rule_name)

	for l in range(1, n):
		for i in range(n - l):
			for j in range(l):

				for rule_name, rule in rules.items():
					first = grid[j][i]
					second = grid[l - j - 1][i + 1 + j]

					for part in rule:
						# fairly sure this part is wrong because it's not a normal part of chomsky form
						if len(part) == 1 and (part[0] in first or part[0] in second):
							grid[l][i].add(rule_name)

						if len(part) == 2 and part[0] in first and part[1] in second:
							grid[l][i].add(rule_name)

	return "0" in grid[n-1][0]

# n = 0	
# for i, msg in enumerate(messages):
# 	valid = check(msg, rules)
# 	if valid:
# 		n += 1
# 	print(i, msg, valid)

# print("Part 1:", n)