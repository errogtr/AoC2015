import re
from math import prod


def f(X, I):
    return prod(
        max(0, sum(x * a for x, a in zip(X, alpha)))
        for alpha in zip(*(i[:-1] for i in I))
    )


with open("data") as fp:
    ingredients = [
        [int(x) for x in re.findall(r"-*\d+", l)] for l in fp.read().splitlines()
    ]

T = 100
spoons = [
    (i, j, k, T - i - j - k)
    for i in range(1, T - len(ingredients))
    for j in range(1, T - i)
    for k in range(1, T - i - j)
]

# ==== PART 1 ====
print(max(f(X, ingredients) for X in spoons))

# ==== PART 2 ====
print(
    max(
        f(X, ingredients)
        for X in spoons
        if sum(s * i[-1] for s, i in zip(X, ingredients)) == 500
    )
)
