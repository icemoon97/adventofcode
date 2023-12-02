with open("input02.txt", "r") as file:
    data = file.read().split("\n")

start = {"red": 0, "green": 0, "blue": 0}

# total = 0
# for line in data:
#     game, cubes = line.split(":")
#     s = cubes.split(";")

#     game_id = int(game.split()[1])

#     possible = True

#     for group in s:
#         current = start.copy()

#         for item in group.split(","):
#             n, color = item.split()
#             n = int(n)

#             current[color] -= n

#         if any(val < 0 for val in current.values()):
#             possible = False

#     if possible:
#         print(game_id)
#         total += game_id

total = 0
for line in data:
    game, cubes = line.split(":")
    s = cubes.split(";")

    game_id = int(game.split()[1])

    current = start.copy()

    for group in s:
        

        for item in group.split(","):
            n, color = item.split()
            n = int(n)

            current[color] = max(n, current[color])

    print(current)

    score = current["red"] * current["green"] * current["blue"]
    print(score)

    total += score

print(total)
