from pathlib import Path
from collections import defaultdict

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def search(grid, dim):
    visited = set()
    queue = [(0, (0, 0))]

    while queue:
        steps, cur = queue.pop(0)

        if cur in visited:
            continue
        visited.add(cur)

        if cur == dim:
            return True, steps

        for dx, dy in DIRS:
            test = (cur[0] + dx, cur[1] + dy)

            if test[0] < 0 or test[0] > dim[0] or test[1] < 0 or test[1] > dim[1]:
                continue

            if grid[test] == ".":
                queue.append((steps + 1, test))

    return False, -1

def sim(blocks: list[tuple[int, int]], part2: bool):
    if part2:
        dim = (70, 70)
        block_num = 1024
    else:
        dim = (6, 6)
        block_num = 12

    grid = defaultdict(lambda: ".")

    for b in blocks[:block_num-1]:
        grid[b] = "#"

    for i in range(block_num-1, len(blocks)):
        b = blocks[i]

        grid[b] = "#"
        is_path, steps = search(grid, dim)

        if i == block_num-1:
            print("Part 1:", steps)

        if not is_path:
            print("Part 2:", b)
            break

def main(input_path: Path, part2: bool=True):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    blocks = [tuple(map(int, line.split(","))) for line in data]

    sim(blocks, part2=part2)

if __name__ == "__main__":
    DAY = 18
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt", part2=False)
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")