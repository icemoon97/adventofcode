from pathlib import Path
from tqdm import tqdm

# returns (visited positions, is_loop)
def walk(grid, start):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_i = 0

    states = set()

    is_loop = False
    cur = start

    while cur in grid:
        state = (cur, dir_i % 4)
        if state in states:
            is_loop = True
            break
        states.add(state)

        dx, dy = dirs[dir_i % 4]
        test = (cur[0] + dx, cur[1] + dy)

        if test in grid:
            if grid[test] == "#":
                dir_i += 1
            else:
                cur = test
        else:
            # out of bounds
            break

    visited = set(pos for pos, _ in states)
    return visited, is_loop

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    grid = {}

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "^":
                start = (i,j)
                char = "."
            grid[(i,j)] = char

    base_visited, _ = walk(grid, start)
    print("Part 1:", len(base_visited))

    total = 0

    # only try obstacles in places guard originally visits
    for pos in tqdm(base_visited):
        if pos == start:
            continue

        grid[pos] = "#"
        _, is_loop = walk(grid, start)
        grid[pos] = "."

        if is_loop:
            total += 1

    print("Part 2:", total)

if __name__ == "__main__":
    DAY = 6
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")