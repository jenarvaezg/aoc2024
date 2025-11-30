from common.grid import Grid, Coord, Direction

with open("../inputs/day06.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

grid = Grid.from_lines(lines)


rotation = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}


def explore(grid: Grid) -> set[Coord]:
    direction = Direction.UP
    position = grid.position_of("^")
    visited = set()

    while True:
        if (position, direction) in visited:
            raise ValueError("Infinite loop")

        visited.add((position, direction))
        try:
            position_ahead = position + direction.delta
            if grid.cell_at(position_ahead) == "#":
                direction = rotation[direction]
            else:
                position = position + direction.delta
        except KeyError:
            break

    return {pos for pos, _ in visited}


print(len(explore(grid)))


def part_2_brute_force():
    # Brute force is not that slow actually
    infinite_loops = 0
    for y in range(grid.height):
        print(y)
        for x in range(grid.width):
            if grid.position_of("^") == Coord(x, y):
                continue

            current_grid = Grid.from_lines(lines)
            current_grid.set_cell_at(Coord(x, y), "#")
            try:
                explore(current_grid)
            except ValueError:
                infinite_loops += 1


def part_2_smart():
    positions_to_check = explore(grid)

    infinite_loops = 0
    for position in positions_to_check:
        # Ignore starting position
        if grid.position_of("^") == position:
            continue

        current_grid = Grid.from_lines(lines)
        current_grid.set_cell_at(position, "#")

        try:
            explore(current_grid)
        except ValueError:
            infinite_loops += 1

    return infinite_loops


print(part_2_smart())
