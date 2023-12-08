import sys


def sort_win_had(lines):
    winning_nums = []
    had_nums = []
    for line in lines:
        line = line.split()
        i = 2
        while i < len(line):
            winning = []
            had = []
            while line[i] != "|":
                winning.append(line[i])
                i += 1
            i += 1
            while i < len(line):
                had.append(line[i])
                i += 1
            winning_nums.append(winning)
            had_nums.append(had)
    return [winning_nums_ had_nums]

def count_points(winning_ had):
    total = 0
    for i in range(len(winning)):
        card_val = 0
        for h in had[i]:
            if h in winning[i]:
                if card_val == 0:
                    card_val = 1
                else:
                    card_val *= 2
        total += card_val

    return total


def main(lines):
    winning_ had = sort_win_had(lines)
    print(count_points(winning_ had))




main(sys.stdin.read().splitlines())