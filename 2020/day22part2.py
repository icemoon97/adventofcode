data = [line.rstrip("\n") for line in open("input22.txt")]

data = "\n".join(data).split("\n\n")

deck1 = [int(x) for x in data[0].split("\n")[1:]]
deck2 = [int(x) for x in data[1].split("\n")[1:]]

def score(deck):
	return sum([deck[::-1][i] * (i + 1) for i in range(len(deck))])

def play_game(deck1, deck2):
	history = set()

	print(deck1, deck2)
	while len(deck1) > 0 and len(deck2) > 0:
		state = str(deck1) + str(deck2)
		if state in history:
			return 1
		history.add(state)

		c1 = deck1.pop(0)
		c2 = deck2.pop(0)

		if len(deck1) >= c1 and len(deck2) >= c2:
			print("subgame time!")
			n_deck1 = deck1.copy()[:c1]
			n_deck2 = deck2.copy()[:c2]

			sub_winner = play_game(n_deck1, n_deck2)
			if sub_winner == 1:
				deck1.extend([c1, c2])
			else:
				deck2.extend([c2, c1])
		else:
			if c1 > c2:
				deck1.extend([c1, c2])
			else:
				deck2.extend([c2, c1])

	if len(deck1) == 0:
		return 2
	else:
		return 1	

print("winner:", play_game(deck1, deck2))
print("final state:", deck1, deck2)
print("score:", score(deck1))