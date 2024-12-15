from pathlib import Path
import numpy as np

def parse_ints(s: str):
    s = "".join([c if c.isdigit() else " " for c in s])
    return [int(x) for x in s.split()]

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n\n")

    total = 0

    for group in data:
        lines = list(map(parse_ints, group.split("\n")))

        m = np.array(lines[:2])
        prize = [n + 10000000000000 for n in lines[2]]

        steps = list(map(round, np.matmul(prize, np.linalg.inv(m))))

        if all(np.matmul(steps, m) == prize):
            total += 3 * steps[0] + steps[1]

    print(total)

if __name__ == "__main__":
    DAY = 13
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")