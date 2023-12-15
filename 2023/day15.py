with open("input15.txt", "r") as file:
    data = file.read().split(",")

def hash(s):
    n = 0
    for c in s:
        n += ord(c)
        n *= 17
        n %= 256
    return n

print("Part 1:", sum(hash(seq) for seq in data))

boxes = [{} for _ in range(256)]

for seq in data:
    match seq.split("="):
        case [label, n]:
            k = hash(label)
            boxes[k][label] = n
        case [label]:
            label = label[:-1]
            k = hash(label)
            boxes[k].pop(label, 0)

total = 0
for i, b in enumerate(boxes):
    for j, n in enumerate(b.values()):
        total += (i+1) * (j+1) * int(n)
print("Part 2:", total)