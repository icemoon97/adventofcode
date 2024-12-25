from pathlib import Path

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n\n")

    keys = []
    locks = []

    for group in data:
        h = [0 for _ in range(5)]
        for line in group.split("\n")[1:-1]:
            count = [int(c == "#") for c in line]
            h = [a + b for a, b in zip(h, count)]

        if group[0] == ".":
            keys.append(h)
        else:
            locks.append(h)

    total = 0
    for k in keys:
        for l in locks:
            overlap = any(a + b >= 6 for a, b in zip(k, l))
            if not overlap:
                total += 1
    print(total)

if __name__ == "__main__":
    DAY = 25
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")