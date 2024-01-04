import sys
from collections import defaultdict


def left(node, E):
    return E[node][0]


def right(node, E):
    return E[node][1]


def find_instructions(lines):
    return lines[0].strip().replace('L', 'left ').replace('R', 'right ').split()


def make_graph(lines):
    E = defaultdict(list)
    for line in lines[2::]:
        line = ''.join([c for c in line if c.isalpha() or c == " "]).split()
        node, e1, e2 = line

        E[node].append(e1)
        E[node].append(e2)

    return E


def find_z(E, instructions):
    node = 'AAA'
    steps = 0
    while True:
        for instr in instructions:
            steps += 1
            node = globals()[instr](node, E)
            if node == 'ZZZ':
                return steps


def main(lines):
    instructions = find_instructions(lines)
    print(instructions)

    E = make_graph(lines)
    print(find_z(E, instructions))


main(sys.stdin.read().splitlines())