from collections import defaultdict, deque

data = [line.rstrip("\n") for line in open("input20.txt")][0]
# data = "^ENWWW(NEEE|SSE(EE|N))$"
# data = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
# data = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
# data = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"

# parsing regex
def parse_branch(s, i):
    options = []
    current = []

    while s[i] != ")":
        if s[i] == "|":
            options.append(current)
            current = []
        elif s[i] == "(":
            subopt, i = parse_branch(s, i + 1)
            current.append(subopt)
        else:
            current.append(s[i])
        
        i += 1

    options.append(current)
    return options, i

paths = []

i = 1
while i < len(data) - 1:
    if data[i] == "(":
        subopt, i = parse_branch(data, i+1)
        paths.append(subopt)
    else:
        paths.append(data[i])
    i += 1

# searching paths in parsed format to get graph structure
dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}
edges = defaultdict(set)

def search_paths(paths, pos):
    for step in paths:
        if type(step) == str:
            prev = pos
            pos = (pos[0] + dirs[step][0], pos[1] + dirs[step][1])
            edges[prev].add(pos)
            edges[pos].add(prev)
        elif type(step) == list:
            for option in step:
                search_paths(option, pos)
        else:
            raise Exception("Invalid path format!!")

search_paths(paths, (0, 0))

# printing map visualization
# rangeX = (min(map(lambda x: x[0], edges)), max(map(lambda x: x[0], edges)))
# rangeY = (min(map(lambda x: x[1], edges)), max(map(lambda x: x[1], edges)))

# for y in range(rangeY[0], rangeY[1]+1):
#     row = "#."
#     for x in range(rangeX[0], rangeX[1]):
#         if (x+1, y) in edges[(x, y)]:
#             row += "|"
#         else:
#             row += "#"
#         row += "."
#     row += "#"
#     print(row)

#     row = "#"
#     for x in range(rangeX[0], rangeX[1]+1):
#         if (x, y+1) in edges[(x, y)]:
#             row += "-"
#         else:
#             row += "#"
#         row += "#"
#     print(row)

# searching graph to find furthest point
dist = {}

visited = set()
queue = deque()
queue.append((0, (0, 0)))

while queue:
    d, pos = queue.popleft()

    dist[pos] = d

    for e in edges[pos]:
        if e not in visited:
            queue.append((d+1, e))
            visited.add(e)


print("Part 1:", max(dist.values()))
print("Part 2:", sum(x >= 1000 for x in dist.values()))