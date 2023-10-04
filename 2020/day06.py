data = [line.rstrip("\n") for line in open("input06.txt")]

data = " ".join(data).split("  ")

total = 0

for group in data:
	answers = []
	for i in range(len(group)):
		letter = group[i]
		if letter != " ":
			answers.append(letter)

	total += len(set(answers))

print(total)

