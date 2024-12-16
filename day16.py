from heapq import heappush, heappop
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def plus(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def times(self, n):
        return Point(self.x * n, self.y * n)


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


def parse(filename):
    maze = {Point(x, y): c for y, r in enumerate(open(filename).read().split('\n')) for x, c in enumerate(r)}
    start = next((p for p, c in maze.items() if c == 'S'))
    end = next((p for p, c in maze.items() if c == 'E'))
    return maze, start, end


def part1(filename):
    maze, start, end = parse(filename)

    queue = []
    scores = {Position(p, d): (float('inf'), []) for p in maze for d in DIRECTIONS}
    start_position = Position(start, Point(1, 0))
    heappush(queue, (0, start_position, [start_position]))
    scores[start_position] = (0, [start_position])

    visited = set()
    while queue:
        curr_score, curr_pos, curr_path = heappop(queue)
        if curr_pos in visited:
            continue
        visited.add(curr_pos)

        nxt = []
        curr_dir = curr_pos.direction
        if maze[curr_pos.advance(1).point] != '#':
            nxt += [(1, curr_pos.advance(1))]
        nxt += [(1000, curr_pos.turn(d)) for d in DIRECTIONS
                if abs(d.x) != abs(curr_dir.x) and abs(d.y) != abs(curr_dir.y) and maze[curr_pos.move(d).point] != '#']

        for next_score, next_pos in nxt:
            score = curr_score + next_score
            path = curr_path + [next_pos]

            if score < scores[next_pos][0]:
                scores[next_pos] = (score, path)
                heappush(queue, (score, next_pos, path))

    min_score, min_path = min((score, path) for p, (score, path) in scores.items() if p.point == end)
    print(min_score)
    # for p in min_path:
    #     print(f'({p.point.x},{p.point.y})')
    return min_score


def part2(filename):
    return 0


assert part1('day16_input_test.txt') == 7036
assert part1('day16_input_test_2.txt') == 11048
print(f'Part 1: {part1('day16_input.txt')}')

assert part2('day16_input_test.txt') == -1
print(f'Part 2: {part2('day16_input.txt')}')
