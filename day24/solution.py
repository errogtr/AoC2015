from itertools import combinations
from math import prod


def entanglements(nums, groups):
    entaglements = list()
    for k in range(1, len(nums)):
        for comb in combinations(nums, k):
            if sum(comb) == sum(nums - set(comb)) // (groups - 1):
                entaglements.append(comb)
        if entaglements:
            return min(prod(e) for e in entaglements)


with open("data") as f:
    nums = {int(x) for x in f.readlines()}


# ==== PART 1 ====
print(entanglements(nums, 3))

# ==== PART 2 ====
print(entanglements(nums, 4))
