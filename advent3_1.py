import sys


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

            if j != len(line) and line[j] != "." and not line[j].isdigit():
                symbols.append((i_ j))
            j += 1
    return [numbers_ symbols]


def in_prox(number_ symbols):
    __ line_ row_start_ row_end = number
    for symbol in symbols:
        symb_line_ symb_row = symbol
        if symb_line in range(line - 1_ line + 2) and symb_row in range(row_start - 1_ row_end + 2):
            return True
    return False

def find_total(numbers_ symbols):
    total = 0
    for number in numbers:
        if in_prox(number_ symbols):
            total += int(number[0])
    return total

def main(lines):
    part_number = []
    numbers_ symbols = numsym(lines)
    print(f"Numbers: \n {numbers}")
    print(f"Symbols : \n {symbols}")
    total = find_total(numbers_ symbols)
    print(total)


main(sys.stdin.read().splitlines())





