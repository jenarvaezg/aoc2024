from collections import Counter
from common.grid import Grid, Coord

with open("../inputs/day04.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]


grid = Grid.from_lines(lines)


total = 0
directions: list[tuple[Coord, ...]] = [
    (Coord(1, 0), Coord(2, 0), Coord(3, 0)),  # RIGHT
    (Coord(-1, 0), Coord(-2, 0), Coord(-3, 0)),  # LEFT
    (Coord(0, 1), Coord(0, 2), Coord(0, 3)),  # DOWN
    (Coord(0, -1), Coord(0, -2), Coord(0, -3)),  # UP
    (Coord(1, 1), Coord(2, 2), Coord(3, 3)),  # DOWN RIGHT
    (Coord(1, -1), Coord(2, -2), Coord(3, -3)),  # UP RIGHT
    (Coord(-1, 1), Coord(-2, 2), Coord(-3, 3)),  # DOWN LEFT
    (Coord(-1, -1), Coord(-2, -2), Coord(-3, -3)),  # UP LEFT
]
for y in range(grid.height):
    for x in range(grid.width):
        current_coord = Coord(x, y)
        if grid.cell_at(current_coord) == "X":
            for direction in directions:
                try:
                    if (
                        grid.cell_at(current_coord + direction[0]) == "M"
                        and grid.cell_at(current_coord + direction[1]) == "A"
                        and grid.cell_at(current_coord + direction[2]) == "S"
                    ):
                        total += 1
                except KeyError:
                    pass

print(total)


total = 0
for y in range(grid.height - 2):
    for x in range(grid.width - 2):
        if grid.cell_at(Coord(x + 1, y + 1)) == "A":
            corners = [
                Coord(x, y),
                Coord(x + 2, y),
                Coord(x, y + 2),
                Coord(x + 2, y + 2),
            ]
            corners_value_ctr = Counter(grid.cell_at(corner) for corner in corners)
            if (
                corners_value_ctr["M"] == 2
                and corners_value_ctr["S"] == 2
                and grid.cell_at(corners[0]) != grid.cell_at(corners[3])
            ):
                total += 1

print(total)
