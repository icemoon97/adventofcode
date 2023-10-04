data = [line.rstrip("\n") for line in open("input05.txt")]

all_ids = []

for line in data:
	row = line[:7]
	col = line[7:]

	row = row.replace("F", "0")
	row = row.replace("B", "1")
	row = int("0b" + row, 2)

	col = col.replace("L", "0")
	col = col.replace("R", "1")
	col = int("0b" + col, 2)

	seat_id = row * 8 + col
	all_ids.append(seat_id)

print("Part 1:", max(all_ids))

all_ids.sort()
for i in range(1, len(all_ids)):
	if all_ids[i] - all_ids[i - 1] > 1:
		print("Part 2:", all_ids[i - 1])

