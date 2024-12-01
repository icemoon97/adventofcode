from collections import defaultdict

# with open("input23test.txt", "r") as file:
with open("input23.txt", "r") as file:
    data = file.read().split("\n")

dim = (len(data), len(data[0]))

grid = defaultdict(lambda: "#")

for i, line in enumerate(data):
    for j, char in enumerate(line):
        grid[(i,j)] = char

def neighbors(point, dirs=[(1,0), (0,1), (-1,0), (0,-1)]):
    for dx, dy in dirs:
        test = (point[0] + dx, point[1] + dy)
        if grid[test] in ".><v^":
            yield test

start = (0, 1)
end = (dim[0]-1, dim[1]-2)

# cur, steps_since branch, last_branch
queue = [(start, 0, start, (0, 0))]
visited = set()

branches = defaultdict(list)

searched = 0

while queue:
    state = queue.pop(0)
    cur, steps, last_branch, prev = state

    if state in visited:
        continue
    visited.add(state)

    searched += 1
    # if searched > 50:
    #     break

    # if cur == (dim[0]-1, dim[1]-2):
    #     best = max(len(visited), best)

    # match grid[cur]:
    #     case ">":
    #         adj = neighbors(cur, [(0, 1)])
    #     case "<":
    #         adj = neighbors(cur, [(0, -1)])
    #     case "v":
    #         adj = neighbors(cur, [(1, 0)])
    #     case "^":
    #         adj = neighbors(cur, [(-1, 0)])
    #     case ".":
    #         adj = neighbors(cur)

    adj = list(neighbors(cur))
    adj = [p for p in adj if p != prev]

    # print(len(visited), cur, grid[cur], adj)
    # print(cur, steps, last_branch, adj)

    if cur == (dim[0]-1, dim[1]-2):
        branches[last_branch].append((cur, steps))

    if len(adj) > 1:
        # print(cur, len(adj))
        branches[last_branch].append((cur, steps))
        for p in adj:
            queue.append((p, 1, cur, cur))
    else:
        for p in adj:
            queue.append((p, steps+1, last_branch, cur))

full = branches.copy()
for k,v in branches.items():
    for other, cost in v:
        if (k, cost) not in full[other]:
            full[other].append((k, cost))

print("branches:")
for k,v in full.items():
    print(k, v)


def dfs(cur, visited, steps):
    if cur == end:
        return steps
    
    best = 0
    for adj, cost in full[cur]:
        if adj in visited:
            continue

        visited.add(cur)
        res = dfs(adj, visited.copy(), steps+cost)
        best = max(res, best)
    return best

print(dfs(start, {start}, 0))