directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def move(pos, direction):
    return tuple(a + b for a, b in zip(pos, directions[direction]))

def char_at(pos, grid):
    if in_bounds(pos, grid):
        return grid[pos[1]][pos[0]]

def in_bounds(pos, grid):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)

def part1(filename):
    grid = open(filename).read().split('\n')
    direction = 0
    pos = next(((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == '^'))
    visited = set()
    while in_bounds(pos, grid):
        visited.add(pos)
        print(move(pos, direction))
        # print(char_at(move(pos, direction), grid))
        while char_at(move(pos, direction), grid) == '#':
            direction = (direction + 1) % 4
            print(f'Turn {direction}')
        pos = move(pos, direction)
        # print()
    print(len(visited))
    return len(visited)


def part2(filename):
   return 0


assert part1('day06_input_test.txt') == 41
print(f'Part 1: {part1('day06_input.txt')}')

assert part2('day06_input_test.txt') == 123
print(f'Part 2: {part2('day06_input.txt')}')