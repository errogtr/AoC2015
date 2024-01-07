import re
from string import ascii_lowercase

num2letter = dict(enumerate(ascii_lowercase))
letter2num = {c: n for n, c in num2letter.items()}


def to_base_26(password):
    return sum(letter2num[c] * 26 ** i for i, c in enumerate(reversed(password)))


def from_base_26(num):
    password = ""
    while num:
        password += num2letter[num % 26]
        num //= 26
    return password[::-1]


def validate(password):
    return all((
        re.search(r"abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", password),
        re.search(r"[iol]", password) is None,
        re.search(r"(\w)\1.*(\w)\2", password)
    ))


def increment(password):
    return from_base_26(to_base_26(password) + 1)


def next_password(password):
    while not validate(password):
        password = increment(password)
    return password


with open("data") as f:
    password = f.read()


# ==== PART 1 ====
password = next_password(password)
print(password)

# ==== PART 2 ====
print(next_password(increment(password)))
