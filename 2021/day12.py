from collections import defaultdict

data = [line.rstrip("\n") for line in open("input12.txt")]

paths = defaultdict(list)
small = set()

for line in data:
	line = line.split("-")

	paths[line[0]].append(line[1])
	paths[line[1]].append(line[0])

	if line[0].islower():
		small.add(line[0])
	if line[1].islower():
		small.add(line[1])


def search(pos, visited, paths, small):
	if pos == "end":
		return 1

	s = 0
	for option in paths[pos]:

		if option in visited:
			continue

		if option in small:
			n_visited = visited.copy()
			n_visited.add(option)
			s += search(option, n_visited, paths, small)
		else:
			s += search(option, visited, paths, small)
	return s

def search2(pos, visited, visited_twice, paths, small):
	if pos == "end":
		return 1

	s = 0
	for option in paths[pos]:
		if option == "start":
			continue

		if option in visited:
			if not visited_twice:
				s += search2(option, visited, True, paths, small)

			continue

		if option in small:
			n_visited = visited.copy()
			n_visited.add(option)
			s += search2(option, n_visited, visited_twice, paths, small)
		else:
			s += search2(option, visited, visited_twice, paths, small)
	return s


v = set()
v.add("start")
print("Part 1:", search("start", v.copy(), paths, small))
print("Part 2:", search2("start", v.copy(), False, paths, small))
