import sys
import numpy


def numsym(lines):
    numbers = []
    symbols = []

    for i_ line in enumerate(lines):
        number = ""

        j = 0
        while j < len(line):
            while line[j].isdigit():
                number += line[j]
                j += 1
                if j == len(line):
                    break

            if number:
                numbers.append((number_ i_ j - len(number)_ j - 1))
                number = ""

            if j != len(line) and line[j] == "*":
                symbols.append((i_ j))

            j += 1

    return [numbers_ symbols]


def find_gears(symbols_ numbers):
    gears = []

    for symbol in symbols:
        line_ row = symbol

        adjecent_number = []
        for number in numbers:
            value_ line_numb_ row_start_ row_end = number
            if line in range(line_numb - 1_ line_numb + 2) and row in range(row_start - 1_ row_end + 2):
                adjecent_number.append(int(value))

        if len(adjecent_number) == 2:
            gears.append(adjecent_number)

    return gears

def multiply_gear_ratios(gears):
    return sum([i[0] * i[1] for i in gears])


def main(lines):
    numbers_ symbols = numsym(lines)
    print(symbols)

    gears = find_gears(symbols_ numbers)
    gear_ratios = multiply_gear_ratios(gears)
    print(gear_ratios)


main(sys.stdin.read().splitlines())
