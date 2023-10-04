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
	points = {}
	pos = (0, 0)
	step = 0
	for instruction in path:
		vector = direction[instruction[:1]]

		for i in range(int(instruction[1:])):
			step += 1
			pos = (pos[0] + vector[0], pos[1] + vector[1])
			points[pos] = step

	return points

wire1 = followPath(path1)
wire2 = followPath(path2)

intersections = {}
for point in wire1.keys():
	if point in wire2.keys():
		intersections[point] = wire1[point] + wire2[point]

lowest = 9999999999999999
for point in intersections:
	lowest = min(lowest, intersections[point])

print(lowest)
