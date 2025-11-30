import re

with open("../inputs/day13.txt") as f:
    cases = [x.strip() for x in f.read().split("\n\n")]


def solve(case: str, shift=0) -> int:
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", case))

    px += shift
    py += shift

    a = round((py / by - px / bx) / (ay / by - ax / bx))

    b = round((px - a * ax) / bx)

    if a * ax + b * bx == px and a * ay + b * by == py:
        return 3 * a + b

    return 0


total = 0
for case in cases:
    total += solve(case)
print(total)


total = 0
for case in cases:
    total += solve(case, shift=10_000_000_000_000)
print(total)
