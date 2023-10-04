data = [line.rstrip("\n") for line in open("input19.txt")]

ops = {
    "addr" : (lambda x,y: x + y, (False, False)),
    "addi" : (lambda x,y: x + y, (False, True)),
    "mulr" : (lambda x,y: x * y, (False, False)),
    "muli" : (lambda x,y: x * y, (False, True)),
    "banr" : (lambda x,y: x & y, (False, False)),
    "bani" : (lambda x,y: x & y, (False, True)),
    "borr" : (lambda x,y: x | y, (False, False)),
    "bori" : (lambda x,y: x | y, (False, True)),
    "setr" : (lambda x: x, (False, False)),
    "seti" : (lambda x: x, (True, False)),
    "gtir" : (lambda x,y: int(x > y), (True, False)),
    "gtri" : (lambda x,y: int(x > y), (False, True)),
    "gtrr" : (lambda x,y: int(x > y), (False, False)),
    "eqir" : (lambda x,y: int(x == y), (True, False)),
    "eqri" : (lambda x,y: int(x == y), (False, True)),
    "eqrr" : (lambda x,y: int(x == y), (False, False))
}

# modifies registers
def apply(func, reg, instr):
    f, literals = func
    A = instr[1] if literals[0] else reg[instr[1]]
    if f.__code__.co_argcount == 1:
        reg[instr[3]] = f(A)
    else:
        B = instr[2] if literals[1] else reg[instr[2]]
        reg[instr[3]] = f(A, B)

ip_r = int(data[0].split()[1])
ip = 0
reg = [0 for _ in range(6)]
reg[0] = 1

program = data[1:]
program = [line.split() for line in program]
program = [[line[0]] + [int(x) for x in line[1:]] for line in program]

while ip >= 0 and ip < len(program):
    reg[ip_r] = ip

    instr = program[ip]
    apply(ops[instr[0]], reg, instr)

    ip = reg[ip_r]
    ip += 1

print(reg)

