from pathlib import Path

def try_calc(nums, cur, target):
    if not len(nums):
        return cur == target

    n = nums[0]

    add = try_calc(nums[1:], cur + n, target)
    mul = try_calc(nums[1:], cur * n, target)
    cat = try_calc(nums[1:], int(str(cur) + str(n)), target)

    return add or mul or cat
        
def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    total = 0

    for line in data:
        target, nums = line.split(": ")

        target = int(target)
        nums = list(map(int, nums.split()))

        if try_calc(nums[1:], nums[0], target):
            total += target

    print(total)

if __name__ == "__main__":
    DAY = 7
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")