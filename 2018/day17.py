from collections import defaultdict
from queue import Queue

data = [line.rstrip("\n") for line in open("input17.txt")]

# grid = defaultdict(lambda: defaultdict(lambda: ""))
clay = set()
min_y, max_y = 9999999999, -99999999999

for line in data:
    line = line.split()
    first = int(line[0][line[0].index("=")+1:-1])
    second = line[1][line[1].index("=")+1:].split("..")
    
    if line[0][0] == "x":
        for i in range(int(second[0]), int(second[1])+1):
            # grid[first][i] = "#"
            clay.add((first, i))
            min_y = min(min_y, i)
            max_y = max(max_y, i)
    elif line[0][0] == "y":
        min_y = min(min_y, first)
        max_y = max(max_y, first)
        for i in range(int(second[0]), int(second[1])+1):
            # grid[i][first] = "#"
            clay.add((i, first))

print(min_y, max_y)

start = (0, 500)

water = set()

fringe = Queue()
fringe.put(start)


