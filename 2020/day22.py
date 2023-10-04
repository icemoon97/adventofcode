data = [line.rstrip("\n") for line in open("input22.txt")]

data = "\n".join(data).split("\n\n")

deck1 = [int(x) for x in data[0].split("\n")[1:]]
deck2 = [int(x) for x in data[1].split("\n")[1:]]

while len(deck1) > 0 and len(deck2) > 0:
	c1 = deck1.pop(0)
	c2 = deck2.pop(0)
	if c1 > c2:
		deck1.extend([c1, c2])
	else:
		deck2.extend([c2, c1])


if len(deck1) == 0:
	winner = deck2
else:
	winner = deck1	

score = sum([winner[::-1][i] * (i + 1) for i in range(len(winner))])

print(score)