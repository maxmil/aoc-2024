from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def plus(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def times(self, n):
        return Point(self.x * n, self.y * n)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'


@dataclass(frozen=True, order=True)
class Position:
    point: Point
    direction: Point

    def move(self, point):
        return Position(self.point.plus(point), self.direction)

    def advance(self, steps):
        return self.move(self.direction.times(steps))

    def turn(self, direction):
        return Position(self.point, direction)


DIRECTIONS = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]
