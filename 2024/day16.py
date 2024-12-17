import heapq

# N, E, S, W
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

from pathlib import Path

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    grid = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
                char = "."
            elif char == "E":
                end = (i, j)
                char = "."
            grid[(i,j)] = char

    # score, pos, last_dir, path
    queue = [(0, start, (0, 1), [start])]
    seen = set()

    best_score = -1
    best_paths = set()

    while queue:

        score, cur, last_dir, path = heapq.heappop(queue)
        seen.add((cur, last_dir))

        # print(score, cur, last_dir)

        if cur == end:
            if best_score < 0:
                best_score = score
                best_paths.update(path)
            elif score == best_score:
                best_paths.update(path)

        for d in DIRS:
            if d == (-last_dir[0], -last_dir[1]):
                continue
            
            test = (cur[0] + d[0], cur[1] + d[1])

            if grid[test] != ".":
                continue
            if (test, d) in seen:
                continue

            test_score = score + 1
            if d != last_dir:
                test_score += 1000

            heapq.heappush(queue, (test_score, test, d, path + [test]))

    print(best_score)
    print(len(best_paths))

if __name__ == "__main__":
    DAY = 16
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")