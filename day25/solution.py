import re

with open("data") as f:
    row, col = map(int, re.search(r"(\d+)\D*(\d+)", f.read()).groups())

current = 20151125
for s in range(2, row + col):
    for x in range(1, s + 1):
        y = s - x + 1
        current = (current * 252533) % 33554393
        if (y, x) == (row, col):
            break
print(current)
