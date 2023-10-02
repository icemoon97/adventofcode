with open("input07.txt", "r") as file:
    data = file.read().split("\n")[1:]

current = "/"
subdir = {}
local_size = {"/": 0}

for line in data:
    line = line.split()

    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current = current[:current.rindex("/", 0, len(current)-1)+1]
            else:
                current += line[2] + "/"
    elif line[0] == "dir":
        if current not in subdir:
            subdir[current] = []

        sub = current + line[1] + "/"
        subdir[current].append(sub)
    else:
        if current not in local_size:
            local_size[current] = 0
        local_size[current] += int(line[0])

def total(path):
    size = 0
    if path in subdir:
        for f in subdir[path]:
            size += total(f)
    if path in local_size:
        size += local_size[path]
    return size

all_folders = []
def map_files(f):
    all_folders.append(f)
    if f in subdir:
        for f2 in subdir[f]:
            map_files(f2)
map_files("/")

p1 = 0
p2 = float("inf")

unused = 70000000 - total("/")
for f in all_folders:
    t = total(f)
    if t <= 100000:
        p1 += t
    if unused + t >= 30000000:
        p2 = min(t, p2)

print("Part 1:", p1)
print("Part 2:", p2)