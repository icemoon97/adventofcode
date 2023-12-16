with open("input16.txt", "r") as file:
    data = file.read().split("\n")

grid = {}

for i, line in enumerate(data):
    for j, char in enumerate(line):
        grid[(i,j)] = char

def run(start, start_dir):
    # pos, dir
    queue = [(start, start_dir)]
    visited = set()

    while queue:
        state = queue.pop(0)

        if state in visited:
            continue
        visited.add(state)

        (cx, cy), (dx, dy) = state
        test = (cx + dx, cy + dy)

        if test not in grid:
            continue

        match grid[test]:
            case "-":
                if dx:
                    dx, dy = 0, 1
                    queue.append((test, (0, -1)))
            case "|":
                if dy:
                    dx, dy = 1, 0
                    queue.append((test, (-1, 0)))
            case "/":
                dx, dy = -dy, -dx
            case "\\":
                dx, dy = dy, dx

        queue.append((test, (dx, dy)))

    visited_tiles = set([x[0] for x in visited])
    # minus 1 because we start one tile off the grid
    return len(visited_tiles) - 1
        
print("Part 1:", run((0, -1), (0, 1)))

dim = (len(data), len(data[0]))

edges = []
for i in range(dim[0]):
    edges.append(((i, -1), (0, 1)))
    edges.append(((i, dim[1]), (0, -1)))
for i in range(dim[1]):
    edges.append(((-1, i), (1, 0)))
    edges.append(((dim[0], i), (-1, 0)))

print("Part 2:", max(run(s, d) for s, d in edges))