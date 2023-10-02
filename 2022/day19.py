from helper import *
from tqdm import tqdm
import functools

with open("input19.txt", "r") as file:
	data = file.read().split("\n")

# with open("input19test.txt", "r") as file:
# 	data = file.read().split("\n")

blueprints = []
reqs = [[0], [0], [0, 1], [0, 2]]

for line in data:
    c = parse_ints(line[13:])
    costs = ((c[0], 0, 0, 0),
        (c[1], 0, 0, 0),
        (c[2], c[3], 0, 0),
        (c[4], 0, c[5], 0))
    # max cost for any resource, as we don't need to build robots past that point
    max_costs = [max([c[0] for c in costs]), costs[2][1], costs[3][2], 9999]
    
    blueprints.append((costs, max_costs))

def can_buy(cost, mats):
    return all([c <= m for c,m in zip(cost, mats)])

# https://stackoverflow.com/questions/15410119/use-list-comprehension-to-build-a-tuple
def add(t1, t2, n=1):
    return tuple((a + b * n) for a,b in zip(t1, t2))

def buy_robot(robots, type):
    return tuple((r + 1 if i == type else r) for i,r in enumerate(robots))

best_g = 0

@functools.lru_cache(maxsize=None)
def sim(b_index, minutes, robots, mats):
    global best_g
    if minutes <= 0:
        best_g = max(best_g, mats[3])
        return mats[3]

    # pruning
    best_possible = mats[3] + robots[3] * minutes + (minutes * (minutes + 1)) // 2
    if best_possible <= best_g:
        return 0

    # capping at max mats we could actually spend in the remaining time
    costs, max_costs = blueprints[b_index]
    if any([m > mc * minutes for m, mc in zip(mats, max_costs)]):
        mats = tuple((min(m, mc)) for m, mc in zip(mats, max_costs))
        return sim(b_index, minutes, robots, mats)
    
    outcomes = []

    # always buy geode machine if possible
    if can_buy(costs[3], mats):
        return sim(b_index, minutes - 1, buy_robot(robots, 3), add(add(mats, robots), costs[3], n=-1))
    # elif can_buy(costs[2], mats):
    #     return sim(b_index, minutes - 1, buy_robot(robots, 2), add(add(mats, robots), costs[2], n=-1))
    else:
        for i in range(3):
            # have more production than we can use
            if robots[i] >= max_costs[i]:
                continue

            if can_buy(costs[i], mats):
                outcomes.append(sim(b_index, minutes - 1, buy_robot(robots, i), add(add(mats, robots), costs[i], n=-1)))

    if mats[0] <= max_costs[0]:
        outcomes.append(sim(b_index, minutes - 1, robots, add(mats, robots)))

    return max(outcomes)

part1 = 0
part2 = 1
bar = tqdm(blueprints)
for i, b in enumerate(bar):
    best_g = 0
    geodes = sim(i, 24, (1,0,0,0), (0,0,0,0))
    part1 += (i+1) * geodes

    if i < 3:
        best_g = 0
        part2 *= sim(i, 32, (1,0,0,0), (0,0,0,0))

    bar.set_description(f"Blueprint {i} opens {geodes} geodes")

print("Part 1:", part1)
print("Part 2:", part2)

