with open("input02.txt", "r") as file:
    data = file.read().split("\n")

def is_safe(nums):
    incr = True
    decr = True
    small_gaps = True

    for (n1, n2) in zip(nums, nums[1:]):
        if n1 > n2:
            incr = False
        if n1 < n2:
            decr = False
        if abs(n1 - n2) > 3 or n1 == n2:
            small_gaps = False

    return small_gaps and (incr or decr)

part1 = 0
part2 = 0
for line in data:
    nums = list(map(int, line.split()))

    safe = is_safe(nums)

    variants = [is_safe(nums[:i] + nums[i+1:]) for i in range(len(nums))]

    if safe:
        part1 += 1
    if safe or any(variants):
        part2 += 1
    
print("Part 1:", part1)
print("Part 2:", part2)