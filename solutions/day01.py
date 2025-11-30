from collections import Counter

with open("../inputs/day01.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


left = []
right = []
for line in lines:
    splitted = line.split()
    left.append(int(splitted[0]))
    right.append(int(splitted[1]))


sorted_left = sorted(left)
sorted_right = sorted(right)

total_diff = 0
for one, other in zip(sorted_left, sorted_right):
    total_diff += abs(one - other)

# Part 1
print(total_diff)

right_ctr = Counter(right)

score = 0
for v in left:
    score += v * right_ctr[v]

print(score)
