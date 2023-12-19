from queue import PriorityQueue

with open("input17.txt", "r") as file:
    data = file.read().split("\n")

dim = (len(data), len(data[0]))
end_pos = (dim[0] - 1, dim[1] - 1)

grid = {}

for i, line in enumerate(data):
    for j, char in enumerate(line):
        grid[(i,j)] = char

def search(min_moves, max_moves):
    # cost, (pos, dir, steps since changing direction)
    queue = PriorityQueue()
    queue.put((0, ((0, 0), (0, 0), -1)))
    visited = set()

    while not queue.empty():
        cur_cost, state = queue.get()

        if state in visited:
            continue
        visited.add(state)

        cur, dir, dir_change = state
        cx, cy = cur

        if dir_change >= max_moves:
            continue

        if cur == end_pos:
            return cur_cost

        if dir[0]:
            dirs = [dir, (0, 1), (0, -1)]
        elif dir[1]:
            dirs = [dir, (1, 0), (-1, 0)]
        # exception for first move
        else:
            dirs = [(1, 0), (0, 1)]

        for dx, dy in dirs:
            test = (cx + dx, cy + dy)
            if test not in grid:
                continue

            cost = int(grid[test]) + cur_cost

            # exception for first move
            if (dx, dy) == dir or dir == (0, 0):
                queue.put((cost, (test, (dx, dy), dir_change + 1)))
            if (dx, dy) != dir and dir_change >= (min_moves-1):
                queue.put((cost, (test, (dx, dy), 0)))

print("Part 1:", search(0, 3))
print("Part 2:", search(4, 10))
