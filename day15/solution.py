import re
from math import prod


def f(X, I, skip_cal=True):
    C = skip_cal or sum(s * i[-1] for s, i in zip(X, I)) == 500
    return (
        prod(
            max(0, sum(x * a for x, a in zip(X, alpha)))
            for alpha in zip(*(i[:-1] for i in I))
        )
        * C
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

# ==== PRINT 1 ====
print(max(f(X, ingredients) for X in spoons))

# ==== PRINT 2 ====
print(max(f(X, ingredients, skip_cal=False) for X in spoons))
