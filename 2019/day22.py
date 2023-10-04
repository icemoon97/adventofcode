from collections import deque

data = [line.rstrip("\n") for line in open("input22.txt")]

deck = deque(range(10007))

def increment(deck, n):
	new = ["" for i in range(len(deck))]
	for i in range(len(deck)):
		new[(i * n) % len(deck)] = deck[i]
	return deque(new)

for line in data:
	line = line.split(" ")
	if line[0] == "deal":
		if line[1] == "into":
			deck.reverse()
		elif line[1] == "with":
			n = int(line[3])
			deck = increment(deck, n)
	elif line[0] == "cut":
		n = int(line[1])
		deck.rotate(-n)

print(deck.index(2019))