with open("input10.txt", "r") as file:
	data = file.read().split("\n")

instr = [0]

for line in data:
    line = line.split()
    if line[0] == "addx":
        instr += [0, int(line[1])]
    else:
        instr += [0]

part1 = 0
cols, rows = 40, 6
screen = [[" "] * cols for _ in range(rows)]

x = 1

for cycle, n in enumerate(instr):
    if (cycle - 20) % 40 == 0:
        part1 += cycle * x

    sprite = (cycle % cols) - x
    if sprite >= 0 and sprite <= 2:
        screen[cycle // cols][cycle % cols] = "█"

    x += n

print("Part 1:", part1)
for line in screen:
    print("".join([x * 2 for x in line[1:]]))