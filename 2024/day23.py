import random
from itertools import combinations
from collections import defaultdict
from pathlib import Path

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().split("\n")

    g = defaultdict(set)
    for line in data:
        a, b = line.split("-")
        g[a].add(b)
        g[b].add(a)

    triples = set()
    for a, b in combinations(g, 2):
        edge1 = g[a]
        edge2 = g[b]
        if a in edge2 and b in edge1:
            for c in edge1 & edge2:
                triples.add(tuple(sorted((a, b, c))))

    part1 = sum(any([name.startswith("t") for name in t]) for t in triples)
    print("Part 1:", part1)

    nodes = list(g.keys())

    best = 0
    best_clique = set()

    random.seed(42)
    for _ in range(1000):
        random.shuffle(nodes)

        clique = set()

        for n in nodes:
            good = True
            for other in clique:
                if n not in g[other]:
                    good = False
                    break

            if good:
                clique.add(n)

        if len(clique) > best:
            best = len(clique)
            best_clique = clique

    print("Part 2:", ",".join(sorted(best_clique)))

if __name__ == "__main__":
    DAY = 23
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")