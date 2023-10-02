from helper import *
import numpy as np

with open("input09.txt", "r") as file:
	data = file.read().split("\n")

def next_tail(head, tail):
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if head == (tail[0] + x, tail[1] + y):
				return tail

	diff = (head[0] - tail[0], head[1] - tail[1])

	return (tail[0] + np.sign(diff[0]), tail[1] + np.sign(diff[1]))
	
head = (0,0)
knots = [(0,0) for _ in range(10)]

d = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

part1 = {knots[1]}
part2 = {knots[-1]}

for line in data:
	dir, dist = line.split()
	dist = int(dist)

	for step in range(dist):
		knots[0] = (knots[0][0] + d[dir][0], knots[0][1] + d[dir][1])
		for i in range(1, len(knots)):
			knots[i] = next_tail(knots[i-1], knots[i])

		part1.add(knots[1])
		part2.add(knots[-1])

print("Part 1:", len(part1))
print("Part 2:", len(part2))
