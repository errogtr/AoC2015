from string import ascii_lowercase
from itertools import product


def is_nice(s):
    if (
        sum(s.count(v) for v in "aeiou") >= 3
        and any(x * 2 in s for x in ascii_lowercase)
        and all(x not in s for x in {"ab", "cd", "pq", "xy"})
    ):
        return True
    return False


def is_better(s):
    if any(x + y + x in s for x, y in product(ascii_lowercase, repeat=2)) and any(
        s[i + 2:].count(s[i:i + 2]) for i in range(len(s) - 3)
    ):
        return True
    return False


with open("data") as f:
    strings = f.read().splitlines()

# == PART 1 ==
print(sum(is_nice(s) for s in strings))

# == PART 2 ==
print(sum(is_better(s) for s in strings))
