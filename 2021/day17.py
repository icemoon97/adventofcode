data = [line.rstrip("\n") for line in open("input17.txt")][0]

def parse(data):
	data = data.split(": ")[1].split(", ")
	target = []
	for part in data:
		part = part.split("=")[1].split("..")
		part = [int(x) for x in part]
		target.append(part)
	return target

def sim(init_vel, target):
	pos = (0,0)
	vel = init_vel

	max_y = -999999999

	for t in range(250):
		pos = (pos[0] + vel[0], pos[1] + vel[1])
		if vel[0] > 0:
			vel = (vel[0] - 1, vel[1] - 1)
		elif vel[0] < 0:
			vel = (vel[0] + 1, vel[1] - 1)
		else:
			vel = (0, vel[1] - 1)

		max_y = max(pos[1], max_y)

		#print(pos)
		if in_target(pos, target):
			#print("in!")
			return True, max_y

		if pos[1] < target[1][0]:
			return False, max_y

		if pos[0] > target[0][1]:
			return False, max_y

	return False, max_y

def in_target(point, target):
	return point[0] >= target[0][0] and point[0] <= target[0][1] and point[1] >= target[1][0] and point[1] <= target[1][1]

target = parse(data)
print(target)

max_y = -1
total = 0
for x in range(target[0][1] + 1):
	for y in range(target[1][0], 250):
		success, result = sim((x,y), target)
		if success:
			total += 1
			max_y = max(result, max_y)

print("Part 1:", max_y)
print("Part 2:", total)