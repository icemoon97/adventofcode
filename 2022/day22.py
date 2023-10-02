from helper import *


with open("input22.txt", "r") as file:
	data = file.read().split("\n\n")

# with open("input22test.txt", "r") as file:
# 	data = file.read().split("\n\n")

board, moves_raw = data

grid = {}

for i, line in enumerate(board.split("\n")):
    for j, char in enumerate(line):
        if char != " ":
            grid[(i,j)] = char

m_ints = parse_ints(moves_raw)
moves = [m_ints.pop(0)]
for char in moves_raw:
    if char in ["L", "R"]:
        moves.append(char)
        moves.append(m_ints.pop(0))

pos = (0, 50)
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
dir_i = 0

print("start:", pos, dirs[dir_i])

def get_next(pos, d):
    fx, fy = pos[0] % 50, pos[1] % 50
    cx, cy = pos[0] // 50, pos[1] // 50

    next_pos = (pos[0] + d[0], pos[1] + d[1])
    next_d = d

    if next_pos not in grid:
        match (cx, cy, d):
            case (0, 1, (-1,0)):
                next_pos = (fy + 150, 0)
                next_d = (0,1)
            case (0, 1, (0,-1)):
                next_pos = (149 - fx, 0)
                next_d = (0,1)

            case (0, 2, (-1,0)):
                next_pos = (199, fy)
            case (0, 2, (0,1)):
                next_pos = (149 - fx, 99)
                next_d = (0,-1)
            case (0, 2, (1,0)):
                next_pos = (50 + fy, 99)
                next_d = (0,-1)

            case (1, 1, (0,1)):
                next_pos = (49, fx + 100)
                next_d = (-1,0)
            case (1, 1, (0,-1)):
                next_pos = (100, fx)
                next_d = (1,0)

            case (2, 1, (0,1)):
                next_pos = (49 - fx, 149)
                next_d = (0,-1)
            case (2, 1, (1,0)):
                next_pos = (150 + fy, 49)
                next_d = (0,-1)

            case (2, 0, (-1,0)):
                next_pos = (50 + fy, 50)
                next_d = (0,1)
            case (2, 0, (0,-1)):
                next_pos = (49 - fx, 50)
                next_d = (0,1)

            case (3, 0, (0,1)):
                next_pos = (149, 50 + fx)
                next_d = (-1,0)
            case (3, 0, (1,0)):
                next_pos = (0, 100 + fy)
            case (3, 0, (0,-1)):
                next_pos = (0, 50 + fx)
                next_d = (1,0)

    assert next_pos in grid
    if grid[next_pos] == "#":
        return pos, d

    assert grid[next_pos] == "."
    return next_pos, next_d


for move in moves:
    print(move)
    if type(move) == int:
        d = dirs[dir_i]
        for _ in range(move):
            old = (pos, d)

            pos, d = get_next(pos, d)
            dir_i = dirs.index(d)

            if old[0] != pos:
                r_test = get_next(pos, (-d[0], -d[1]))
                print(f"actual: {old} -> {pos}, {d}")
                print(f"r_test: {pos}, {(-d[0], -d[1])} -> {r_test}")
                assert r_test[0] == old[0]
    else:
        assert move == "L" or move == "R"
        if move == "R":
            dir_i += 1
        else:
            dir_i -= 1
        dir_i = dir_i % len(dirs)
    print(pos, dirs[dir_i])

print("end:", pos, dir_i)
print("Part 2:", (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + dir_i)