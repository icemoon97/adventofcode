with open("input03.txt", "r") as file:
    data = file.read().split("\n")

total = 0

def priority(char):
    assert char.isalpha()
    if char.islower():
        return ord(char) - ord('a') + 1
    elif char.isupper():
        return ord(char) - ord("A") + 27

def run(part2=True):
    total = 0

    for i in range(0, len(data), 3 if part2 else 1):
        if part2:
            overlap = set(list(data[i])) & set(list(data[i+1])) & set(list(data[i+2]))
        else:
            line = data[i]
            n = len(line)

            first = line[:n//2]
            second = line[n//2:]
            assert len(first) == len(second)

            overlap = set(list(first)) & set(list(second))

        assert len(overlap) == 1

        char = next(iter(overlap))
        total += priority(char)

    return total

print("Part 1:", run(part2=False))
print("Part 2:", run())
