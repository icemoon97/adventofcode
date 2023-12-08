from collections import Counter

with open("input07.txt", "r") as file:
    data = file.read().split("\n")

def hand_rank_part1(hand):
    card_rank = "23456789TJQKA"

    C = Counter(hand)
    kind = sorted(list(C.values()), reverse=True)
    ranks = [card_rank.index(c) for c in hand]

    return (kind, ranks)

def hand_rank_part2(hand):
    card_rank = "J23456789TQKA"

    C = Counter(hand)
    kind = sorted(list(C.values()), reverse=True)
    if "J" in C:
        num_j = C["J"]
        C2 = Counter(hand.replace("J", ""))
        kind = sorted(list(C2.values()), reverse=True)
        if len(kind) > 0:
            kind[0] += num_j
        else:
            kind.append(num_j)

    ranks = [card_rank.index(c) for c in hand]

    return (kind, ranks)

def calc_winnings(ranked):
    return sum([bid * (i+1) for i, (_, bid) in enumerate(ranked)])

hands = []
for line in data:
    hand, bid = line.split()
    bid = int(bid)
    hands.append((hand, bid))

part1 = sorted(hands, key=lambda h: hand_rank_part1(h[0]))
print("Part 1:", calc_winnings(part1))

part2 = sorted(hands, key=lambda h: hand_rank_part2(h[0]))
print("Part 2:", calc_winnings(part2))

# test_hands = ["AAAAA", "AA8AA", "2332", "TTT98", "23432", "A23A4", "23456", "33332", "2AAAA", "77888", "77788"]
# test_hands.sort(key=hand_rank)
# print(test_hands)