# data = [line.rstrip("\n") for line in open("input16.txt")]

with open("input16.txt", "r") as file:
    s = file.read()
    samples, data = s.split("\n\n\n\n")

samples = samples.split("\n\n")
data = data.split("\n")

def apply(func, literals, before, instr):
    A = instr[1] if literals[0] else before[instr[1]]
    B = instr[2] if literals[1] else before[instr[2]]
    ret = before.copy()
    ret[instr[3]] = func(A, B)
    return ret

ops = [
    (lambda x,y: x + y, (False, False)),
    (lambda x,y: x + y, (False, True)),
    (lambda x,y: x * y, (False, False)),
    (lambda x,y: x * y, (False, True)),
    (lambda x,y: x & y, (False, False)),
    (lambda x,y: x & y, (False, True)),
    (lambda x,y: x | y, (False, False)),
    (lambda x,y: x | y, (False, True)),
    (lambda x,y: x, (False, False)),
    (lambda x,y: x, (True, False)),
    (lambda x,y: int(x > y), (True, False)),
    (lambda x,y: int(x > y), (False, True)),
    (lambda x,y: int(x > y), (False, False)),
    (lambda x,y: int(x == y), (True, False)),
    (lambda x,y: int(x == y), (False, True)),
    (lambda x,y: int(x == y), (False, False))
]

total = 0
possible = {}

for line in samples:
    before, instr, after = line.split("\n")
    
    before = [int(x) for x in before[before.index("[")+1:before.index("]")].split(",")]
    after = [int(x) for x in after[after.index("[")+1:after.index("]")].split(",")]
    instr = [int(x) for x in instr.split()]

    results = [apply(op[0], op[1], before, instr) for op in ops]
    matches = [i for i,r in enumerate(results) if r == after]

    if len(matches) >= 3:
        total += 1

    if instr[0] not in possible:
        possible[instr[0]] = set(range(len(ops)))

    possible[instr[0]] &= set(matches)


print("Part 1:", total)

opcodes = {}

for i in range(len(ops)):
    for k,v in possible.items():
        if len(v) == 1:
            to_remove = next(iter(v))
            opcodes[k] = to_remove
            for v in possible.values():
                v.discard(to_remove)

r = [0 for _ in range(4)]
for line in data:
    line = [int(x) for x in line.split()]

    f, literals = ops[opcodes[line[0]]]
    r = apply(f, literals, r, line)

print("Part 2:", r[0])
    

