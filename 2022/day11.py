import math

with open("input11.txt", "r") as file:
	data = file.read().split("\n\n")

monkeys = []

class Monkey:
    def __init__(self):
        self.holds = []
        self.op = ""
        self.test = -1
        self.true_next = -1
        self.false_next = -1

        self.count = 0

for group in data:
    group = group.split("\n")
    
    m = Monkey()

    m.holds = [int(x) for x in group[1].split(":")[1].split(",")]
    m.op = eval("lambda old: " + group[2].split("=")[1])
    m.test = int(group[3].split()[3])
    m.true_next = int(group[4].split()[5])
    m.false_next = int(group[5].split()[5])

    monkeys.append(m)

factor = math.prod([m.test for m in monkeys])

def run_round(monkeys):
    for m in monkeys:
        while len(m.holds) > 0:
            worry = m.holds.pop(0)
            worry = m.op(worry)

            # worry = worry // 3
            worry %= factor

            m_next = m.true_next if worry % m.test == 0 else m.false_next
            monkeys[m_next].holds.append(worry)

            m.count += 1

for i in range(10000):
    run_round(monkeys)

def monkey_business(monkeys):
    return math.prod(sorted([m.count for m in monkeys], reverse=True)[:2])

print("Part 2:", monkey_business(monkeys))
