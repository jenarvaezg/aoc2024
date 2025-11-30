from common.grid import Grid, Coord


with open("../inputs/day10.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

grid = Grid.from_lines(lines)


def find_path_ends(grid: Grid, current_position: Coord) -> set[Coord]:
    current_value = grid.cell_at(current_position)
    if current_value == "9":
        return {current_position}

    total_paths: set[Coord] = set()
    for neighboor, _ in grid.get_ortogonal_neighbors_with_direction(current_position):
        if ord(grid.cell_at(neighboor)) == ord(current_value) + 1:
            total_paths.update(find_path_ends(grid, neighboor))

    return total_paths


def find_all_paths(grid: Grid, current_position: Coord) -> int:
    current_value = grid.cell_at(current_position)
    if current_value == "9":
        return 1

    total_paths = 0
    for neighboor, _ in grid.get_ortogonal_neighbors_with_direction(current_position):
        if ord(grid.cell_at(neighboor)) == ord(current_value) + 1:
            total_paths += find_all_paths(grid, neighboor)

    return total_paths


total_path_ends = 0
for start in grid.coords_of("0"):
    total_path_ends += len(find_path_ends(grid, start))

print(total_path_ends)


total_paths = 0
for start in grid.coords_of("0"):
    total_paths += find_all_paths(grid, start)

print(total_paths)
