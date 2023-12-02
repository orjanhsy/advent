import string
import sys
alph = string.ascii_lowercase



def main(lines):
    total = 0
    for line in lines:
        first = None
        last = None
        for c in line:
            if c not in alph and first is None:
                first = c
                last = c
                continue
            if c not in alph:
                last = c
        total += int(first+last)

    print(total)


main(sys.stdin.read().splitlines())
