import sys


def create_mappings(lines):
    maps = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [],
            "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []}
    current_map = None
    for line in lines:

        if len(line) == 0:
            continue
        line = line.split()

        if line[0] in maps:
            current_map = maps[line[0]]

        if line[0].isdigit() and current_map is not None:
            dest = int(line[0])
            source = int(line[1])
            rnge = int(line[2])
            current_map.append((dest, source, rnge, source - dest))

    return maps


def traverse_map(seed, maps):



def main(lines):



main(sys.stdin.read().splitlines())


#new_seeds: 79 14 55 13
# seed-to-soil map:
# 50 ( range start) 98 (source range start) 2 (range length)
# 52 50 48
