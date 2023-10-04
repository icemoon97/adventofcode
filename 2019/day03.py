data = [line.rstrip("\n") for line in open("input03.txt")]

path1 = data[0].split(",")
path2 = data[1].split(",")

direction = {
	"U": (0, 1),
	"R": (1, 0),
	"D": (0, -1),
	"L": (-1, 0)
}

def followPath(path):
	points = set()
	pos = (0, 0)
	for instruction in path:
		vector = direction[instruction[:1]]

		for i in range(int(instruction[1:])):
			pos = (pos[0] + vector[0], pos[1] + vector[1])
			points.add(pos)

	return points

wire1 = followPath(path1)
wire2 = followPath(path2)

intersections = set()
for point in wire1:
	if point in wire2:
		intersections.add(point)

lowest = 9999999999999999
for point in intersections:
	distance = abs(point[0]) + abs(point[1])
	lowest = min(lowest, distance)

print(lowest)
