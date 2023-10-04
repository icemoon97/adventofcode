data = [line.rstrip("\n") for line in open("input08.txt")][0]

width = 25
height = 6
numLayers = len(data) // (width * height)

layers = []
pos = 0
for i in range(numLayers):
	layer = [[-1 for x in range(width)] for y in range(height)]
	for y in range(height):
		for x in range(width):
			layer[y][x] = data[pos]
			pos += 1
	layers.append(layer)

image = [[-1 for x in range(width)] for y in range(height)]
for y in range(height):
	for x in range(width):
		i = 0
		while layers[i][y][x] == "2":
			i += 1
		image[y][x] = layers[i][y][x]

for y in range(height):
	for x in range(width):
		if image[y][x] == "0":
			print(" ", end=" ")
		elif image[y][x] == "1":
			print("O", end=" ")
	print()



