import math

data = [line.rstrip("\n") for line in open("input12.txt")]

pos = (0, 0)
waypoint = (10, 1)

for line in data:
	action = line[0]
	value = int(line[1:])

	if action == "N":
		waypoint = (waypoint[0], waypoint[1] + value)
	elif action == "S":
		waypoint = (waypoint[0], waypoint[1] - value)
	elif action == "E":
		waypoint = (waypoint[0] + value, waypoint[1])
	elif action == "W":
		waypoint = (waypoint[0] - value, waypoint[1])
	elif action == "L":
		angle = math.radians(value)

		x = math.cos(angle) * waypoint[0] - math.sin(angle) * waypoint[1]
		y = math.sin(angle) * waypoint[0] + math.cos(angle) * waypoint[1]

		waypoint = (x, y)
	elif action == "R":
		angle = math.radians(-value)

		x = math.cos(angle) * waypoint[0] - math.sin(angle) * waypoint[1]
		y = math.sin(angle) * waypoint[0] + math.cos(angle) * waypoint[1]

		waypoint = (x, y)
	elif action == "F":
		pos = (pos[0] + waypoint[0] * value, pos[1] + waypoint[1] * value)

print(round(abs(pos[0]) + abs(pos[1])))