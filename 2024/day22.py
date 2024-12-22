from pathlib import Path
from collections import defaultdict

def mix(a: int, b: int):
    return a ^ b

def prune(a: int):
    return a % 16777216

def secret(n: int):
    n = mix(n, n * 64)
    n = prune(n)
    n = mix(n, n // 32)
    n = prune(n)
    n = mix(n, n * 2048)
    n = prune(n)
    return n

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    part1 = 0

    seqs = defaultdict(lambda: 0)

    for line in data:
        secrets = [int(line)]
        
        for _ in range(2000):
            secrets.append(secret(secrets[-1]))

        part1 += secrets[-1]

        prices = [n % 10 for n in secrets]
        diff = [b - a for a, b in zip(prices, prices[1:])]

        seq = {}
        for i in range(0, len(diff) - 4):
            window = tuple(diff[i:i+4])

            if window in seq:
                continue
            seq[window] = prices[i+4]

        for k, v in seq.items():
            seqs[k] += v

    print("Part 1:", part1)
    print("Part 2:", max(seqs.items(), key=lambda x: x[1])[1])


if __name__ == "__main__":
    DAY = 22
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")