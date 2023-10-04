data = [line.rstrip("\n") for line in open("input11.txt")]

state = [[data[x][y] for y in range(len(data[0]))] for x in range(len(data))]

def print_state(state):
	for x in range(len(state)):
		for y in range(len(state[0])):
			print(state[x][y], end="")
		print()

def update(state):
	next_state = [[state[x][y] for y in range(len(data[0]))] for x in range(len(data))]

	for x in range(len(state)):
		for y in range(len(state[0])):
			adj = 0

			for i in [-1, 0, 1]:
				for j in [-1, 0, 1]:
					point = (x + i, y + j)

					if point[0] >= 0 and point[0] < len(state) and point[1] >= 0 and point[1] < len(state[0]) and point != (x,y):
						if state[point[0]][point[1]] == "#":
							adj += 1

			if state[x][y] == "L" and adj == 0:
				next_state[x][y] = "#"
			elif state[x][y] == "#" and adj >= 4:
				next_state[x][y] = "L"

	return next_state

history = set()

while "".join(["".join(x) for x in state]) not in history:
	history.add("".join(["".join(x) for x in state]))
	state = update(state)

print(sum([x.count("#") for x in state]))


