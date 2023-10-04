data = [line.rstrip("\n") for line in open("input08.txt")][0]

width = 25
height = 6
numLayers = len(data) // (width * height)

pos = 0
minZeros = 9999999999999
minZerosLayer = ""
for i in range(numLayers):
	layer = [[-1 for x in range(width)] for y in range(height)]
	for y in range(height):
		for x in range(width):
			layer[y][x] = data[pos]
			pos += 1

	zeros = sum([x.count("0") for x in layer])

	if zeros < minZeros:
		minZeros = zeros
		minZerosLayer = layer

ones = sum([x.count("1") for x in minZerosLayer])
twos = sum([x.count("2") for x in minZerosLayer])

print(ones * twos)


