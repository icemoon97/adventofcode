from helper import *
import itertools

import time
start_time = time.time()

with open("input16.txt", "r") as file:
	data = file.read().split("\n")

flow = {}
adj = {}

for i, line in enumerate(data):
    line = line.split()

    valve = line[1]
    f = parse_ints(line[4])[0]
    if f > 0:
        flow[valve] = f
    adj[valve] = [v.rstrip(",") for v in line[9:]]

# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
d = {}
for v in adj.keys():
    d[v] = {u : 999999 for u in adj.keys()}
    d[v][v] = 0
    for u in adj[v]:
        d[v][u] = 1

for k,i,j in itertools.product(adj.keys(), adj.keys(), adj.keys()):
    if d[i][j] > d[i][k] + d[k][j]:
        d[i][j] = d[i][k] + d[k][j]

bits = {}
for i, valve in enumerate(flow):
    bits[valve] = 1<<i

def search(minutes, pos, open, released, cache):
    if open not in cache:
        cache[open] = 0

    cache[open] = max(cache[open], released)

    for other in flow:
        if bits[other] & open:
            continue

        time = minutes - d[pos][other] - 1
        if time <= 0:
            continue

        search(time, other, open | bits[other], released + time * flow[other], cache)

    return cache

part1 = search(30, "AA", 0, 0, {})
print("Part 1:", max(part1.values()))

# print(f"Time since start: {time.time() - start_time:.2f}s")

part2 = search(26, "AA", 0, 0, {})
# print(f"Time since start: {time.time() - start_time:.2f}s")
best = 0
for me, elephant in itertools.product(part2.items(), part2.items()):
    if not (me[0] & elephant[0]):
        best = max(best, me[1] + elephant[1])
print("Part 2:", best)

# print(f"Time since start: {time.time() - start_time:.2f}s")


# @functools.lru_cache(maxsize=None)
# def search(minutes, pos, open, current_flow, released, e=False):
#     # print(minutes, pos, open, released)
#     if minutes <= 0:
#         if e:
#             # print("elephant's turn", released, open)
#             return search(26, "AA", open, 0, released, e=False)
#         else:
#             return released

#     # current_flow = sum([flow[v] for v in open])
#     outcomes = []

#     for other in d[pos]:
#         if other in open:
#             continue
#         if flow[other] == 0:
#             continue

#         time_cost = d[pos][other] + 1 # cost of travelling plus opening valve
#         if time_cost > minutes:
#             continue

#         outcomes.append(search(
#             minutes - time_cost, 
#             other, 
#             open | {other}, 
#             current_flow + flow[other], 
#             released + current_flow * time_cost,
#             e=e))

#     # represents standing still until time runs out
#     rem = released + minutes * current_flow
#     if e:
#         print("elephant's turn", rem, open)
#         rem += search(26, "AA", open, 0, 0, e=False)
#     outcomes.append(rem) 

#     return max(outcomes)
