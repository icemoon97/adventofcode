import re 

data = [line.rstrip("\n") for line in open("input18.txt")]

def e(exp):
	if exp.isnumeric():
		return int(exp)
	elif "(" in exp:
		exp = exp.split(" ")
		while "" in exp:
			exp.remove("")
		
		i = exp.index("(") + 1
		count = 0

		while not (exp[i] == ")" and count == 0):
			if exp[i] == "(":
				count += 1
			elif exp[i] == ")":
				count -= 1
			i += 1
		
		section = exp[exp.index("(") + 1:i]
		mini_exp = " ".join(section)

		exp = exp[:exp.index("(")] + [str(e(mini_exp))] + exp[i + 1:]
		
		return e(" ".join(exp))

	else:
		exp = exp.split(" ")
		
		if "+" in exp:
			i = exp.index("+")
			total = int(exp[i - 1]) + int(exp[i + 1])

			exp = exp[:i - 1] + [str(total)] + exp[i + 2:]
			exp = " ".join(exp)

			return e(exp)
		else:
			i = exp.index("*")
			total = int(exp[i - 1]) * int(exp[i + 1])

			exp = exp[:i - 1] + [str(total)] + exp[i + 2:]
			exp = " ".join(exp)

			return e(exp)

total = 0

for line in data:
	line = line.replace("(", " ( ")
	line = line.replace(")", " ) ")

	total += e(line)

print(total)

	