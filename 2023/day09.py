with open("input09.txt", "r") as file:
    data = file.read().split("\n")

part1 = 0
part2 = 0
for i, line in enumerate(data):
    seq = list(map(int, line.split()))

    layers = [seq]

    diff = seq
    while any(d != 0 for d in diff):
        diff = [b - a for a, b in zip(diff[:-1], diff[1:])]
        layers.append(diff)

    for i in range(len(layers)-2, -1, -1):
        l = layers[i]
        l.append(l[-1] + layers[i+1][-1])
        l.insert(0, l[0] - layers[i+1][0])

    part1 += layers[0][-1]
    part2 += layers[0][0]

print("Part 1:", part1)
print("Part 2:", part2)