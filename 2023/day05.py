with open("input05.txt", "r") as file:
    data = file.read().split("\n\n")


seeds_data = data[0].split(":")[1]
map_data = data[1:]

seeds_data = [int(n) for n in seeds_data.split()]
current = [(seeds_data[i], seeds_data[i+1]) for i in range(0, len(seeds_data), 2)]
# print(current)

for i, line in enumerate(map_data):
    map_data = line.split("\n")
    name = map_data[0]
    maps = map_data[1:]

    # print(name)

    maps = [[int(n) for n in m.split()] for m in maps]
    maps = sorted(maps, key=lambda x: x[1])
    # print(maps)

    next = []
    for s in current:
        start, n = s
        end = start + n

        found = False
        for m in maps:
            m_end = m[1] + m[2]
            m_start = m[1]
            if start >= m_start and start < m_end:
                # print("found", s, m)

                mapped = (start - m[1]) + m[0]
                
                if end < m_end:
                    next.append((mapped, n))
                else:
                    remaining = end - m_end
                    # print("remaining:", remaining)

                    next.append((mapped, n - remaining))

                    # print("go again?", m_end, remaining)
                    current.append((m_end, remaining))

                    # start = m_end+1
                    # n = remaining

                # print(mapped)
                # next.append(mapped)

                found = True

        if not found:
            next.append(s)

    # print(next)
    current = next


print(min([x[0] for x in current]))






# PART 1

# current = [int(n) for n in seeds_data.split()]

# for i, line in enumerate(map_data):
#     map_data = line.split("\n")
#     name = map_data[0]
#     maps = map_data[1:]

#     print(name)

#     maps = [[int(n) for n in m.split()] for m in maps]

#     next = []
#     for s in current:
#         found = False
#         for m in maps:
#             if s >= m[1] and s <= m[1] + m[2]:
#                 # print("found", s, m)
#                 mapped = (s - m[1]) + m[0]
#                 # print(mapped)
#                 next.append(mapped)
#                 found = True
#                 break
#         if not found:
#             next.append(s)
#     # print(next)
#     current = next

# print(min(current))