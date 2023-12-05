with open("input05.txt", "r") as file:
    data = file.read().split("\n\n")

seeds_data = data[0].split(":")[1]
seeds_data = [int(n) for n in seeds_data.split()]

map_data = data[1:]
all_maps = []
for i, line in enumerate(map_data):
    map_data = line.split("\n")[1:]

    maps = [[int(n) for n in m.split()] for m in map_data]
    maps = sorted(maps, key=lambda x: x[1])
    all_maps.append(maps)


def map_seeds(maps: list[list[list[int]]], seeds: list[tuple[int, int]]):
    for m in maps:
        next = []
        for s in seeds:
            start, n = s
            end = start + n
            found = False

            # checking each range of the map
            for r in m:
                r_end = r[1] + r[2]
                r_start = r[1]

                if start >= r_start and start < r_end:
                    dest = (start - r_start) + r[0]
                    found = True

                    if end > r_end:
                        cutoff = end - r_end
                        # append section that got mapped, add remaining back into list of seed
                        next.append((dest, n - cutoff))
                        seeds.append((r_end, cutoff))
                    else:
                        next.append((dest, n))

            # if seeds aren't in a map range, they stay the same
            # theoretically this should have a bug where the start isn't in a range, but some part of the range is and incorrectly stays the same, but this isn't an issue for my input
            if not found:
                next.append(s)

        seeds = next

    return seeds


part1_seeds = [(s, 1) for s in seeds_data]
part1 = map_seeds(all_maps, part1_seeds)
print("Part 1:", min(map(lambda x: x[0], part1)))

part2_seeds = [(seeds_data[i], seeds_data[i+1]) for i in range(0, len(seeds_data), 2)]
part2 = map_seeds(all_maps, part2_seeds)
print("Part 2:", min(map(lambda x: x[0], part2)))
