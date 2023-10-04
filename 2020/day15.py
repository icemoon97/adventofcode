def game(start, end):

	history = {}

	for i, n in enumerate(start[:-1]):
		history[n] = i + 1

	current = start[-1]

	turn = len(start)

	while turn < end:
		if current in history.keys():
			next_num = turn - history[current]
		else:
			next_num = 0

		history[current] = turn
		current = next_num

		turn += 1

	return current

start_nums = [5,2,8,16,18,0,1]

print("Part 1:", game(start_nums, 2020))
print("Part 2:", game(start_nums, 30000000))