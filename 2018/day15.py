from queue import PriorityQueue

data = [line.rstrip("\n") for line in open("input15.txt")]

n, m = len(data), len(data[0])

def get_adjacent(pos):
    adj = []
    for dir in [(1,0), (-1,0), (0,1), (0,-1)]:
        adj.append((pos[0] + dir[0], pos[1] + dir[1]))
    return adj

class Unit:
    def __init__(self, type, pos):
        self.type = type
        self.pos = pos
        self.health = 200
        self.damage = 3
        self.alive = True

    def __str__(self):
        return f"<{self.type}, {self.pos}, {self.health}>"

    def in_range(self, map, enemies):
        result = set()
        for e in enemies:
            for test in get_adjacent(e.pos):
                if test == self.pos or map[test[0]][test[1]] == ".":
                    result.add(test)

        return result

    def choose_move(self, map, enemies):
        # print("choose_move", self.__str__())
        possible = self.in_range(map, enemies)
        
        if len(possible) == 0:
            return self.pos
        if self.pos in possible:
            return self.pos

        searched = {self.pos}

        q = PriorityQueue() # priority is (dist, i, j)
        q.put((0, self.pos[0], self.pos[1]))

        while not q.empty():
            d, x, y = q.get()
            if (x,y) in possible:
                return self._pick_first_step(map, (x,y), d)

            for test in get_adjacent((x,y)):
                if test not in searched and map[test[0]][test[1]] == ".":
                    searched.add(test)
                    q.put((d + 1, test[0], test[1]))

        return self.pos

    def _pick_first_step(self, map, target, max_d):
        searched = {target}
        candidates = set()

        q = PriorityQueue()
        q.put((1, target[0], target[1]))

        while not q.empty():
            d, x, y = q.get()
            if d > max_d:
                break
            elif d == max_d:
                candidates.add((x,y))

            for test in get_adjacent((x,y)):
                if test not in searched and map[test[0]][test[1]] == ".":
                    searched.add(test)
                    q.put((d + 1, test[0], test[1]))

        return sorted(list(candidates & set(get_adjacent(self.pos))))[0]

def printMap(map):
    for i in range(n):
        for j in range(m):
            print(map[i][j], end="")
        print()

def simulate_battle(data, elf_damage=3):
    units: list[Unit] = []

    map = [[0 for _ in range(m)] for _ in range(n)]
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "E":
                u = Unit("E", (i,j))
                u.damage = elf_damage
                units.append(u)
            elif c == "G":
                units.append(Unit("G", (i,j)))
            map[i][j] = c

    elves = list(filter(lambda x: x.type == "E", units))
    goblins = list(filter(lambda x: x.type == "G", units))

    elf_deaths = 0

    step = 0
    battle_active = True
    while battle_active:
        # print(step)
        for u in units:
            if not u.alive:
                continue

            enemies = elves if u.type == "G" else goblins
            if len(enemies) == 0:
                battle_active = False
                break

            move = u.choose_move(map, enemies)
            
            map[u.pos[0]][u.pos[1]] = "."
            map[move[0]][move[1]] = u.type
            u.pos = move

            attacks = []
            adj = get_adjacent(u.pos)
            for other in enemies:
                if other.pos in adj:
                    attacks.append(other)
            
            if len(attacks) > 0:
                target = sorted(attacks, key=lambda x: (x.health, x.pos))[0]
                target.health -= u.damage
                if target.health <= 0:
                    map[target.pos[0]][target.pos[1]] = "."
                    target.alive = False
                    enemies.remove(target)

                    if target.type == "E":
                        elf_deaths += 1

        units = list(filter(lambda x: x.alive, units))
        units.sort(key=lambda x: x.pos)

        # printMap(map)
        # for u in units:
        #     print(u)

        if not battle_active:
            outcome = step * sum([u.health for u in units])
            return outcome, elf_deaths

        step += 1


print("Part 1:", simulate_battle(data)[0])

for damage in range(3, 100):
    outcome, deaths = simulate_battle(data, elf_damage=damage)
    if deaths == 0:
        print("Part 2:", outcome)
        break

#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######

#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######

#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######

#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######

#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######

#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
    