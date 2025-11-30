from common.grid import Coord, Direction
from collections import defaultdict
import itertools

with open("../inputs/day08.txt") as f:
    lines = [x.strip() for x in f.read().splitlines()]

DIMENSIONS = len(lines)


antennas = defaultdict(list)
for y in range(DIMENSIONS):
    line = lines[y]
    for x in range(DIMENSIONS):
        if line[x] != "." and line[x] != "#":
            antennas[line[x]].append(Coord(x, y))


def is_out_of_bounds(coord: Coord):
    return coord.x < 0 or coord.y < 0 or coord.x >= DIMENSIONS or coord.y >= DIMENSIONS


def calculate_antinodes(antennas: list[Coord]) -> list[Coord]:
    antinodes: list[Coord] = []
    for one, other in itertools.combinations(antennas, 2):
        one_diff = one - other
        other_diff = other - one
        if not is_out_of_bounds(one + one_diff):
            antinodes.append(one + one_diff)
        if not is_out_of_bounds(other + other_diff):
            antinodes.append(other + other_diff)

    return antinodes


def calculate_antinodes_with_resonance(antennas: list[Coord]) -> list[Coord]:
    antinodes: list[Coord] = []
    for one, other in itertools.combinations(antennas, 2):
        antinodes.append(one)
        antinodes.append(other)

        one_diff = one - other
        other_diff = other - one

        resonance_count = 1
        while not is_out_of_bounds(one + one_diff * resonance_count):
            antinodes.append(one + one_diff * resonance_count)
            resonance_count += 1

        resonance_count = 1
        while not is_out_of_bounds(other + other_diff * resonance_count):
            antinodes.append(other + other_diff * resonance_count)
            resonance_count += 1

    return antinodes


antinodes = set()
for antennas_for_name in antennas.values():
    if len(antennas_for_name) <= 1:
        continue
    antinodes.update(calculate_antinodes(antennas_for_name))

print(len(antinodes))


antinodes_with_ressonance = set()
for antennas_for_name in antennas.values():
    if len(antennas_for_name) <= 1:
        continue
    antinodes_with_ressonance.update(
        calculate_antinodes_with_resonance(antennas_for_name)
    )

print(antinodes_with_ressonance)
print(len(antinodes_with_ressonance))
