import itertools
import networkx as nx

# with open("input25test.txt", "r") as file:
with open("input25.txt", "r") as file:
    data = file.read().split("\n")

G = nx.Graph()

for line in data:
    name, l = line.split(":")
    l = l.split()

    for n in l:
        G.add_edge(name, n, capacity=1)
        G.add_edge(n, name, capacity=1)   
  
for a, b in itertools.combinations(G.nodes(), 2):
    n, parts = nx.minimum_cut(G, a, b)

    if n == 3:
        print(len(parts[0]) * len(parts[1]))
        break
