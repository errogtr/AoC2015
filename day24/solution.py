from itertools import combinations
from math import prod


def entanglements(nums, groups):
    for k in range(1, len(nums)):
        entanglements = [
            c
            for c in combinations(nums, k)
            if sum(c) == sum(nums - set(c)) // (groups - 1)
        ]
        if entanglements:
            return min(prod(e) for e in entanglements)


with open("data") as f:
    nums = {int(x) for x in f.readlines()}


# ==== PART 1 ====
print(entanglements(nums, 3))

# ==== PART 2 ====
print(entanglements(nums, 4))
