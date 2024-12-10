
dirs = [1, -1j, -1, 1j]

def part1(filename):
    grid = {i + j * 1j: int(c) for i, r in enumerate(open(filename)) for j, c in enumerate(r.strip())}
    paths = [[p] for p in grid if grid[p] == 0]
    for i in range(1, 10):
        paths = [p + [p[-1] + d] for d in dirs for p in paths if p[-1] + d in grid and grid[p[-1] + d] == i]
    ans = len(set((p[0], p[-1]) for p in paths))
    return ans

def part2(filename):
    return 0

assert part1('day10_input_test.txt') == 36
assert part1('day10_input.txt') == 582
print(f'Part 1: {part1('day10_input.txt')}')

assert part2('day10_input_test.txt') == 2858
print(f'Part 2: {part2('day10_input.txt')}')