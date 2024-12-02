def parse_input(filename):
    lines = open(filename).read().splitlines()
    return [*map(lambda l: [*map(int, l.split())], lines)]

def is_safe(levels):
    if len(levels) == 1:
        return True
    for i in range(len(levels) - 1):
        dist = levels[i + 1] - levels[i]
        if abs(dist) < 1 or abs(dist) > 3 or dist / (levels[1] - levels[0]) < 0:
            return False
    return True

def part1(filename):
    return len([r for r in parse_input(filename) if is_safe(r)])

def part2(filename): return sum(
    any(is_safe(record[:i] + record[i + 1:]) for i in range(len(record))) for record in parse_input(filename))

assert part1('day02_input_test.txt') == 2
print(f'Part 1: {part1('day02_input.txt')}')

assert part2('day02_input_test.txt') == 4
print(f'Part 2: {part2('day02_input.txt')}')