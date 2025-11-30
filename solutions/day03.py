import re

with open("../inputs/day03.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


pattern_1 = re.compile(r"mul\((\d*),(\d*)\)")

total = 0
for line in lines:
    for match in pattern_1.findall(line):
        print(match)
        total += int(match[0]) * int(match[1])

print(total)

pattern_2 = re.compile(r"(mul\((\d*),(\d*)\)|don't()|do())")

enabled = True
total = 0
for line in lines:
    for match in pattern_2.findall(line):
        print(match)
        if match[0] == "don't":
            enabled = False
        elif match[0] == "do":
            enabled = True
        elif "mul" in match[0] and enabled:
            print("Multiplying", match)
            total += int(match[1]) * int(match[2])

print(total)
