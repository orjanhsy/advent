import sys
from collections import defaultdict


def max_card(hand):
    occurances = defaultdict(int)
    for c in hand:
        occurances[c] += 1
    return max(occurances.values())


def rank_hands(lines):
    ranks = [list() for i in range(7)]
    hands = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        nondupe = len(set(hand))
        if nondupe == 1:
            ranks[6].append((hand, bid))

        if nondupe == 2:
            if max_card(hand) == 4:
                ranks[5].append((hand, bid))
            else:
                ranks[4].append((hand, bid))

        if nondupe == 3:
            if max_card(hand) == 3:
                ranks[3].append((hand, bid))
            else:
                ranks[2].append((hand, bid))

        if nondupe == 4:
            ranks[1].append((hand, bid))

        if nondupe == 5:
            ranks[0].append((hand, bid))

    return ranks

def sort_rank(rank):
    points = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    for i in range(2, 10):
        points[str(i)] = i

    print(points)
    for i in range(len(rank)):
        hand, bid = rank[i]
        rank[i] = (list(hand), bid)

    for i in range(len(rank) - 1):
        for j in range(len(rank) - i - 1):
            c = 0
            hand1 = rank[j][0]
            hand2 = rank[j + 1][0]
            while hand1[c] == hand2[c]:
                c += 1
            if points[hand1[c]] > points[hand2[c]]:
                rank[j], rank[j + 1] = rank[j+1], rank[j]






def main(lines):
    ranks = rank_hands(lines)

    for rank in ranks:
        sort_rank(rank)

    ordered = []
    for rank in ranks:
        for hand in rank:
            ordered.append(hand)
    total = 0
    print(ordered)
    for hand in ordered:
        _, bid = hand
        print(f"Bid: {bid} * {ordered.index(hand) + 1}")
        total += bid * (ordered.index(hand) + 1)
    print(total)

main(sys.stdin.read().splitlines())