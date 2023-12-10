import sys
from collections import deque
from collections import defaultdict


def separate_card(card):
    i = 2
    wins = []
    had = []
    while card[i] != "|":
        wins.append(card[i])
        i += 1
    i = i + 1

    while i < len(card):
        had.append(card[i])
        i += 1
    return [wins, had]


def won(card):
    wins, had = separate_card(card)
    w = 0
    for i in had:
        if i in wins:
            w += 1
    return w


def main(lines):
    cards = dict()
    for i in range(len(lines)):
        card = lines[i].split()
        # print(f"Card{i} won {won(card)} times")
        cards[i] = [card, 1]

    for card, v in cards.items():
        for i in range(v[1]):
            w = won(v[0])
            if w == 0:
                break
            # print(f"Card {card} has {w} wins")
            while w > 0:
                if card + w < len(cards):
                    cards[card + w][1] += 1
                w -= 1

    totals = [total[1] for total in cards.values()]
    print(totals)
    total_sum = sum([total[1] for total in cards.values()])
    print(f"Total cards: {total_sum}")


main(sys.stdin.read().splitlines())