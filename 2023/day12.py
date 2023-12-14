with open("input12.txt", "r") as file:
    data = file.read().split("\n")

opt = {}
def combos(scan, nums, i, spring_i, current):
    id = (i, spring_i, current)
    if id in opt:
        return opt[id]

    # exit condition
    if i == len(scan):
        if spring_i == len(nums) and not current:
            return 1
        elif spring_i == len(nums) - 1 and nums[spring_i] == current:
            return 1
        else:
            return 0
        
    count = 0

    char = scan[i]
    if char == "#" or char == "?":
        count += combos(scan, nums, i+1, spring_i, current+1)
    if char == "." or char == "?":
        if not current:
            count += combos(scan, nums, i+1, spring_i, 0)
        elif spring_i < len(nums) and nums[spring_i] == current:
            count += combos(scan, nums, i+1, spring_i+1, 0)

    opt[id] = count
    return count

part1 = 0
part2 = 0
for i, line in enumerate(data):
    scan, nums = line.split()
    nums = list(map(int, nums.split(",")))

    opt.clear()
    part1 += combos(scan, nums, 0, 0, 0)
    opt.clear()
    part2 += combos((scan + "?") * 4 + scan, nums * 5, 0, 0, 0)

print("Part 1:", part1)
print("Part 2:", part2)


# # Brute force solution
# # (originally used for part 1)
# def search(scan, nums):
#     if "?" not in scan:
#         springs = scan.replace(".", " ").split()
#         if len(springs) == len(nums) and all(len(s) == n for s, n in zip(springs, nums)):
#             return 1
#         return 0

#     count = 0

#     i = scan.index("?")
#     count += search(scan[:i] + "." + scan[i+1:], nums)
#     count += search(scan[:i] + "#" + scan[i+1:], nums)

#     return count
