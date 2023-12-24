import itertools

def parse_ints(s: str):
    s = "".join([c if c.isdigit() or c == "-" else " " for c in s])
    s = [int(x) for x in s.split()]
    return s

# with open("input24test.txt", "r") as file:
with open("input24.txt", "r") as file:
    data = file.read().split("\n")

# test_x = (7, 27)
# test_y = (7, 27)
test_x = (200000000000000, 400000000000000)
test_y = (200000000000000, 400000000000000)

hail = []
for i, line in enumerate(data):
    px, py, pz, vx, vy, vz = parse_ints(line)

    pos = (px, py, pz)
    v = (vx, vy, vz)

    hail.append((pos, v))


import numpy as np

total = 0
for h1, h2 in itertools.combinations(hail, 2):
    (x1, y1, _), (vx1, vy1, _) = h1
    (x2, y2, _), (vx2, vy2, _) = h2

    A = [[vx1, vx2],
         [vy1, vy2]]
    b = [x2 - x1, y2 - y1]

    if np.linalg.det(A):
        sol = np.linalg.solve(A, b)

        if sol[0] < 0 or sol[1] > 0:
            continue

        crash_x, crash_y = x1 + vx1 * sol[0], y1 + vy1 * sol[0]

        if crash_x >= test_x[0] and crash_x <= test_x[1] and crash_y >= test_y[0] and crash_y <= test_y[1]:
            # print("good")
            total += 1

print("Part 1:", total)
    
from sympy import symbols, Eq, solve

# Define symbols
rx, ry, rz, rvx, rvy, rvz = symbols(['rx', 'ry', 'rz', 'rvx', 'rvy', 'rvz'])
t_syms = symbols([f"t{i}" for i in range(3)])

eqs = []
for i, h in enumerate(hail[:3]):
    (hx, hy, hz), (hvx, hvy, hvz) = h

    eq1 = Eq(hx + hvx * t_syms[i], rx + rvx * t_syms[i])
    eq2 = Eq(hy + hvy * t_syms[i], ry + rvy * t_syms[i])
    eq3 = Eq(hz + hvz * t_syms[i], rz + rvz * t_syms[i])

    eqs.extend([eq1, eq2, eq3])

sol = solve(eqs, [rx, ry, rz, rvx, rvy, rvz] + t_syms)
for s in sol:
    print("Part 2:", sum(s[:3]))