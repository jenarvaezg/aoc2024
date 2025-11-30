import math
from functools import cache
from collections import defaultdict


with open("../inputs/day11.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

stones: dict[str, int] = defaultdict(lambda: 0)
for stone in lines[0].split():
    stones[stone] += 1


def process(stones: dict[str, int]) -> dict[str, int]:
    new_stones: dict[str, int] = defaultdict(lambda: 0)
    for k, v in stones.items():
        if k == "0":
            new_stones["1"] += v
        elif len(k) % 2 == 0:
            new_stones[k[: len(k) // 2]] += v
            new_stones[str(int(k[len(k) // 2 :]))] += v
        else:
            new_stones[str(int(k) * 2024)] += v

    return new_stones


for i in range(25):
    stones = process(stones)

print(sum(stones.values()))


# 25 + 50 = 75
for i in range(50):
    stones = process(stones)

print(sum(stones.values()))
