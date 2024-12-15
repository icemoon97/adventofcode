
import functools
import collections
import itertools
import numpy as np
from math import prod
from copy import deepcopy

# returns list of all ints in given string (works with negatives, not decimals)
def parse_ints(s: str):
    s = "".join([c if c.isdigit() or c == "-" else " " for c in s])
    s = [int(x) for x in s.split()]
    return s

def min_max(l):
    return min(l), max(l)

# N, E, S, W
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

from pathlib import Path

def main(input_path: Path):
    with open(input_path, "r") as file:
        raw_grid, steps = file.read().split("\n\n")

    steps = steps.replace("\n", "")
    rocks = set()

    # grid = collections.defaultdict(lambda: "#")
    grid = {}
    for i, line in enumerate(raw_grid.split("\n")):
        for j, char in enumerate(line):
            if char == "@":
                start = (i, j)
                char = "."
            elif char == "O":
                rocks.add((i, j))
                char = "."
            grid[(i,j)] = char

    # print(grid)
    print(rocks)

    dirs = {
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0)
    }


    cur = start
    for step in steps:

        # print(step, cur)

        dx, dy = dirs[step]

        test = (cur[0] + dx, cur[1] + dy)

        if grid[test] != ".":
            continue

        if test in rocks:
            # print(test)

            ray = test
            empty = False
            while ray in grid:
                if grid[ray] == "#":
                    break
                if grid[ray] == "." and ray not in rocks:
                    empty = True
                    break
                ray = (ray[0] + dx, ray[1] + dy)

            # print(ray, empty)

            if not empty:
                continue

            rocks.remove(test)
            rocks.add(ray)

        cur = test

        # print(step, cur)
        # print(sorted(rocks))


    print(sorted(rocks))


    total = 0

    for rx, ry in rocks:
        total += rx * 100 + ry

    print(total)



if __name__ == "__main__":
    DAY = 15
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")