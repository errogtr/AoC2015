from itertools import combinations


with open("data") as f:
    containers = [int(x) for x in f.read().splitlines()]

# ==== PART 1 ====
combs = [c for i in range(2, len(containers) + 1) for c in combinations(containers, i) if sum(c) == 150]
print(len(combs))

# ==== PART 2 ====
min_containers = len(combs[0])
print(len([c for c in combs if len(c) == min_containers]))
