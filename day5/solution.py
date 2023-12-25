import re


def is_nice(s):
    return (
        True
        if (
            re.search(r"([aeiou]\w*){3,}", s)
            and re.search(r"(\w)\1", s)
            and not re.search(r"ab|cd|pq|xy", s)
        )
        else False
    )


def is_better(s):
    return (
        True if (re.search(r"(\w)\w\1", s) and re.search(r"(\w{2}).*\1", s)) else False
    )


with open("data") as f:
    strings = f.read().splitlines()

# == PART 1 ==
print(sum(is_nice(s) for s in strings))

# == PART 2 ==
print(sum(is_better(s) for s in strings))
