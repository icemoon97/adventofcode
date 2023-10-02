with open("input01.txt", "r") as file:
    data = file.read().split("\n\n")

# elves = []

# for n in data:
#     n = n.split("\n")
#     n = [int(x) for x in n]

#     elves.append(sum(n))

# elves.sort()

# print("Part 1:", elves[-1])
# print("Part 2:", sum(elves[-3:]))

print("Part 1:", sorted([sum(map(int, elf.split("\n"))) for elf in data], reverse=True)[0])
print("Part 2:", sum(sorted([sum(map(int, elf.split("\n"))) for elf in data], reverse=True)[:3]))

