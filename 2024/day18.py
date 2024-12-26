from pathlib import Path
from collections import defaultdict

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def search(grid, dim):
    start = (0, 0)

    visited = {start}
    queue = [(0, start)]

    while queue:
        steps, cur = queue.pop(0)

        if cur == dim:
            return True, steps

        for dx, dy in DIRS:
            test = (cur[0] + dx, cur[1] + dy)

            if test[0] < 0 or test[0] > dim[0] or test[1] < 0 or test[1] > dim[1]:
                continue
            if grid[test] != ".":
                continue

            if test not in visited:
                visited.add(test)
                queue.append((steps + 1, test))

    return False, -1

def sim(blocks: list[tuple[int, int]], test_input: bool = False):
    if test_input:
        dim = (6, 6)
        block_num = 12
    else:
        dim = (70, 70)
        block_num = 1024

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

def main(input_path: Path, test_input: bool = False):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    blocks = [tuple(map(int, line.split(","))) for line in data]

    sim(blocks, test_input)

if __name__ == "__main__":
    DAY = 18
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt", test_input=True)
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")