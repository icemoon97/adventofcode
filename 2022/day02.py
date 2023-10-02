with open("input02.txt", "r") as file:
    data = file.read().split("\n")

def run(part2=True):
    score = 0

    for line in data:
        opp, me = line.split()

        opp = ord(opp) - ord("A")
        me = ord(me) - ord("X")

        if part2:
            me = (opp + me + 2) % 3

        if (opp + 1) % 3 == me:
            score += 6
        elif opp == me:
            score += 3
        
        score += me + 1

    return score

print("Part 1:", run(part2=False))
print("Part 2:", run())

