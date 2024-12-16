from heapq import heappush, heappop
from utils.grid import Point, Position, DIRECTIONS


def parse(filename):
    return {Point(x, y): c for y, r in enumerate(open(filename).read().split('\n')) for x, c in enumerate(r)}


def shortest_paths(maze):
    queue = []
    visited = set()
    start = Position(next((p for p, c in maze.items() if c == 'S')), Point(1, 0))
    paths = {Position(p, d): (float('inf'), set()) for p in maze for d in DIRECTIONS if maze[p] != '#'}
    paths[start] = (0, {start.point})
    heappush(queue, (0, start, {start.point}))
    while queue:
        score, position, points = heappop(queue)
        if position in visited: continue
        visited.add(position)

        neighbours = []
        direction = position.direction
        if maze[position.advance(1).point] != '#': neighbours += [(1, position.advance(1))]
        neighbours += [(1000, position.turn(d)) for d in DIRECTIONS
                       if abs(d.x) != abs(direction.x) and abs(d.y) != abs(direction.y)
                       and maze[position.move(d).point] != '#']

        for neighbour_score, neighbour_position in neighbours:
            new_score = score + neighbour_score
            new_points = points | {neighbour_position.point}
            if new_score == paths[neighbour_position][0]:
                paths[neighbour_position][1].update(new_points)
            if new_score < paths[neighbour_position][0]:
                paths[neighbour_position] = (new_score, new_points)
                heappush(queue, (new_score, neighbour_position, new_points))
    return paths


def part1(filename):
    maze = parse(filename)
    return min(score for p, (score, _) in shortest_paths(maze).items() if maze[p.point] == 'E')


def part2(filename):
    maze = parse(filename)
    _, points = min((score, points) for p, (score, points) in shortest_paths(maze).items() if maze[p.point] == 'E')
    return len(points)


assert part1('day16_input_test.txt') == 7036
assert part1('day16_input_test_2.txt') == 11048
assert part1('day16_input.txt') == 88416
print(f'Part 1: {part1('day16_input.txt')}')

assert part2('day16_input_test.txt') == 45
assert part2('day16_input_test_2.txt') == 64
assert part2('day16_input.txt') == 442
print(f'Part 2: {part2('day16_input.txt')}')
