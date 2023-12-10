import sys
from collections import defaultdict

def sort_string(hands):
    points = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    for i in range(2, 10):
        points['i'] = i

    sorted_hands = [None] * len(hands)
    i = 0



def find_hands(lines):
    hands = dict()
    for line in lines:
        line = line.split()
        hand = line[0]
        value = line[1]
        unique = len(set(hand))
        rank = len(hand) - unique
        if rank >= 3:
            rank += 1
        if unique == 3 or unique == 2:
            dupes = defaultdict(int)
            for card in hand:
                dupes[card] += 1
            if unique == 3:
                if max(dupes.values()) == 3:
                    hands[hand] = (rank + 1, value)
                else:
                    hands[hand] = (rank, value)
                continue
            elif unique == 4:
                if max(dupes.values()) == 4:
                    hands[hand] = (rank + 1, value)
                else:
                    hands[hand] = (rank, value)
                continue
        hands[hand] = (rank, value)
    return hands


def main(lines):

    hands = find_hands(lines)
    print(hands)

    ranked = [list() for i in range(7)]
    print(ranked)
    for hand, info in hands.items():
        rank, value = info
        print(info)
        ranked[rank].append((rank, hand, value))
        print(ranked)

    ranked_sorted = []
    for rank in ranked:
        rank = sort_string(rank)
        ranked_sorted.append(rank)
    # print(f"RANKED PRE SORT {ranked}")





main(sys.stdin.read().splitlines())