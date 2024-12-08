import itertools
from pathlib import Path
from collections import defaultdict

def cast_line(start, dir, steps, bounds):
    for i in steps:
        x, y = start[0] + dir[0] * i, start[1] + dir[1] * i
        if x < 0 or x >= bounds[0] or y < 0 or y >= bounds[1]:
            break
        yield (x, y)

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    DIM = len(data), len(data[0])

    freq = defaultdict(list)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != ".":
                freq[char].append((i, j))

    part1 = set()
    part2 = set()

    for f, nodes in freq.items():
        for a, b in itertools.combinations(nodes, 2):
            dx, dy = a[0] - b[0], a[1] - b[1]

            part1.update(cast_line(a, (dx, dy), [1], DIM))
            part1.update(cast_line(b, (-dx, -dy), [1], DIM))

            part2.update(cast_line(a, (dx, dy), itertools.count(), DIM))
            part2.update(cast_line(b, (-dx, -dy), itertools.count(), DIM))

    print(len(part1))
    print(len(part2))

if __name__ == "__main__":
    DAY = 8
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")