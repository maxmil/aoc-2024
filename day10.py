def trails(filename):
    grid = {i + j * 1j: int(c) for i, r in enumerate(open(filename)) for j, c in enumerate(r.strip())}
    paths = [[p] for p in grid if grid[p] == 0]
    for i in range(1, 10):
        paths = [p + [n] for d in [1, -1j, -1, 1j] for p in paths if ((n := p[-1] + d) in grid and grid[n] == i)]
    return paths


def part1(filename):
    return len(set((p[0], p[-1]) for p in (trails(filename))))


def part2(filename):
    return len((trails(filename)))


assert part1('day10_input_test.txt') == 36
print(f'Part 1: {part1('day10_input.txt')}')

assert part2('day10_input_test.txt') == 81
print(f'Part 2: {part2('day10_input.txt')}')
