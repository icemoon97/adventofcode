import math

data = [line.rstrip("\n") for line in open("input01.txt")]

def fuel(mass):
	return math.floor(mass / 3) - 2

total = 0
for line in data:
	mass = int(line)
	while fuel(mass) > 0:
		mass = fuel(mass)
		total += mass


print(total)