from pathlib import Path

def search(grid, start):
    ends = set()
    routes = 0

    queue = [start]
    while queue:
        cur = queue.pop(0)
        cur_n = grid[cur]

        if cur_n == 9:
            routes += 1
            ends.add(cur)

        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
            test = (cur[0] + dx, cur[1] + dy)

            if test in grid:
                n = grid[test]
                if n == cur_n + 1:
                    queue.append(test)

    return len(ends), routes

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    grid = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            grid[(i,j)] = int(char)

    starts = [pos for pos in grid if grid[pos] == 0]

    part1 = 0
    part2 = 0
    for s in starts:
        ends, routes = search(grid, s)
        part1 += ends
        part2 += routes

    print(part1)
    print(part2)

if __name__ == "__main__":
    DAY = 10
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")