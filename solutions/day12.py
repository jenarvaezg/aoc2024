from common.grid import Grid, Coord

with open("../inputs/day12.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

grid = Grid.from_lines(lines)


def fill_region(
    grid: Grid, value: str, coord: Coord, visited: set[Coord]
) -> set[Coord]:
    if coord in visited or value != grid.cell_at(coord):
        return set()

    visited.add(coord)
    region = {coord}

    for neighboor, _ in grid.get_ortogonal_neighbors_with_direction(coord):
        if grid.cell_at(neighboor) != value or neighboor in visited:
            continue

        region.update(fill_region(grid, value, neighboor, visited))

    return region


def build_regions(grid: Grid) -> list[set[Coord]]:
    visited: set[Coord] = set()
    regions: list[set[Coord]] = []
    for y in range(grid.height):
        for x in range(grid.width):
            coord = Coord(x, y)
            if coord in visited:
                continue

            cell = grid.cell_at(coord)
            region = fill_region(grid, cell, coord, visited)
            visited.update(region)
            regions.append(region)

    return regions


def region_area(region: set[Coord]) -> int:
    return len(region)


def region_perimeter(grid: Grid, region: set[Coord]) -> int:
    perimeter = 0
    for coord in region:
        neighboors_with_directions = grid.get_ortogonal_neighbors_with_direction(coord)
        out_of_bounds = 4 - len(neighboors_with_directions)
        perimeter += out_of_bounds
        for neighboor, _ in neighboors_with_directions:
            if neighboor not in region:
                perimeter += 1

    return perimeter


def region_corners(region: set[Coord]) -> int:
    visited = set()
    corners = 0
    for coord in region:
        for dx, dy in [
            (-0.5, -0.5),
            (0.5, -0.5),
            (0.5, 0.5),
            (-0.5, 0.5),
        ]:
            new_row = coord.x + dx
            new_col = coord.y + dy

            if (new_row, new_col) in visited:
                continue

            visited.add((new_row, new_col))

            adjacent = sum(
                (Coord(int(new_row + r), int(new_col + c))) in region
                for r, c in [
                    (-0.5, -0.5),
                    (0.5, -0.5),
                    (0.5, 0.5),
                    (-0.5, 0.5),
                ]
            )

            if adjacent == 1 or adjacent == 3:
                corners += 1
            elif adjacent == 2:
                # diagonal
                pattern = [
                    c in region
                    for c in [
                        Coord(int(new_row - 0.5), int(new_col - 0.5)),
                        Coord(int(new_row + 0.5), int(new_col + 0.5)),
                    ]
                ]

                if pattern == [True, True] or pattern == [False, False]:
                    corners += 2

    return corners


regions = build_regions(grid)

total = 0
for region in regions:
    total += region_area(region) * region_perimeter(grid, region)
print(total)


total = 0
for region in regions:
    total += region_area(region) * region_corners(region)
print(total)
