from collections import defaultdict

data = [line.rstrip("\n") for line in open("input21.txt")]

possible = defaultdict(list)
recipies = []

all_ingredients = []

for line in data:
	line = line.split("(contains ")
	line[1] = line[1][:-1]

	ingredients = line[0].strip(" ").split(" ")
	allergens = line[1].split(", ")

	for a in allergens:
		possible[a].append(set(ingredients))

	recipies.append((ingredients, allergens))

	all_ingredients += ingredients

for allergen in possible.keys():
	lst = possible[allergen]
	s = lst[0]
	for item in lst:
		s = s.intersection(item)

	possible[allergen] = s

for i in range(len(possible)):
	for allergen in possible.keys():
		if len(possible[allergen]) == 1:
			item = max(possible[allergen])
			for l in possible.values():
				if l != possible[allergen] and item in l:
					l.remove(item)

print("part 1:", sum([1 if i not in [max(a) for a in possible.values()] else 0 for i in all_ingredients]))

keys = list(possible.keys())
keys.sort()

print("part 2:", ",".join([max(possible[key]) for key in keys]))
