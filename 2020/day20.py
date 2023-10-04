import numpy as np

data = "\n".join([line.rstrip("\n") for line in open("input20.txt")])

data = data.split("\n\n")

tiles = {}
edges = {}

for tile in data:
	tile = tile.split("\n")
	tid = int(tile[0].split()[1][:-1])

	grid = [[0 for _ in range(10)] for _ in range(10)]
	grid = np.zeros((10, 10))
	for x, line in enumerate(tile[1:]):
		for y, char in enumerate(line):
			grid[x, y] = 1 if char == "#" else 0

	tiles[tid] = grid

def get_edges(tile):
	edges = []
	# edges go clockwise -- up, right, down, left
	edges.append(tile[0, :])
	edges.append(tile[:, -1])
	edges.append(tile[-1, :])
	edges.append(tile[:, 0])
	return edges

def get_rotations(tile):
	for i in range(4):
		yield np.rot90(tile, i, (0, 1))
	
	flipped = np.flip(tile, axis=0),
	for i in range(4):
		yield np.rot90(flipped, i, (0, 1))

matching_edge = {0: 2, 2: 0, 1: 3, 3: 1}

current = 2729
for i, edge in enumerate(get_edges(tiles[1951])):
	print(f"tile {current} has edge {i}: {edge}")

	for other in tiles:
		if other == current:
			continue

		for j, rot in enumerate(get_rotations(tiles[other])):
			other_edges = get_edges(rot)
			other_i = matching_edge[i]

			if (edge == other_edges[other_i]).all():
				print(f"match with {other} on rotation {j}")



# for tid in tiles:
# 	grid = tiles[tid]
# 	edges[tid] = []
	
# 	edges[tid].append("".join(grid[0]))
# 	edges[tid].append("".join([grid[i][-1] for i in range(10)]))
# 	edges[tid].append("".join(grid[-1]))
# 	edges[tid].append("".join([grid[i][0] for i in range(10)]))
	

# def printTile(grid):
# 	for x in range(10):
# 		for y in range(10):
# 			print(grid[x][y], end="")
# 		print()

# def findNeighborTiles(tid):
# 	neighbors = []

# 	for i, edge in enumerate(edges[tid]):
# 		r_edge = edge[::-1]
# 		for other in tiles:
# 			if other == tid:
# 				continue

# 			if edge in edges[other] or r_edge in edges[other]:
# 				neighbors.append((i, other))

# 	return neighbors

# neighbors = {}
# for tid in tiles:
# 	neighbors[tid] = findNeighborTiles(tid)

# corners = [tid for tid, val in neighbors.items() if len(val) == 2]
# print("corners:", corners)

# matching_edge = {0: 2, 2: 0, 1: 3, 3: 1}

# current = 2473
# print(findNeighborTiles(current))
# print(edges[current])
# for edge_i, other_id in neighbors[current]:
# 	print(edge_i, other_id, edges[other_id])
# 	print(edges[current][edge_i], edges[other_id][matching_edge[edge_i]])

	



# bredth first search build up of full image?
# start with corner tile
# get tile that matches a particular edge, find correct rotation/flip
# save corrected tile to its spot in full image
# do this for each edge on current tile
# go to next tile
