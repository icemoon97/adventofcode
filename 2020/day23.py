from collections import deque

data = "394618527"

def part1(moves):
	cups = [int(x) for x in list(data)]

	for turn in range(moves):
		current = cups[0]
		picked_up = cups[1:4]
		cups = [cups[0]] + cups[4:]

		destination = current - 1
		while destination not in cups:
			if destination == 0:
				destination = len(cups) + 4
			destination -= 1

		cups = deque(cups)
		i = cups.index(destination)
		cups.rotate(-i)
		cups = list(cups)

		cups = [cups[0]] + picked_up + cups[1:]

		cups = deque(cups)
		cups.rotate(i)
		cups.rotate(-1)
		cups = list(cups)

	i = cups.index(1)
	return "".join([str(x) for x in cups[i + 1:] + cups[:i]])

print("Part 1:", part1(100))