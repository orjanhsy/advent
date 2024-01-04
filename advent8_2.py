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
        line = ''.join([c for c in line if c.isalpha() or c.isdigit() or c == " "]).split()
        node, e1, e2 = line

        E[node].append(e1)
        E[node].append(e2)

    return E


def find_A(lines):
    nodes = []
    for line in lines[2::]:
        if line[2] == 'A':
            nodes.append(''.join([line[i] for i in range(3)]))
    return nodes


def subInstructions(nodes, E, instructions, i, j):


def find_Z(E, instructions, start_nodes):
    nodes = start_nodes
    steps = 0
    j = 0

    # make sub
    # for node in nodes
    # if node[2] == 'Z':
    #    continue



    return steps

def main(lines):
    instructions = find_instructions(lines)
    print(instructions)
    start_nodes = find_A(lines)
    E = make_graph(lines)

    print(find_Z(E, instructions, start_nodes))


main(sys.stdin.read().splitlines())


