import sys


def record_overview(lines):
    races = []
    for line in lines:
        numbers = []
        number = ""
        c = 0
        while c < len(line):
            while line[c].isdigit():
                number += line[c]
                c += 1
                if c == len(line):
                    break
            if len(number) > 0:
                numbers.append(int(number))
            number = ""
            c += 1
        races.append(numbers)
    records = dict()
    for i in range(len(races[0])):
        records[races[0][i]] = races[1][i]
    return records


def beat_record(time, distance):
    avaliable = time
    speed = 0
    possible = 0

    while speed*avaliable <= distance and avaliable > 0:
        avaliable -= 1
        speed += 1

    while speed*avaliable > distance:
        avaliable -= 1
        speed += 1
        possible += 1

    return possible


def main(lines):
    records = record_overview(lines)
    print(records)

    choices = []
    for time, distance in records.items():
        choices.append(beat_record(time, distance))

    print(choices)
    total = 1
    for i in choices:
        total *= i

    print(total)


main(sys.stdin.read().splitlines())