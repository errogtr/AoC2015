from itertools import combinations
from math import prod


def entanglements(nums, target):
    for k in range(1, len(nums)):
        entanglements = [prod(c) for c in combinations(nums, k) if sum(c) == target]
        if entanglements:
            return min(entanglements)


with open("data") as f:
    nums = [int(x) for x in f.readlines()]


# ==== PART 1 ====
print(entanglements(nums, sum(nums) // 3))

# ==== PART 2 ====
print(entanglements(nums, sum(nums) // 4))
