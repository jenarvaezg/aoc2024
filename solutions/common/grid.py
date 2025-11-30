from dataclasses import dataclass
from enum import Enum, auto
import typing


class Direction(Enum):
    UP = auto()
    UP_RIGHT = auto()
    RIGHT = auto()
    DOWN_RIGHT = auto()
    DOWN = auto()
    DOWN_LEFT = auto()
    LEFT = auto()
    UP_LEFT = auto()

    @property
    def delta(self):
        match self:
            case Direction.UP:
                return Coord(0, -1)
            case Direction.DOWN:
                return Coord(0, 1)
            case Direction.LEFT:
                return Coord(-1, 0)
            case Direction.RIGHT:
                return Coord(1, 0)
            case Direction.UP_RIGHT:
                return Coord(1, -1)
            case Direction.UP_LEFT:
                return Coord(-1, -1)
            case Direction.DOWN_RIGHT:
                return Coord(1, 1)
            case Direction.DOWN_LEFT:
                return Coord(-1, 1)

    @classmethod
    def orthogonal_directions(cls):
        return [cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT]

    @classmethod
    def all_directions(cls):
        return [
            cls.UP,
            cls.UP_RIGHT,
            cls.RIGHT,
            cls.DOWN_RIGHT,
            cls.DOWN,
            cls.DOWN_LEFT,
            cls.LEFT,
            cls.UP_LEFT,
        ]


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other: typing.Self):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other: typing.Self):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, amount: int):
        return Coord(self.x * amount, self.y * amount)


@dataclass
class Grid:
    width: int
    height: int
    cells: list[str]

    @classmethod
    def from_lines(cls, lines: list[str]) -> "Grid":
        width = len(lines[0])
        height = len(lines)
        cells = []
        for line in lines:
            for cell in line:
                cells.append(cell)

        return cls(width, height, cells)

    def __str__(self) -> str:
        s = ""
        for i, c in enumerate(self.cells):
            s += c
            if (i + 1) % self.width == 0:
                s += "\n"

        return s

    def set_cell_at(self, coord: Coord, value: str):
        self.cells[coord.y * self.width + coord.x] = value

    def cell_at(self, coord: Coord) -> str:
        if (
            coord.x < 0
            or coord.y < 0
            or coord.x >= self.width
            or coord.y >= self.height
        ):
            raise KeyError
        return self.cells[coord.y * self.width + coord.x]

    def get_neighbors_positions(self, coord: Coord) -> list[Coord]:
        neighbor_deltas = (
            (-1, -1),  # TOP LEFT
            (0, -1),  # TOP
            (1, -1),  # TOP RIGHT
            (-1, 0),  # LEFT
            (1, 0),  # RIGHT
            (-1, 1),  # BOTTOM LEFT
            (0, 1),  # BOTTOM
            (1, 1),  # BOTTOM RIGHT
        )
        positions = []
        for xd, yd in neighbor_deltas:
            xtarget, ytarget = coord.x + xd, coord.y + yd
            if (
                xtarget < 0
                or xtarget >= self.width
                or ytarget < 0
                or ytarget >= self.height
            ):
                continue
            positions.append(Coord(xtarget, ytarget))

        return positions

    def get_ortogonal_neighbors_with_direction(
        self,
        coord: Coord,
    ) -> list[tuple[Coord, Direction]]:
        positions = []
        for direction in Direction.orthogonal_directions():
            target_coord = coord + direction.delta
            if (
                target_coord.x < 0
                or target_coord.x >= self.width
                or target_coord.y < 0
                or target_coord.y >= self.height
            ):
                continue
            positions.append((target_coord, direction))

        return positions

    def get_neighbors(self, coord: Coord) -> list[str]:
        neighbors = []
        for cell in self.get_neighbors_positions(coord):
            if neighbor := self.cell_at(cell):
                neighbors.append(neighbor)

        return neighbors

    def position_of(self, value: str, offset) -> Coord:
        index = self.cells.index(value)
        x = index % self.height
        y = index // self.height
        return Coord(x, y)

    def coords_of(self, value: str) -> list[Coord]:
        return [
            Coord(i % self.height, i // self.height)
            for i, val in enumerate(self.cells)
            if val == value
        ]

    def add_column(self, position: int, value: str) -> None:
        for i in range(self.height):
            self.cells.insert((position + i) + (i * self.width), value)
            i += 1
        self.width += 1

    def add_row(self, position: int, value: str) -> None:
        self.cells = (
            self.cells[: self.width * position]
            + [value] * self.width
            + self.cells[self.width * position :]
        )
        self.height += 1
