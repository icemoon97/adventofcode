from pathlib import Path

add = lambda x,y: x + y
mul = lambda x,y: x * y
concat = lambda x,y: int(str(x) + str(y))

def try_calc(nums, cur, target, ops=[add, mul]):
    # minor optimization
    if cur > target:
        return False
    if not len(nums):
        return cur == target

    for op in ops:
        if try_calc(nums[1:], op(cur, nums[0]), target, ops):
            return True
        
    return False
        
def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    part1 = 0
    part2 = 0

    for line in data:
        target, nums = line.split(": ")

        target = int(target)
        nums = list(map(int, nums.split()))

        if try_calc(nums[1:], nums[0], target):
            part1 += target
        if try_calc(nums[1:], nums[0], target, ops=[add, mul, concat]):
            part2 += target

    print(part1)
    print(part2)

if __name__ == "__main__":
    DAY = 7
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")