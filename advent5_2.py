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
    source = seed
    for relations in maps:

        for relation in maps[relations]:
            dest = relation[0]
            s = relation[1]
            rnge = relation[2]
            rel = relation[3]

            if s <= source < s + rnge:
                source = source - rel
                break

        info = relations.split("-")[2]
        # print(f"{info}, {source}")

    return source


def main(lines):
    seeds = [int(i) for i in lines[0].replace("seeds:", "").split()]
    new_seeds = []
    i = 1
    while i < len(seeds):
        j = i - 1
        rnge = seeds.pop(i)
        start = seeds[j]
        for y in range(start, start + rnge):
            new_seeds.append(y)

        i += 2
    print(f"Seeds with ranges: {new_seeds}")

    print(f"Seeds: {new_seeds}")
    maps = create_mappings(lines)
    for m in maps:
        print(f"{m}: {maps[m]}")

    lowest = None
    for seed in new_seeds:

        print(f"\nSeed:{seed}")
        location = traverse_map(seed, maps)
        if lowest is None or location < lowest:
            lowest = location

    print(f"\nLOWEST = {lowest}")


main(sys.stdin.read().splitlines())


#new_seeds: 79 14 55 13
# seed-to-soil map:
# 50 ( range start) 98 (source range start) 2 (range length)
# 52 50 48
