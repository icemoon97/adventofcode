import functools

start = (1, 10)  # player 1, player 2

def run_game(pos1, pos2, score1, score2, die):
	if score2 >= 1000:
		return score1 * die

	roll = (die % 100) * 3 + 6  # add 6 because 6 = 3 + 2 + 1
	pos1 = (pos1 + roll - 1) % 10 + 1

	return run_game(pos2, pos1, score2, score1 + pos1, die + 3)

print("Part 1:", run_game(start[0], start[1], 0, 0, 0))

# value, frequency of 3 rolls of 3 sided die
rolls = {
	3 : 1,
	4 : 3,
	5 : 6,
	6 : 7,
	7 : 6,
	8 : 3,
	9 : 1
}

# returns (number of p1 wins, number of p2 wins)
@functools.lru_cache(maxsize=None)
def quantum_game(pos1, pos2, score1, score2):
	if score2 >= 21:
		return 0, 1

	wins = [0, 0]
	for roll, count in rolls.items():
		h_pos1 = (pos1 + roll - 1) % 10 + 1

		result = quantum_game(pos2, h_pos1, score2, score1 + h_pos1)
		# result is (p2 wins, p1 wins) because of player swap
		wins[0] += result[1] * count
		wins[1] += result[0] * count
		
	return wins

wins = quantum_game(start[0], start[1], 0, 0)
print("Part 2:", max(wins))




# def run_game(start):
# 	pos = [start[0], start[1]]
# 	score = [0, 0]
# 	die = 1

# 	turn = 0  # 0 for player 1, 1 for player 2

# 	total_rolls = 0

# 	def roll(die):
# 		r = 0
# 		for _ in range(3):
# 			r += die
# 			die += 1
# 			die = (die - 1) % 100 + 1
# 		return r, die

# 	while max(score) < 1000:
# 		r, die = roll(die)
# 		total_rolls += 3
		
# 		pos[turn] += r
# 		pos[turn] = (pos[turn] - 1) % 10 + 1

# 		score[turn] += pos[turn]

# 		turn = int(not bool(turn))

# 	return total_rolls * min(score)