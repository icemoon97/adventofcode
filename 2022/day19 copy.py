from helper import *

import functools
import math

with open("input19.txt", "r") as file:
	data = file.read().split("\n")

# with open("input19test.txt", "r") as file:
# 	data = file.read().split("\n")

blueprints = []
mat_types = ["ore", "clay", "obsidian", "geode"]
# reqs = [["ore"], ["ore"], ["ore", "clay"], ["ore", "obsidian"]]
reqs = [[0], [0], [0, 1], [0, 2]]

for line in data:
    line = line[13:].split(". ")
    costs = []
    for robot_desc in line:
        costs.append(tuple(parse_ints(robot_desc)))
    blueprints.append(tuple(costs))

def can_buy(types, cost, mats):
    for i, t in enumerate(types):
        if mats[t] < cost[i]:
            return False
    return True

def sub_reqs(types, cost, mats):
    result = [n for n in mats]
    for i, t in enumerate(types):
        result[t] -= cost[i]
    return tuple(result)

def calc_wait(types, cost, mats, robots):
    wait = []
    for i, t in enumerate(types):
        if mats[t] >= cost[i]:
            wait.append(0)
        else:
            diff = cost[i] - mats[t]
            if robots[t] == 0:
                return False, []
            wait.append(math.ceil(diff / robots[t]))
    return True, max(wait)

def add(mats, robots, n=1):
    return tuple([m + r * n for m,r in zip(mats, robots)])

def buy_robot(robots, type):
    r = list(robots)
    r[type] += 1
    return tuple(r)

@functools.lru_cache(maxsize=None)
def sim(costs, minutes, robots, mats): 
    if minutes <= 0:
        # print("minute:", minutes, mats, robots)
        return mats[3]

    outcomes = [0]

    if can_buy(reqs[3], costs[3], mats):
        _mats = sub_reqs(reqs[3], costs[3], mats)
        return sim(costs, minutes - 1, buy_robot(robots, 3), add(_mats, robots))
    elif minutes <= 10 and can_buy(reqs[2], costs[2], mats):
        _mats = sub_reqs(reqs[2], costs[2], mats)
        return sim(costs, minutes - 1, buy_robot(robots, 2), add(_mats, robots))
    else:
        max_cost = [max([c[0] for c in costs]), costs[2][1], costs[3][1]]
        for i in range(3):
            if robots[i] >= max_cost[i]:
                continue

            if can_buy(reqs[i], costs[i], mats):
                _mats = sub_reqs(reqs[i], costs[i], mats)
                outcomes.append(sim(costs, minutes - 1, buy_robot(robots, i), add(_mats, robots)))

    if mats[0] < 5:
        outcomes.append(sim(costs, minutes - 1, robots, add(mats, robots)))

    return max(outcomes)

total = 1
for i, b in enumerate(blueprints[:3]):
    print(i, b)
    best = sim(b, 32, (1,0,0,0), (0,0,0,0))
    print(best)
    # total += (i + 1) * best
    total *= best

print(total)
