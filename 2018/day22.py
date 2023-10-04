data = [line.rstrip("\n") for line in open("input22.txt")]

# depth = int(data[0][6:])
# target = tuple(int(x) for x in data[1][7:].split(","))
depth = 510
target = (10, 10)

print(depth, target)

def erosion_level(ero, x, y):
    if (x, y) == (0, 0):
        geo = 0 
    elif (x, y) == target:
        geo = 0
    elif not y:
        geo = x * 16807
    elif not x:
        geo = y * 48271
    else:
        geo = ero[(x-1, y)] * ero[(x, y-1)]
    
    return (geo + depth) % 20183
        

# erosion level
ero = {(0,0): 0}

for x in range(target[0]+200):
    for y in range(target[1]+200):
        ero[(x, y)] = erosion_level(ero, x, y)

risk = {k: v % 3 for k, v in ero.items()}

# for y in range(target[0] + 1):
#     for x in range(target[1] + 1):
#         r = risk[(x, y)]
#         if r == 0:
#             print(".", end="")
#         elif r == 1:
#             print("=", end="")
#         elif r == 2:
#             print("|", end="")
#     print()

# print("Part 1:", sum(risk.values()))

# clearly a search problem, A* is probably necessary because of all the tool switching?
# also need to generate grid larger than target, 2x is probably fine?

# tools: neither=0, torch=1, climbing=2
# if tool==risk, cannot move

from queue import PriorityQueue

start = (0, 0)
starting_tool = 1

# heuristic for search
def h(point, end):
    return abs(point[0] - end[0]) + abs(point[1] - end[1])

# heuristic, steps, pos, tool
queue = PriorityQueue()
queue.put((h(start, target), 0, start, starting_tool))

# steps, pos, tool
seen = set()
seen.add((0, start, starting_tool))

searched = 0
while not queue.empty():
    searched += 1
    if searched % 100000 == 0:
        print(searched)
    if searched > 10000000:
        print("searched too many states, exiting")
        break

    _, steps, cur, cur_tool = queue.get()

    if cur == target:
        print("reached target!", steps)
        print("final tool:", cur_tool)
        if cur_tool == 2:
            steps += 7
        break

    # try moving in all directions
    for d in [(1,0), (0,1), (-1,0), (0,-1)]:
        test = (cur[0] + d[0], cur[1] + d[1])

        if test not in risk:
            continue
        if cur_tool == risk[test]:
            continue
        if (steps + 1, test, cur_tool) in seen:
            continue

        h_test = steps + 1 + h(test, target)

        seen.add((steps + 1, test, cur_tool))
        queue.put((h_test, steps + 1, test, cur_tool))
        
    # try switching tools
    for test_tool in [0, 1, 2]:
        if test_tool == cur_tool:
            continue
        if test_tool == risk[cur]:
            continue
        if (steps + 7, cur, test_tool) in seen:
            continue

        h_test = steps + 7 + h(cur, target)

        seen.add((steps + 7, cur, test_tool))
        queue.put((h_test, steps + 7, cur, test_tool))


print(steps)

