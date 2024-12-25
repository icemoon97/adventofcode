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

    output = []
    for i in itertools.count():
        key = f"z{i:02d}"
        if key not in wires:
            break
        output.append(compute(wires, key))

    print(output)

    output_val = int("".join(map(str, output[::-1])), 2)

    print(output_val)

if __name__ == "__main__":
    DAY = 24
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")