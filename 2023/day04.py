with open("input04.txt", "r") as file:
    data = file.read().split("\n")

total = 0
cards = [1 for _ in range(len(data))]

for i, line in enumerate(data):
    _, nums = line.split(":")
    win, mine = nums.split("|")

    win = [int(n) for n in win.split()]
    mine = [int(n) for n in mine.split()]

    matches = [n for n in mine if n in win]
    n = len(matches)

    if n > 0:
        total += 2**(n-1)

    for j in range(n):
        cards[i+1+j] += cards[i]

print("Part 1:", total)
print("Part 2:", sum(cards))
