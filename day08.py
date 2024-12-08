def in_bounds(p, grid):
    return 0 <=  p.real < len(grid[0]) and 0 <= p.imag < len(grid)

def part1(filename):
    grid = open(filename).read().split()
    antennas = {}
    resonance = set()
    for y, row in enumerate(grid):
        for x, freq in enumerate(row):
          if freq != '.':
              p1 = x + y * 1j
              antennas_freq = antennas.setdefault(freq, [])
              for p2 in antennas_freq:
                r1 = 2 * p2 - p1
                r2 = 2 * p1 - p2
                if in_bounds(r1, grid):
                    resonance.add(r1)
                if in_bounds(r2, grid):
                    resonance.add(r2)
              antennas_freq.append(p1)
    ans = len(resonance)
    return ans


def part2(filename):
    grid = open(filename).read().split()
    antennas = {}
    resonance = set()
    for y, row in enumerate(grid):
        for x, freq in enumerate(row):
          if freq != '.' and freq  != '#':
              p1 = x + y * 1j
              antennas_freq = antennas.setdefault(freq, [])
              for p2 in antennas_freq:
                  dist = p2 - p1
                  i = 0
                  while in_bounds(p2 + i * dist, grid):
                      resonance.add(p2 + i * dist)
                      i += 1
                  i = 0
                  while in_bounds(p1 - i * dist, grid):
                      resonance.add(p1 - i * dist)
                      i += 1
              antennas_freq.append(p1)
    ans = len(resonance)
    return ans


assert part1('day08_input_test.txt') == 14
print(f'Part 1: {part1('day08_input.txt')}')

assert part2('day08_input_test.txt') == 34
print(f'Part 2: {part2('day08_input.txt')}')
