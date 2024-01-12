from collections import defaultdict

target = 34000000

# ==== PART 1 ====
house = defaultdict(int)
for i in range(1, (target // 10) + 1):
    for j in range(i, (target // 10) + 1, i):
        house[j] += 10 * i
print(next(k for k, v in house.items() if v >= target))


# ==== PART 2 ====
house = defaultdict(int)
for i in range(1, (target // 10) + 1):
    for j in range(i, 51 * i, i):
        house[j] += 11 * i
print(next(k for k, v in house.items() if v >= target))

