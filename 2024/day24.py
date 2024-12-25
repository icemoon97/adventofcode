import itertools
from pathlib import Path

def compute(wires, key):
    match wires[key]:
        case ("AND", in1, in2):
            return compute(wires, in1) & compute(wires, in2)
        case ("OR", in1, in2):
            return compute(wires, in1) | compute(wires, in2)
        case ("XOR", in1, in2):
            return compute(wires, in1) ^ compute(wires, in2)
        case val:
            return val
        
def print_tree(wires, key, depth, max_width):
    if not depth:
        return
    match wires[key]:
        case (op, in1, in2):
            print(f"{key:|>{max_width - depth}} - {in1} {op} {in2}")
            print_tree(wires, in1, depth - 1, max_width)
            print_tree(wires, in2, depth - 1, max_width)
        case val:
            print(f"{key:|>{max_width - depth}} - {val}")
        
def add(wires_original, x, y):
    wires = wires_original.copy()

    for i in itertools.count():
        key = f"x{i:02d}"
        if key not in wires:
            break
        wires[key] = x % 2
        x //= 2
    for i in itertools.count():
        key = f"y{i:02d}"
        if key not in wires:
            break
        wires[key] = y % 2
        y //= 2

    output = []
    for i in itertools.count():
        key = f"z{i:02d}"
        if key not in wires:
            break
        output.append(compute(wires, key))

    return int("".join(map(str, output[::-1])), 2)

def main(input_path: Path):
    with open(input_path, "r") as file:
        start, gates_data = file.read().split("\n\n")

    wires = {}
    for line in start.split("\n"):
        a, b = line.split(": ")
        wires[a] = int(b)

    for line in gates_data.split("\n"):
        in1, op_name, in2, _, out = line.split()

        wires[out] = (op_name, in1, in2)

    swaps = [("z05", "bpf"), ("z11", "hcc"), ("hqc", "qcw"), ("z35", "fdw")]
    for s1, s2 in swaps:
        temp = wires[s1]
        wires[s1] = wires[s2]
        wires[s2] = temp

    for shift in range(44):
        test_x = 1 << shift
        test_y = 1 << shift
        expected = test_x + test_y
        z = add(wires, test_x, test_y)
        print("shift", shift, expected, z)

        for i in itertools.count():
            b1 = expected % 2
            b2 = z % 2
            # print(i, b1, b2)
            if b1 != b2:
                print(i, b1, b2)
            expected //= 2
            z //= 2
            if expected <= 0:
                break


    flat_swaps = []
    for s in swaps:
        flat_swaps.extend(s)
    print(",".join(sorted(flat_swaps)))

    # sus bits: 5, 11, 24, 35

    # print_tree(wires, "z36", 5, 8)

    # zo5
    # bpf

    # z11
    # hcc

    # hqc
    # qcw

    # z35
    # fdw


if __name__ == "__main__":
    DAY = 24
    # print("===== Tests =====")
    # main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")