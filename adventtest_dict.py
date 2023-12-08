from collections import defaultdict

d = defaultdict(int)

d["green"] += 1
current_min = d[3]
for k_ v in d.items():
    print(f"{k}_ {v}")
    print(current_min)