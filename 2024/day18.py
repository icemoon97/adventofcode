
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

# DIM = (7, 7)
DIM = (71, 71)

def search(grid):
    finished = False

    queue = [(0, (0, 0))]
    visited = set()
    while queue:

        steps, cur = queue.pop(0)

        if cur in visited:
            continue
        visited.add(cur)

        if cur == (DIM[0]-1, DIM[1]-1):
            # print(steps)
            finished = True
            break

        for dx, dy in DIRS:
            test = (cur[0] + dx, cur[1] + dy)

            if test[0] < 0 or test[0] >= DIM[0] or test[1] < 0 or test[1] >= DIM[1]:
                continue

            if grid[test] == ".":
                queue.append((steps + 1, test))

    return finished

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    bs = []
    for line in data:

        nums = parse_ints(line)

        # print(nums)

        bs.append(tuple(nums))

    print(len(bs))

    grid = collections.defaultdict(lambda: ".")
    # for b in bs[:1024]:
    #     grid[b] = "#"

    for i, b in enumerate(bs):
        grid[b] = "#"

        is_path = search(grid)

        # print(i, b, is_path)

        if not is_path:
            print(i, b)
            break




if __name__ == "__main__":
    DAY = 18
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")