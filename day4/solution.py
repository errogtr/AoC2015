from hashlib import md5


def hash(s):
    return md5(s.encode()).hexdigest()


def lowest(key, l):
    i = 0
    while True:
        if hash(f"{key}{i}").startswith("0" * l):
            break
        i += 1
    return i


with open("day4/data") as f:
    key = f.read()

# ==== PART 1 ====
print(lowest(key, 5))

# ==== PART 2 ====
print(lowest(key, 6))
