with open("input13.txt", "r") as file:
    data = file.read().split("\n\n")

        
def find_mirror(pattern, part2=False):
    dim = (len(pattern), len(pattern[0]))
    trans = ["".join([p[i] for p in pattern]) for i in range(dim[1])]

    for i in range(dim[0]-1):
        d = 0
        for a, b in zip(pattern[i+1:], pattern[i::-1]):
            d += sum(a[i] != b[i] for i in range(len(a)))

        if d == (1 if part2 else 0):
            return (i + 1) * 100
    
    for i in range(dim[1]-1):
        d = 0
        for a, b in zip(trans[i+1:], trans[i::-1]):
            d += sum(a[i] != b[i] for i in range(len(a)))

        if d == (1 if part2 else 0):
            return i + 1 

part1 = 0
part2 = 0
for pattern in data:
    pattern = pattern.split("\n")

    part1 += find_mirror(pattern)
    part2 += find_mirror(pattern, part2=True)

print("Part 1:", part1)
print("Part 2:", part2)
