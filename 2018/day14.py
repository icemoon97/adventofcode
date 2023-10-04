target = "074501"
# target = "59414"

scores = "37"
e1 = 0
e2 = 1

while target not in scores[-7:]:
    scores += str(int(scores[e1]) + int(scores[e2]))

    e1 = (e1 + int(scores[e1]) + 1) % len(scores)
    e2 = (e2 + int(scores[e2]) + 1) % len(scores)

print(scores.index(target))