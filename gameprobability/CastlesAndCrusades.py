import math
from itertools import product

rolls = product(range(1, 7), repeat=3)
stats = {}
for roll in rolls:
    rollTotal = str(sum(roll))
    if rollTotal in stats:
        stats[rollTotal] += 1
    else:
        stats[rollTotal] = 1

totalRolls = sum([val for val in stats.values()])
for score, numAppearing in stats.items():
    print(f"{str(score)}: {numAppearing / totalRolls * 100}")
