with open("input06.txt", "r") as file:
    data = file.read()

def first_unique_seg(n):
    for i in range(0, len(data) - n):
        seg = data[i:i+n]
        
        if len(set(list(seg))) == n:
            return i + n

print("Part 1:", first_unique_seg(4))
print("Part 2:", first_unique_seg(14))