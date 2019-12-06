import random

stats = {}

for i in range(1000):
    getal = random.randint(1, 5)
    getal = str(getal)
    if getal in stats:
        stats[getal] += 1
    else:
        stats[getal] = 1


ordered_stats = sorted(stats.items())
print(stats.items())
print(ordered_stats)
for item in ordered_stats:
    print("{}: {}".format(item[0], item[1]))