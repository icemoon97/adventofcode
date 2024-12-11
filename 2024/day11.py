from pathlib import Path
from collections import defaultdict
import math

def split_digits(n: int):
    s = str(n)
    i = len(s)//2
    return int(s[:i]), int(s[i:])

def blink(stones: list[int], steps: int) -> int:
    counts = defaultdict(lambda: 0, {s : 1 for s in stones})

    for _ in range(steps):
        post = defaultdict(lambda: 0)

        for s, num in counts.items():
            if s == 0:
                post[1] += num
            elif len(str(s)) % 2 == 0:
                a, b = split_digits(s)
                post[a] += num
                post[b] += num
            else:
                post[s * 2024] += num

        counts = post

    return sum(counts.values())

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split()

    stones = list(map(int, data))

    print(blink(stones, 25))
    print(blink(stones, 75))

if __name__ == "__main__":
    DAY = 11
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")