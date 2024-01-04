import sys
from collections import defaultdict


def max_card(hand):
    occurances = defaultdict(int)
    jokers = 0
    for c in hand:
        if c == 'J':
            occurances[c] = 0
            jokers += 1
            continue
        occurances[c] += 1
    occurance = []
    highest = max(occurances.values())
    for k, v in occurances.items():
        if v == highest:
            del occurances[k]
            break

    second_highest = 0
    if len(occurances.values()) > 0:
        second_highest = max(occurances.values())

    return highest + jokers, second_highest



def rank_hands(lines):
    ranks = [list() for i in range(7)]
    hands = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)

        initial, second = max_card(hand)

        print(f"Hand: {hand}, {(initial, second)}")
        if initial == 5:
            ranks[6].append((hand, bid))

        if initial == 4:
            ranks[5].append((hand, bid))

        if initial == 3:
            if second == 2:
                ranks[4].append((hand, bid))
            else:
                ranks[3].append((hand, bid))

        if initial == 2:
            if second == 2:
                ranks[2].append((hand, bid))
            else:
                ranks[1].append((hand, bid))

        if initial == 1:
            ranks[0].append((hand, bid))

    return ranks

def sort_rank(rank):
    points = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10}
    for i in range(2, 10):
        points[str(i)] = i

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
                print(f"Hand1: {hand1} swapped with Hand2 {hand2}")
                rank[j], rank[j + 1] = rank[j+1], rank[j]






def main(lines):
    ranks = rank_hands(lines)

    print(ranks)
    for rank in ranks:
        sort_rank(rank)

    print(ranks)
    ordered = []
    for rank in ranks:
        for hand in rank:
            ordered.append(hand)
    total = 0

    for i in range(len(ordered)):
        print(''.join(ordered[i][0]))


    for hand in ordered:
        _, bid = hand
        # print(f"Bid: {bid} * {ordered.index(hand) + 1}")
        total += bid * (ordered.index(hand) + 1)
    print(total)


main(sys.stdin.read().splitlines())