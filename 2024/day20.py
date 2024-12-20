
import heapq
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

    print(start, end)

    # steps, pos, skip_mode, skip_loc
    queue = [(0, start, False, tuple())]
    visited = set()

    results = collections.defaultdict(lambda: 0)

    normal_steps = search_normal(grid, start)
    no_cheat = normal_steps[end]
    print("no cheat:", no_cheat)

    while queue:

        steps, cur, skip_mode, skip_loc = heapq.heappop(queue)

        if normal_steps[cur] < steps:
            continue

        state = (cur, skip_mode, skip_loc)
        if state in visited:
            continue
        visited.add(state)

        if cur == end:
            saves = no_cheat - steps
            # print(f"skip: {skip_loc}, save {saves}")
            # if saves > 50:
            #     print(cur, steps, skip_mode, skip_loc)
            results[saves] += 1

        for dx, dy in DIRS:
            test = (cur[0] + dx, cur[1] + dy)

            if test not in grid:
                continue

            if skip_mode and grid[test] == ".":
                queue.append((steps+1, test, False, (*skip_loc, test)))

            else:

                if grid[test] == ".":
                    queue.append((steps+1, test, skip_mode, skip_loc))
                elif grid[test] == "#" and len(skip_loc) == 0:
                    queue.append((steps+1, test, True, (test,)))

    print(results)
        




if __name__ == "__main__":
    DAY = 20
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")