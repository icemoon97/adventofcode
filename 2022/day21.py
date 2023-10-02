with open("input21.txt", "r") as file:
	data = file.read().split("\n")

# with open("input21test.txt", "r") as file:
# 	data = file.read().split("\n")

monkey = {}

for line in data:
    name, op = line.replace("/", "//").split(": ")
    op = op.split()

    if len(op) == 1:
        monkey[name] = int(op[0])
    else:
        monkey[name] = op

def compute(name):
    mk = monkey[name]
    if type(mk) == int:
        return mk
    
    a, b = compute(mk[0]), compute(mk[2])
    return eval(f"{a} {mk[1]} {b}")

def contains_human(name):
    if name == "humn":
        return True

    mk = monkey[name]
    if type(mk) == int:
        return False

    return contains_human(mk[0]) or contains_human(mk[2])

def reverse(name, eq):
    mk = monkey[name]

    if name == "humn":
        return eq

    if type(mk) == int:
        return mk

    left, right = mk[0], mk[2]
    op = mk[1]

    if contains_human(left):
        x = compute(right)
        if op == "+":
            return reverse(left, eq - x)
        elif op == "-":
            return reverse(left, eq + x)
        elif op == "*":
            return reverse(left, eq // x)
        elif op == "//":
            return reverse(left, eq * x)
    else:
        x = compute(left)
        if op == "+":
            return reverse(right, eq - x)
        # x - right = eq
        elif op == "-":
            return reverse(right, x - eq)
        elif op == "*":
            return reverse(right, eq // x)
        # x / right = eq
        elif op == "//":
            return reverse(right, x // eq)

root = monkey["root"]
left, right = root[0], root[2]

print("Part 1:", compute("root"))

if contains_human(left):
    eq = compute(right)
    print("Part 2:", reverse(left, eq))
else:
    eq = compute(left)
    print("Part 2:", reverse(right, eq))

