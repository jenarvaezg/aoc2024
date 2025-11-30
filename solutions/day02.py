with open("../inputs/day02.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


def is_safe_report(report: list[int], allow_errors: bool = False) -> bool:
    ascending = report[1] > report[0]
    for i in range(len(report) - 1):
        one, other = report[i], report[i + 1]
        diff = other - one

        if (
            abs(diff) < 1
            or abs(diff) > 3
            or (ascending and diff < 0)
            or (not ascending and diff > 0)
        ):
            return (
                # Try ignoring both numbers and zero (maybe the sign is wrong so we need to check that one too)
                (
                    is_safe_report(report[:i] + report[i + 1 :])
                    or is_safe_report(report[: i + 1] + report[i + 2 :])
                    or is_safe_report(report[1:])
                )
                if allow_errors
                else False
            )

    return True


safe_counter = 0
for line in lines:
    report = [int(x) for x in line.split()]

    if is_safe_report(report):
        safe_counter += 1
print(safe_counter)

safe_counter = 0
for line in lines:
    report = [int(x) for x in line.split()]
    is_safe = is_safe_report(report, allow_errors=True)

    if is_safe:
        safe_counter += 1


print(safe_counter)
