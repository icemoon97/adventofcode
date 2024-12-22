from pathlib import Path
from collections import defaultdict

def main(input_path: Path):
    with open(input_path, "r") as file:
        bits, lines = file.read().split("\n\n")

    bits = bits.split(", ")

    part1 = 0
    part2 = 0

    for line in lines.split("\n"):
        dp = defaultdict(lambda: 0)
        dp[0] = 1

        for i in range(len(line)):
            for b in bits:
                if line[i:].startswith(b):
                    dp[i+len(b)] += dp[i]

        part1 += bool(dp[len(line)])
        part2 += dp[len(line)]

    print("Part 1:", part1)
    print("Part 2:", part2)

if __name__ == "__main__":
    DAY = 19
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")