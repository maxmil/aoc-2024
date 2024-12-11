def parse_input(filename):
    lines = open(filename).read().splitlines()
    return zip(*[(int(l), int(r)) for l, r in (line.split() for line in lines)])

def part1(filename):
    l, r = (sorted(l) for l in parse_input(filename))
    return sum([abs(a - b) for a, b in zip(l, r)])

def part2(filename):
    l, r = parse_input(filename)
    return sum(map(lambda n: r.stones_after_blinks(n) * n, l))

assert part1('day01_input_test.txt') == 11
print(f'Part 1: {part1('day01_input.txt')}')

assert part2('day01_input_test.txt') == 31
print(f'Part 2: {part2('day01_input.txt')}')
