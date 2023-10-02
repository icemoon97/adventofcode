with open("input05.txt", "r") as file:
    data = file.read().split("\n\n")

config, instructions = data

config = config.split("\n")
indices = config[-1].split()
n = len(indices)

def run(part2=True):
    stacks = {i : [] for i in indices}

    for line in config[:-1]:
        for i, n in enumerate(indices):
            if line[i * 4] == "[":
                char = line[i * 4 + 1]
                stacks[n].insert(0, char)

    for line in instructions.split("\n"):
        _, num, _, start, _, end = line.split()

        num = int(num)

        if part2:
            c = stacks[start][-num:]
            stacks[start] = stacks[start][:-num]
            stacks[end] += c
        else:
            for _ in range(num):
                c = stacks[start].pop()
                stacks[end].append(c)

    return "".join([stacks[n][-1] for n in indices])

print("Part 1:", run(part2=False))
print("Part 2:", run())          