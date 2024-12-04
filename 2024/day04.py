from pathlib import Path

def build_word(grid, p, diffs):
    px, py = p
    dir = [(px + dx, py + dy) for dx, dy in diffs]
    word = "".join([(grid[test] if test in grid else "") for test in dir])
    return word

def XMAS_count(grid, p):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue

            dir = [(x * i, y * i) for i in range(4)]
            word = build_word(grid, p, dir)

            if word == "XMAS":
                count += 1

    return count

def is_cross_MAS(grid, p):
    word1 = build_word(grid, p, [(0, 0), (1, 1), (2, 2)])
    word2 = build_word(grid, p, [(2, 0), (1, 1), (0, 2)])

    return (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM")

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    grid = {}

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            grid[(i,j)] = char

    part1 = 0
    part2 = 0

    for p in grid:
        part1 += XMAS_count(grid, p)
        part2 += is_cross_MAS(grid, p)   

    print(part1)
    print(part2)

if __name__ == "__main__":
    day = "04"
    print("===== Tests =====")
    main(f"tests/day{day}.txt")
    print("===== Input =====")
    main(f"inputs/day{day}.txt")