from itertools import product

with open("../inputs/day07.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


def calc(left: int, right: int, operation: str) -> int:
    if operation == "+":
        return left + right
    elif operation == "|":
        return int(f"{left}{right}")
    else:
        return left * right


def is_possible(
    target: int,
    value: int,
    numbers: tuple[int, ...],
    operations: tuple[str, ...],
    pos: int,
) -> bool:
    if pos == len(numbers) - 1:
        return calc(value, numbers[pos], operations[pos]) == target

    value = calc(value, numbers[pos], operations[pos])

    if value > target:
        return False

    return is_possible(target, value, numbers, operations, pos + 1)


total = 0
for line in lines:
    target = int(line.split(": ")[0])
    values = [int(x) for x in line.split(" ")[1:]]

    for ops in product("+*", repeat=len(values) - 1):
        if is_possible(target, values[0], tuple(values[1:]), ops, 0):
            total += target
            break

print(total)


total = 0
for i, line in enumerate(lines):
    target = int(line.split(": ")[0])
    values = [int(x) for x in line.split(" ")[1:]]

    for ops in product("+*|", repeat=len(values) - 1):
        if is_possible(target, values[0], tuple(values[1:]), ops, 0):
            total += target
            break

print(total)
