from helper import *
from math import prod
from copy import deepcopy

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

    m.holds = parse_ints(group[1])
    m.op = eval("lambda old: " + group[2].split("=")[1])
    m.test = parse_ints(group[3])[0]
    m.true_next = parse_ints(group[4])[0]
    m.false_next = parse_ints(group[5])[0]

    monkeys.append(m)

factor = prod([m.test for m in monkeys])

def run_round(monkeys, part2=True):
    for m in monkeys:
        while len(m.holds) > 0:
            worry = m.holds.pop(0)
            worry = m.op(worry)

            if part2:
                worry %= factor
            else:
                worry = worry // 3

            m_next = m.true_next if worry % m.test == 0 else m.false_next
            monkeys[m_next].holds.append(worry)

            m.count += 1

def monkey_business(monkeys, part2=True):
    for _ in range(10000 if part2 else 20):
        run_round(monkeys, part2=part2)

    return prod(sorted([m.count for m in monkeys], reverse=True)[:2])

print("Part 1:", monkey_business(deepcopy(monkeys), part2=False))
print("Part 2:", monkey_business(deepcopy(monkeys)))
