def transpose(grid):
    return [[grid[y][x] for y in range(len(grid[x]))] for x in range(len(grid))]

def diagonal(grid, right):
    h = len(grid)
    w = len(grid[0])
    d = [[] for _ in range(w + h)]
    for y in range(h):
        for x in range(w):
            if right:
                d[x - y + h].append(grid[y][x])
            else:
                d[x + y].append(grid[y][x])
    return d

def count(grid):
    return sum(''.join(row).count(s) for s in ['XMAS', 'SAMX'] for row in grid)

def part1(filename):
    grid = open(filename).read().splitlines()
    return sum(count(g) for g in [grid, transpose(grid), diagonal(grid, False), diagonal(grid, True)])

def part2(filename):
    return 0

assert part1('day04_input_test.txt') == 18
print(f'Part 1: {part1('day04_input.txt')}')

# assert part2('day04_input_test.txt') == 9
# print(f'Part 2: {part2('day04_input.txt')}')
