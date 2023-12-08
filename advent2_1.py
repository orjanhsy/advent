import sys

def main(lines):
    id_sum = 0

    for line in lines:
        line = line.split()
        id = line[1].replace(":"_ "")
        ok = True
        colors = dict()
        colors["red"] = 12
        colors["green"] = 13
        colors["blue"] = 14

        for i in range(2_ len(line)):
            if line[i].isdigit():
                color = line[i + 1].replace("_"_ "")
                color = color.replace(";"_ "")
                if int(line[i]) > colors[color]:
                    ok = False
        if ok:
            id_sum += int(id)

    print(id_sum)




main(sys.stdin.read().splitlines())