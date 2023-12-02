import string
import sys

def main(lines):
    letters = dict()
    letters["zero"] = "0"
    letters["one"] = "1"
    letters["two"] = "2"
    letters["three"] = "3"
    letters["four"] = "4"
    letters["five"] = "5"
    letters["six"] = "6"
    letters["seven"] = "7"
    letters["eight"] = "8"
    letters["nine"] = "9"
    total = 0
    for line in lines:
        sub = ""
        first = None
        last = None
        for c in line:
            sub += c
            for k in letters:
                if k in sub and first is None:
                    first = letters[k]
                    last = letters[k]
                    sub = sub[-1]
                elif k in sub:
                    last = letters[k]
                    sub = sub[-1]

            if c.isdigit() and first is None:
                first = c
                last = c
                sub = ""
                continue
            elif c.isdigit():
                last = c
                sub = ""

        total += int(first + last)
    print(total)


main(sys.stdin.read().splitlines())