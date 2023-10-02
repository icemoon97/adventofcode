from helper import *


with open("input22.txt", "r") as file:
	data = file.read().split("\n\n")

# with open("input22test.txt", "r") as file:
# 	data = file.read().split("\n\n")

board, moves = data

grid = {}

for i, line in enumerate(board.split("\n")):
    for j, char in enumerate(line):
        if char != " ":
            grid[(i,j)] = char

faces = [{} for _ in range(6)]
offsets = [(0,50), (0,100), (50,50), (100,50), (100,0), (150,0)]
for f,off in zip(faces, offsets):
    for i in range(50):
        for j in range(50):
            f[(i,j)] = grid[(i + off[0], j + off[1])]
for f in faces:
    assert len(f) == 50 * 50
    for k in f.values():
        assert k == "." or k == "#"

face_change = {
    0 : {
        (0,1): (1, (0,1)),
        (1,0): (2, (1,0)),
        (0,-1): (4, (0,1)),
        (-1,0): (5, (0,1))
    },
    1 : {
        (0,1): (3, (0,-1)),
        (1,0): (2, (0,-1)),
        (0,-1): (0, (0,-1)),
        (-1,0): (5, (-1,0))
    },
    2 : {
        (0,1): (1, (-1,0)),
        (1,0): (3, (1,0)),
        (0,-1): (4, (1,0)),
        (-1,0): (0, (-1,0))
    },
    3 : {
        (0,1): (1, (0,-1)),
        (1,0): (5, (0,-1)),
        (0,-1): (4, (0,-1)),
        (-1,0): (2, (-1,0))
    },
    4 : {
        (0,1): (3, (0,1)),
        (1,0): (5, (1,0)),
        (0,-1): (0, (0,1)),
        (-1,0): (2, (0,1))
    },
    5 : {
        (0,1): (3, (-1,0)),
        (1,0): (1, (1,0)),
        (0,-1): (0, (-1, 0)),
        (-1,0): (4, (-1,0))
    }
    
}


# pos = (0, min([x[1] for x in grid.keys() if x[0] == 0]))
# pos = (0, 50)
pos = (0,0)
dir_i = 0
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
face = 0

print("start", pos)

def get_next(pos, d, face):
    test = (pos[0] + d[0], pos[1] + d[1])
    next_face = face
    next_d = d
    if test not in faces[face]:
        next_face, next_d = face_change[face][d]
        save = pos[d.index(0)]

        next_pos = [-1, -1]
        next_pos[next_d.index(0)] = save
        change = int(not bool(next_d.index(0)))
        if sum(next_d) > 0:
            next_pos[change] = 0
        else:
            next_pos[change] = 49

        assert all([n >= 0 for n in next_pos])

        test = tuple(next_pos)

    assert test in faces[next_face]
    if faces[next_face][test] == "#":
        return pos, face, d

    assert faces[next_face][test] == "."
    assert next_face in range(6)
    return test, next_face, next_d

assert get_next((0, 0), (1, 0), 0) == ((1,0), 0, (1,0))   
assert get_next((0, 5), (-1, 0), 0) == ((5,0), 5, (0,1))  
assert get_next((5, 0), (0, -1), 0) == ((5,0), 4, (0,1))  
assert get_next((49, 5), (1, 0), 0) == ((0,5), 2, (1,0))  
assert get_next((5, 49), (0, 1), 0) == ((5,0), 1, (0,1))  


# def get_next(pos, d):
#     test = (pos[0] + d[0], pos[1] + d[1])
#     if test not in grid:
#         if d == (1, 0):
#             test = (min([x[0] for x in grid.keys() if x[1] == test[1]]), test[1])
#         elif d == (-1, 0):
#             test = (max([x[0] for x in grid.keys() if x[1] == test[1]]), test[1])
#         elif d == (0, 1):
#             test = (test[0], min([x[1] for x in grid.keys() if x[0] == test[0]]))
#         elif d == (0, -1):
#             test = (test[0], max([x[1] for x in grid.keys() if x[0] == test[0]]))
#         else:
#             print("very bad")

#     assert test in grid
#     if grid[test] == "#":
#         return pos

#     return test

moves_i = 0
for n in parse_ints(moves):
    d = dirs[dir_i % len(dirs)]

    
    print(pos, face, d)
    print(n)

    for _ in range(n):
        pos, face, d = get_next(pos, d, face)

        # print(grid[pos], pos)
        # assert grid[pos] == "."
        assert faces[face][pos] == "."
        assert d in dirs
        dir_i = dirs.index(d)

    while moves[moves_i].isdigit():
        moves_i += 1
        if moves_i >= len(moves):
            break

    if moves_i < len(moves):
        m = moves[moves_i]
        print(m)
        assert m == "L" or m == "R"
        if m == "L":
            dir_i -= 1
        else:
            dir_i += 1

    moves_i += 1

print(pos, dir_i, face)

# print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + (dir_i % len(dirs)))
print((pos[0] + offsets[face][0] + 1) * 1000 + (pos[1] + offsets[face][1] + 1) * 4 + (dir_i % len(dirs)))