with open("input01.txt", "r") as file:
    data = file.read().split("\n")

d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

part1 = 0
part2 = 0
for line in data:
    p1_nums = []
    p2_nums = []

    for i, char in enumerate(line):
        if char.isdigit():
            p1_nums.append(int(char))
            p2_nums.append(int(char))

        for k, v in d.items():
            if line[i:].startswith(k):
                p2_nums.append(v)

    part1 += p1_nums[0] * 10 + p1_nums[-1]
    part2 += p2_nums[0] * 10 + p2_nums[-1]

print("Part 1:", part1)
print("Part 2:", part2)
