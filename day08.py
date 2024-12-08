def in_bounds(p, grid):
    return 0 <= p.real < len(grid[0]) and 0 <= p.imag < len(grid)


def find_antinodes(grid, max_dist=float('inf'), exclude_source=False):
    antennas = {}
    antinodes = set()
    for y, row in enumerate(grid):
        for x, freq in enumerate(row):
            if freq != '.':
                antenna = x + y * 1j
                freq = antennas.setdefault(freq, [])
                for other in freq:
                    wavelength = other - antenna
                    i = 1 if exclude_source else 0
                    while i <= max_dist:
                        nodes = [n for n in [antenna - wavelength * i, other + wavelength * i] if in_bounds(n, grid)]
                        if len(nodes):
                            antinodes.update(nodes)
                            i += 1
                        else:
                            break
                freq.append(antenna)
    return antinodes


def part1(filename):
    return len(find_antinodes(open(filename).read().split(), 1, True))


def part2(filename):
    return len(find_antinodes(open(filename).read().split()))


assert part1('day08_input_test.txt') == 14
print(f'Part 1: {part1('day08_input.txt')}')

assert part2('day08_input_test.txt') == 34
print(f'Part 2: {part2('day08_input.txt')}')
