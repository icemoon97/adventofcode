with open("input02.txt", "r") as file:
    data = file.read().split("\n")

def part1(data):
    start = {"red": 12, "green": 13, "blue": 14}

    total = 0
    for line in data:
        game, info = line.split(":")
        game_id = int(game.split()[1])

        possible = True

        for group in info.split(";"):
            current = start.copy()

            for cubes in group.split(","):
                n, color = cubes.split()
                current[color] -= int(n)

            if any(val < 0 for val in current.values()):
                possible = False

        if possible:
            total += game_id

    return total

def part2(data):
    start = {"red": 0, "green": 0, "blue": 0}

    total = 0
    for line in data:
        _, info = line.split(":")
        current = start.copy()

        for group in info.split(";"):
            for cubes in group.split(","):
                n, color = cubes.split()
                current[color] = max(int(n), current[color])

        score = current["red"] * current["green"] * current["blue"]
        total += score

    return total

print("Part 1:", part1(data))
print("Part 2:", part2(data))
