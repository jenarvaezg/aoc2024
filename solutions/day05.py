with open("../inputs/day05.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


rules: list[tuple[int, int]] = []
updates: list[list[int]] = []
for line in lines:
    if line == "":
        continue

    if "|" in line:
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    else:
        updates.append([int(x) for x in line.split(",")])


def is_order_ok(rules_to_apply: list[tuple[int, int]], update: list[int]) -> bool:
    for rule in rules_to_apply:
        if not update.index(rule[0]) < update.index(rule[1]):
            return False

    return True


def reorder(rules_to_apply: list[tuple[int, int]], update: list[int]) -> list[int]:
    swapped = False

    for rule in rules_to_apply:
        a_index, b_index = update.index(rule[0]), update.index(rule[1])
        if not a_index < b_index:
            update[a_index], update[b_index] = update[b_index], update[a_index]
            swapped = True

    if swapped:
        return reorder(rules_to_apply, update)

    return update


total = 0
for update in updates:
    rules_to_apply = [rule for rule in rules if rule[0] in update and rule[1] in update]

    if is_order_ok(rules_to_apply, update):
        total += update[int(len(update) / 2)]

print(total)


total = 0
for update in updates:
    rules_to_apply = [rule for rule in rules if rule[0] in update and rule[1] in update]

    if is_order_ok(rules_to_apply, update):
        continue

    reordered = reorder(rules_to_apply, update)
    total += reordered[int(len(reordered) / 2)]

print(total)
