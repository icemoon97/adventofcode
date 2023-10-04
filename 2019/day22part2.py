from collections import deque

data = [line.rstrip("\n") for line in open("input22.txt")]

numCards = 10007
pos = 4649

offset = 0
increment = 0

for line in data:
	line = line.split(" ")
	if line[0] == "deal":
		if line[1] == "into":
			increment *= -1
			offset += increment
		elif line[1] == "with":
			n = int(line[3])
			increment += n
			deck = increment(deck, n)
	elif line[0] == "cut":
		n = int(line[1])
		deck.rotate(-n)

print(deck.index(2019))