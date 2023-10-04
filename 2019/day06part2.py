data = [line.rstrip("\n") for line in open("input06.txt")]

orbits = {}

for line in data:
	line = line.split(")")

	parent = line[0]
	child = line[1]

	orbits[child] = parent

def getParents(obj):
	lst = []
	while obj in orbits.keys():
		obj = orbits[obj]
		lst.append(obj)
	return lst

path = getParents("YOU")
path.reverse()
santaPath = getParents("SAN")
santaPath.reverse()

while path[0] == santaPath[0]:
	path.pop(0)
	santaPath.pop(0)

print(len(path) + len(santaPath))
