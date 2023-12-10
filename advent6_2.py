import sys


def record_overview(lines):
    numbers = []
    for line in lines:
        line = line.replace(" ", "")
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
                break
            c += 1
    record = dict()
    record[numbers[0]] = numbers[1]
    return record


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
    record = record_overview(lines)
    print(record)

    for time, distance in record.items():
        print(beat_record(time, distance))


main(sys.stdin.read().splitlines())