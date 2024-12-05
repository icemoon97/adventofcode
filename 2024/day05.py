from pathlib import Path
from collections import defaultdict
from functools import cmp_to_key

def main(input_path: Path):
    with open(input_path, "r") as file:
        rules, books = file.read().split("\n\n")
        rules = rules.split("\n")
        books = books.split("\n")

    follows = defaultdict(set)

    for line in rules:
        left, right = map(int, line.split("|"))
        follows[left].add(right)

    def compare(a, b):
        if a in follows[b]:
            return 1
        if b in follows[a]:
            return -1
        return 0

    part1 = 0
    part2 = 0
    for book in books:
        nums = list(map(int, book.split(",")))

        valid = True
        for i, n in enumerate(nums):
            prev = set(nums[:i])
            post = set(nums[i+1:])

            if prev & follows[n]:
                valid = False
                break
            if len(post & follows[n]) != len(post):
                valid = False
                break

        fixed = sorted(nums, key=cmp_to_key(compare))

        if valid:
            part1 += nums[len(nums)//2]
        else:
            part2 += fixed[len(nums)//2]

    print(part1)
    print(part2)

if __name__ == "__main__":
    DAY = 5
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")