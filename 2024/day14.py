from pathlib import Path
from math import prod

def safety_score(dim: tuple[int, int], pos: list[tuple[int, int]]) -> int:
    mid_x, mid_y = dim[0] // 2, dim[1] // 2
    quad_count = [0 for _ in range(4)]
    for px, py in pos:
        if px < mid_x and py < mid_y:
            quad_count[0] += 1
        elif px > mid_x and py < mid_y:
            quad_count[1] += 1
        elif px < mid_x and py > mid_y:
            quad_count[2] += 1
        elif px > mid_x and py > mid_y:
            quad_count[3] += 1

    return prod(quad_count)

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    DIM = (101, 103)
    # DIM = (11, 7)

    pos = []
    vel = []

    for line in data:
        p, v = [list(map(int, part[2:].split(","))) for part in line.split()]
        pos.append(p)
        vel.append(v)

    best_score = 9999999999999
    best_grid = ""
    best_timestamp = 0

    for step in range(10000):
        next_pos = []

        for p, v in zip(pos, vel):
            x = (p[0] + v[0]) % DIM[0]
            y = (p[1] + v[1]) % DIM[1]
            next_pos.append((x, y))

        pos = next_pos

        # box_min = [min(p[n] for p in pos) for n in range(2)]
        # box_max = [max(p[n] for p in pos) for n in range(2)]
        # print(box_min, box_max)

        # unique = set(pos)
        # print(len(unique))
        # uni.append(len(unique))

        score = (safety_score(DIM, pos))
        if score < best_score:
            best_score = score
            best_grid = "\n".join("".join(("#" if (x, y) in pos else ".") for x in range(DIM[0])) for y in range(DIM[1]))
            best_timestamp = step

    # print(sorted(uni, reverse=True)[:10])

    # print(safety_score(DIM, pos))

    print(best_grid)
    print(best_timestamp+1)



if __name__ == "__main__":
    DAY = 14
    # print("===== Tests =====")
    # main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")