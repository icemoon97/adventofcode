from math import prod, lcm

with open("input20.txt", "r") as file:
    data = file.read().split("\n")

# name -> (type, dst, mem?)
# for %, mem means on/off (True or False)
# for &, mem means dict of {src -> last_recieved}

circuit = {}

def init_circuit():
    for line in data:
        src, dst = line.split(" -> ")
        dst = dst.split(", ")

        if src == "broadcaster":
            circuit[src] = ('broadcaster', dst)
        else:
            t, src = src[0], src[1:]
            if t == "%":
                circuit[src] = (t, dst, False)
            elif t == "&":
                circuit[src] = (t, dst, {})

    # init mem for all & modules
    for name, mod in circuit.items():
        for d in mod[1]:
            if d not in circuit:
                continue

            if circuit[d][0] == "&":
                mem = circuit[d][2]
                mem[name] = False

total = {True: 0, False: 0}

def pulse_circuit(start="broadcaster", exit=''):
    # (src, dst, pulse)
    # for pulses: False = low, True = high
    pulses = [('button', start, False)]

    while pulses:
        src, cur, p = pulses.pop(0)
        total[p] += 1

        if cur == exit and not p:
            return True

        if cur not in circuit:
            continue

        match circuit[cur]:
            case ['broadcaster', dst]:
                for d in dst:
                    pulses.append((cur, d, p))

            case ["%", dst, state]:
                if p: continue

                state = not state
                for d in dst:
                    pulses.append((cur, d, state))
                circuit[cur] = ("%", dst, state)

            case ["&", dst, mem]:
                mem[src] = p
                if all(mem.values()):
                    for d in dst:
                        pulses.append((cur, d, False))
                else:
                    for d in dst:
                        pulses.append((cur, d, True))

    return False

init_circuit()
for i in range(1000):
    pulse_circuit()
print("Part 1:", prod(total.values()))

# for each subcircuit, finds the end by looking two deep for a &
# not really a general solution but should work on any other AoC input (i think)
def find_conj_child(name, depth=0, max_depth=2):
    if depth >= max_depth:
        return name
    
    for c in circuit[name][1]:
        child = circuit[c]
        if child[0] == "&":
            return find_conj_child(c, depth+1, max_depth)

sub_starts = circuit['broadcaster'][1]
sub_ends = [find_conj_child(s) for s in sub_starts]

cycles = []
for s, e in zip(sub_starts, sub_ends):
    init_circuit()
    i = 1
    while not pulse_circuit(start=s, exit=e):
        i += 1
    cycles.append(i)

print("Part 2:", lcm(*cycles))
