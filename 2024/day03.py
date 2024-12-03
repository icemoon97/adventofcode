from pathlib import Path
from math import prod
import re

def main(input_path: Path):

    with open(input_path, "r") as file:
        data = file.read()

    part1 = 0
    part2 = 0
    active = True

    cmds = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

    for c in cmds:
        if c == "do()":
            active = True
        elif c == "don't()":
            active = False
        else:
            nums = re.findall("(\d+)", c)
            n = prod(map(int, nums))
            part1 += n
            if active:
                part2 += n

    print(part1)
    print(part2)

if __name__ == "__main__":
    print("===== Tests =====")
    main(f"tests/day03.txt")
    print("===== Input =====")
    main(f"inputs/day03.txt")