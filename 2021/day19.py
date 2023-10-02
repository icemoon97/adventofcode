data = "\n".join([line.rstrip("\n") for line in open("input19.txt")])

data = data.split("\n\n")

scanners = {}

for unit in data:
	unit = unit.split("\n")

	sid = int(unit[0].split()[2])
	
	scanners[sid] = []

	for p in unit[1:]:
		x,y,z = p.split(",")

		scanners[sid].append((int(x),int(y),int(z)))

# links sid to dictionary that links pairs of beacons to their distance
dist = {}

for sid, lst in scanners.items():
	dist[sid] = {}

	for i, p1 in enumerate(lst):
		for j, p2 in enumerate(lst):
			if i == j:
				continue

			pair = (i, j)
			d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

			dist[sid][pair] = d

overlap = []

for sid in dist:
	for other in dist:
		if sid == other:
			continue

		l = len(set(dist[sid].values()) & set(dist[other].values()))
		if l >= 66:
			pair = (sid, other)
			overlap.append(pair)


def cycle(p):
	a,b,c = p
	yield a,b,c
	yield c,a,b
	yield b,c,a

def spins(p):
	a,b,c = p
	yield a, -b, c
	yield a, -b, -c
	yield a, c, -b
	yield -c, b, a
	yield -a, b, -c
	yield c, b, -a
	yield -b, -a, -c
	yield -a, -b, c
	yield -b, a, c
	yield b, -a, c

def rotations(p_set):
	result = [[] for _ in range(30)]

	for point in p_set:
		i = 0
		for c in cycle(point):
			for s in spins(c):
				result[i].append(s)
				i += 1

	return result

def get_common(scan_pair):
	common = (set(), set())

	for i, sid in enumerate(scan_pair):
		other = scan_pair[int(not bool(i))]

		test = dist[other].values()

		for b_pair, d in dist[sid].items():
			if d in test:
				common[i].add(b_pair[0])
				common[i].add(b_pair[1])

	return common

def calc_total_distance(sid_set, scanner):
	total = [0 for _ in range(12)]

	for i, sid in enumerate(sid_set):
		for j, other in enumerate(sid_set):
			if i == j:
				continue

			total[i] += dist[scanner][(sid, other)]

	total = zip(total, list(sid_set))
	total = sorted(total, key=lambda x : x[0])
			
	return total

def link_shared(scan_pair):
	common = get_common(scan_pair)

	z1 = calc_total_distance(common[0], scan_pair[0])
	z2 = calc_total_distance(common[1], scan_pair[1])

	linked = []

	for i in range(len(z1)):
		if z1[i][0] != z2[i][0]:
			print("problem, not shared", z1[i], z2[i])

		linked.append((scanners[scan_pair[0]][z1[i][1]], scanners[scan_pair[1]][z2[i][1]]))

	return linked

def check_offsets(a, b):
	offsets = set()
	for i in range(len(a)):
		offsets.add((a[i][0] - b[i][0], a[i][1] - b[i][1], a[i][2] - b[i][2]))

	if len(offsets) == 1:
		return list(offsets)[0]

	return False

def compare(scan_pair):
	linked = link_shared(scan_pair)

	size = 3

	subset1 = [x[0] for x in linked[:size]]
	subset2 = [x[1] for x in linked[:size]]

	#print(subset1, subset2)

	for r in rotations(subset2):
		check = check_offsets(subset1, r)

		if check:
			return check


print(overlap)

offset = compare(overlap[0])

for pair in overlap:
	print(pair)
	print(compare(pair))
