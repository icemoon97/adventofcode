import heapq
from pathlib import Path

def part1(data: str):
    disk = []
    for i, n in enumerate(map(int, data)):
        if i % 2 == 0:
            disk.extend([i // 2] * n)
        else:
            disk.extend([-1] * n)

    # we know final disk state will be full up to index len(block_idx), then empty
    # so just compute checksum in place by tracking block/empty idx
    block_idx = [i for i in range(len(disk)) if disk[i] >= 0]
    empty_idx = [i for i in range(len(disk)) if disk[i] < 0]

    check = 0

    empty_p = 0
    for i in block_idx[::-1]:
        id = disk[i]

        if i >= len(block_idx):
            check += id * empty_idx[empty_p]
            empty_p += 1
        else:
            check += id * i

    return check
    
def parse_disk(data: str):
    files = []
    # min-heap for sizes 0-9 of free space
    free = [[] for _ in range(10)]

    p = 0
    for i, n in enumerate(map(int, data)):
        block = (p, n)
        if i % 2 == 0:
            files.append(block)
        else:
            heapq.heappush(free[n], block)
        p += n

    return files, free

def checksum(files: list[tuple[int, int]]) -> int:
    check = 0
    for id, (p, size) in enumerate(files):
        check += id * p * size
        check += id * (size * (size - 1) // 2)
    return check

def main(input_path: Path):
    with open(input_path, "r") as file:
        data = file.read().rstrip("\n")

    print("Part 1:", part1(data))

    files, free = parse_disk(data)

    for id in range(len(files) - 1, -1, -1):
        file_p, file_size = files[id]

        # peek at open spaces of large enough size, pull earliest
        openings = [h[0] for h in free[file_size:] if h]
        if not openings:
            continue

        free_p, free_size = min(openings)
        if free_p > file_p:
            continue

        files[id] = (free_p, file_size)

        heapq.heappop(free[free_size])
        rem = free_size - file_size
        rem_start = free_p + file_size
        heapq.heappush(free[rem], (rem_start, rem))
    
    print("Part 2:", checksum(files))

if __name__ == "__main__":
    DAY = 9
    print("===== Tests =====")
    main(f"tests/day{DAY:02}.txt")
    print("===== Input =====")
    main(f"inputs/day{DAY:02}.txt")