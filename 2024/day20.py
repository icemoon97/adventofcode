import collections
import itertools

# N, E, S, W
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

from pathlib import Path

def search_normal(grid, start):
    queue = [(0, start)]
    best = collections.defaultdict(lambda: 999999999)

    while queue:

        steps, cur = queue.pop(0)

        if best[cur] <= steps:
            continue
        best[cur] = steps

        for dx, dy in DIRS:
            test = (cur[0] + dx, cur[1] + dy)

            if grid[test] == ".":
                queue.append((steps+1, test))

    return best

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    grid = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
                char = '.'
            elif char == "E":
                end = (i, j)
                char = '.'
            grid[(i,j)] = char

    normal_steps = search_normal(grid, start)

    results = collections.defaultdict(lambda: 0)

    open_pos = [p for p in grid if grid[p] == "."]
    for p1, p2 in itertools.combinations(open_pos, 2):
        if grid[p1] != "." or grid[p2] != ".":
            continue

        dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        if dist > 20:
            continue

        steps1 = normal_steps[p1]
        steps2 = normal_steps[p2]

        saves = abs(steps1 - steps2) - dist
        if saves >= 50 and saves < 999999:
            results[saves] += 1

    for k, v in sorted(results.items()):
        print(f"saves {k}: {v}")

    total = 0
    for k, v in results.items():
        if k >= 100:
            total += v

    print(total)


if __name__ == "__main__":
    DAY = 20
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")