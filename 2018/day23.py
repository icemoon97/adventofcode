input_file = "input23.txt"
# input_file = "input23test.txt"
data = [line.rstrip("\n") for line in open(input_file, "r")]

bots = []
for line in data:
    pos = tuple(int(x) for x in line[line.index("<")+1:line.index(">")].split(","))
    r = int(line[line.index("r=")+2:])

    bots.append((pos, r))

strong = max(bots, key=lambda x: x[1])

def dist(bot1, bot2):
    return sum(abs(a - b) for a, b in zip(bot1[0], bot2[0]))

count = 0
for b in bots:
    d = dist(strong, b)
    if d <= strong[1]:
        count += 1

print(count)