import functools
import math

from helper import *

with open("input13.txt", "r") as file:
	data = file.read().split("\n\n")

def cmp(a, b):
    # if a < b:
    #     return -1
    # elif a > b:
    #     return 1
    # else:
    #     return 0
    return (a > b) - (a < b)

# -1 if left comes first, 0 if same, 1 if right comes first
def compare(left, right):
    if type(left) == int and type(right) == int:
        return cmp(left, right)

    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]

    # zip is only as long as shorter list
    for l,r in zip(left, right):
        comp = compare(l, r)
        if comp != 0:
            return comp

    return cmp(len(left), len(right))

pairs = []
for pair in data:
    pairs += [eval(part) for part in pair.split("\n")]

print("Part 1:", sum([i//2 + 1 for i in range(0, len(pairs), 2) if compare(pairs[i], pairs[i+1]) == -1]))

dividers = [[[2]], [[6]]]
pairs += dividers

sorted_pairs = sorted(pairs, key=functools.cmp_to_key(compare))
print("Part 2:", math.prod([sorted_pairs.index(d) + 1 for d in dividers]))