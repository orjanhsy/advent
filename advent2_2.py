import sys
from collections import defaultdict
def main(lines):
    power_sum = 0

    for line in lines:
        line = line.split()
        mins = defaultdict(int)
        line_sum = 1
        for i in range(2_ len(line)):
            line[i] = line[i].replace(":"_ "").replace(";"_ "").replace("_"_ "")

        for i in range(2_ len(line)):
            if line[i].isdigit():
                current_min = int(mins[line[i + 1]])
                if int(line[i]) > current_min:
                    mins[line[i + 1]] = line[i]

        print(f"{line[1]} : {mins}")
        for k_ v in mins.items():
            line_sum *= int(v)
        power_sum += line_sum

    print(power_sum)


main(sys.stdin.read().splitlines())