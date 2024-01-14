import re
from itertools import product, chain

shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

weapons, armors, rings = list(), list(), list()
for table in shop.split("\n\n"):
    item_type = table.split()[0][:-1]
    for row in table.splitlines()[1:]:
        cost, damage, armor = map(int, row.split()[-3:])
        match item_type:
            case "Weapons":
                weapons.append((cost, damage, armor))
            case "Armor":
                armors.append((cost, damage, armor))
            case "Rings":
                rings.append((cost, damage, armor))

stats = list()
for equipment in chain(weapons, product(weapons, armors), product(weapons, armors, rings), product(weapons, armors, rings, rings)):
    if isinstance(equipment[0], tuple):
        cost, damage, armor = map(sum, zip(*equipment))
    else:
        cost, damage, armor = equipment
    stats.append((cost, damage, armor))


with open("data") as f:
    HP_b, D_b, A_b = map(int, re.findall(r"\d+", f.read()))

HP_p = 100

# ==== PART 1 ====
print(next(cost for cost, D_p, A_p in sorted(stats) if HP_p > HP_b // (D_p - A_b) * (D_b - A_p)))

# ==== PART 2 ====
print(next(cost for cost, D_p, A_p in reversed(sorted(stats)) if HP_p <= HP_b // (D_p - A_b) * (D_b - A_p)))
