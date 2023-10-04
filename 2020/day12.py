data = [line.rstrip("\n") for line in open("input12.txt")]

pos = (0, 0)
deg = 90

for line in data:
	action = line[0]
	value = int(line[1:])

	if action == "N":
		pos = (pos[0], pos[1] + value)
	elif action == "S":
		pos = (pos[0], pos[1] - value)
	elif action == "E":
		pos = (pos[0] + value, pos[1])
	elif action == "W":
		pos = (pos[0] - value, pos[1])
	elif action == "L":
		deg -= value
		deg %= 360
	elif action == "R":
		deg += value
		deg %= 360
	elif action == "F":
		d = { 0 : (0, 1), 90 : (1, 0), 180 : (0, -1), 270 : (-1, 0) }

		pos = (pos[0] + d[deg][0] * value, pos[1] + d[deg][1] * value)

	print(pos)

print(abs(pos[0]) + abs(pos[1]))