def parse_input(filename):
    return [[int(x) for x in l.split()] for l in open(filename).read().splitlines()]

def is_safe(levels):
    windowed = [levels[i:i + 2] for i in range(len(levels) - 1)]
    distances = [l[min(1, len(windowed) - 1)] - l[0] for l in windowed]
    return all(0 < d < 4 for d in distances) or all(-4 < d < 0 for d in distances)

def part1(filename):
    return len([r for r in parse_input(filename) if is_safe(r)])

def part2(filename):
    return sum(any(is_safe(record[:i] + record[i + 1:]) for i in range(len(record))) for record in parse_input(filename))

assert part1('day02_input_test.txt') == 2
print(f'Part 1: {part1('day02_input.txt')}')

assert part2('day02_input_test.txt') == 4
print(f'Part 2: {part2('day02_input.txt')}')
