with open("input20.txt", "r") as file:
	data = file.read().split("\n")

nums = [int(line) for line in data]

d_key = 811589153

def mix(nums, rounds=1):
    n = len(nums)
    ids = [i for i in range(n)]

    for _ in range(rounds):
        for i, step in enumerate(nums):
            cur = ids.index(i)
            ids.pop(cur)
            ids.insert((cur + step) % (n - 1), i)
    
    return [nums[i] for i in ids]

def grove(nums):
    zero = nums.index(0)
    return sum([nums[(zero + i*1000) % len(nums)] for i in range(1,4)])

print("Part 1:", grove(mix(nums)))
print("Part 2:", grove(mix([n * d_key for n in nums], rounds=10)))

