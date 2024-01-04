import sys
from collections import defaultdict



def org_hisotires(lines):
    histories = dict()
    for line in lines:
        history = [int(i) for i in line.split()]
        diffs = []
        gen_diff(history, diffs)
        histories[line] = diffs[::-1]
    return histories

def gen_diff(history, diffs):
    diff = []
    i = 1
    while i < len(history):
        diff.append(history[i] - history[i-1])
        i += 1
    for i in range(len(diff) - 1):
        if diff[i] != diff[i+1]:
            gen_diff(diff, diffs)
            break
    diffs.append(diff)


def main(lines):
    histories = org_hisotires(lines)
    print(histories)


main(sys.stdin.read().splitlines())