from math import prod

with open("input06.txt", "r") as file:
    data = file.read().split("\n")

def sim_boat(t, g):
    count = 0
    for acc in range(1, t):
        if acc * (t - acc) > g:
            count += 1
    return count

times = [int(x) for x in data[0].split(":")[1].split()]
dists = [int(x) for x in data[1].split(":")[1].split()]

counts = [sim_boat(t, g) for t, g in zip(times, dists)]

# for t, g in zip(times, dists):
#     count = 0
#     for acc in range(1, t):
#         if acc * (t - acc) > g:
#             count += 1
#     counts.append(count)

print("Part 1:", prod(counts))

time = int("".join(map(str, times)))
dist = int("".join(map(str, dists)))

# count = 0
# for acc in range(1, time):
#     travel = time - acc
    
#     d = travel * acc
#     if d > dist:
#         count += 1

print("Part 2:", sim_boat(time, dist))