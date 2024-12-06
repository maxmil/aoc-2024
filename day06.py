from operator import contains
import copy

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def move(pos, direction):
    return tuple(a + b for a, b in zip(pos, directions[direction]))


def char_at(pos, grid):
    if in_bounds(pos, grid):

        try:
            return grid[pos[1]][pos[0]]
        except Exception as e:
            print(f"Error: {e}")
            print(f"Position: {pos}")
            print(f"Grid: {grid}")
            print(grid[pos[1]])
            print(pos[0])
            exit(1)


def in_bounds(pos, grid):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)


def step(direction, pos, grid):
    while char_at(move(pos, direction), grid) in {'#', 'O'}:
        direction = (direction + 1) % 4
    pos = move(pos, direction)
    return direction, pos


def path(direction, pos, grid):
    visited = set()
    while char_at(pos, grid):
        visited.add(pos)
        direction, pos = step(direction, pos, grid)
    return visited


def is_loop(direction, pos, grid):
    visited = set()
    while char_at(pos, grid):
        visited.add((pos, direction))
        direction, pos = step(direction, pos, grid)
        if contains(visited, (pos, direction)):
            return True
    return False


def put_obstacle(grid, pos):
    x, y = pos[0], pos[1]
    g = copy.deepcopy(grid)
    g[y] = g[y][:x] + 'O' + g[y][x + 1:]
    return g


def part1(filename):
    grid = open(filename).read().split('\n')
    direction = 0
    start = next(((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == '^'))
    return len(path(direction, start, grid))


def part2(filename):
    grid = open(filename).read().split('\n')
    direction = 0
    start = next(((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == '^'))
    pos = start
    loops = set()
    visited = set()
    while char_at(pos, grid):
        visited.add(pos)
        nxt_dir, nxt_pos = step(direction, pos, grid)
        if in_bounds(nxt_pos, grid) and nxt_pos != start and nxt_pos not in visited:
            obstructed = put_obstacle(grid, nxt_pos)
            if is_loop(0, start, obstructed):
                loops.add(nxt_pos)
        direction, pos = nxt_dir, nxt_pos
    return len(loops)


assert part1('day06_input_test.txt') == 41
assert part1('day06_input.txt') == 4515
print(f'Part 1: {part1('day06_input.txt')}')

assert part2('day06_input_test.txt') == 6
# assert part2('day06_input.txt') == 1309
print(f'Part 2: {part2('day06_input.txt')}')
