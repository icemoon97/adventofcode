from queue import PriorityQueue

data = [line.rstrip("\n") for line in open("input23.txt")]

rows, cols = len(data), len(data[0])
grid = {}

def print_grid(grid):
    for i in range(rows):
        for j in range(cols):
            char = grid[(i,j)] if (i,j) in grid else " "
            print(char, end="")
        print()

amps = {}

letters = ["A", "B", "C", "D"]
cost = {"A": 1, "B": 10, "C": 100, "D": 1000}

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char in letters:
            amps[(i,j)] = char
            char = "."
        grid[(i,j)] = char
        

hallway = {(1,1), (1,2), (1,4), (1,6), (1,8), (1,10), (1,11)}
goals = {}
for i, char in enumerate(letters):
    goals[char] = set()
    for j in range(2):
        goals[char].add((j+2, i*2 + 3))

print(amps)
print(goals)

def construct_state(grid, amps):
    state = ""
    for i in range(rows):
        for j in range(cols):
            if (i,j) in amps:
                state += amps[(i,j)]
            elif (i,j) in grid:
                state += grid[(i,j)]
        state += "\n"
    return state

def parse_state(state):
    amps = {}
    for i, line in enumerate(state.split("\n")):
        for j, char in enumerate(line):
            if char in letters:
                amps[(i,j)] = char
    return amps

print(construct_state(grid, amps))

def scout(start, type, amps):
    reachable = {}

    q = [(start, 0)]
    seen = {start}

    while len(q) > 0:
        pos, steps = q.pop(0)
        if pos in hallway or pos in goals[type]:
            reachable[pos] = steps

        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            test = (pos[0] + d[0], pos[1] + d[1])

            if test in seen:
                continue
            if test in amps or grid[test] != ".":
                continue

            q.append((test, steps+1))
            seen.add(test)

    return reachable

# print(scout((2,3), "B", amps))
for pos, type in amps.items():
    print(type, pos, scout(pos, type, amps))

def search(start, goal):
    q = PriorityQueue()

    best = {} # state -> best known cost

    while not q.empty():
        cost, state = q.get()

        # if state is goal, return cost
        if state == goal:
            return cost

        amps = parse_state(state)

        for loc, char in amps.items():
            if loc in goals[char]:
                continue

            reachable = scout(loc, char, amps)

        # parse state
        # for each amp, consider possible moves:
            # if can't move: continue
            # if in hallway, try to move to goal
            # if in wrong room, try to move to hallway

            # compute possible state
            # compare cost, add to queue if better than prev cost

