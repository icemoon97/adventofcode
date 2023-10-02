data = [line.rstrip("\n") for line in open("input07.txt")]
data = [int(x) for x in data[0].split(",")]

def calc_cost(data, calc_fuel):
	min_fuel = 99999999999999
	for target in range(max(data)):
		fuel = 0
		for n in data:
			diff = abs(n - target)
			fuel += calc_fuel(diff)

		min_fuel = min(min_fuel, fuel)

	return min_fuel


print("Part 1:", calc_cost(data, lambda x : x))
print("Part 2:", calc_cost(data, lambda x : int(x * (x + 1) / 2)))