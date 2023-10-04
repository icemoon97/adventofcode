data = [line.rstrip("\n") for line in open("input11.txt")]

state = [[data[x][y] for y in range(len(data[0]))] for x in range(len(data))]

def print_state(state):
	for x in range(len(state)):
		for y in range(len(state[0])):
			print(state[x][y], end="")
		print()

def adj(state, point):
	adj = 0

	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if i == 0 and j == 0:
				continue

			direction = (i, j)

			test = (point[0] + direction[0], point[1] + direction[1])

			while test[0] in range(0, len(state)) and test[1] in range(0, len(state[0])):
				if state[test[0]][test[1]] == "#":
					adj += 1
					break

				if state[test[0]][test[1]] == "L":
					break

				test = (test[0] + direction[0], test[1] + direction[1])

	return adj

def update(state):
	next_state = [[state[x][y] for y in range(len(data[0]))] for x in range(len(data))]

	for x in range(len(state)):
		for y in range(len(state[0])):
			n = adj(state, (x, y))

			if state[x][y] == "L" and n == 0:
				next_state[x][y] = "#"
			elif state[x][y] == "#" and n >= 5:
				next_state[x][y] = "L"

	return next_state

history = set()

while "".join(["".join(x) for x in state]) not in history:
	history.add("".join(["".join(x) for x in state]))
	state = update(state)

print(sum([x.count("#") for x in state]))

