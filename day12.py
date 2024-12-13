def get_corners(point, grid, plant):
    corners = set()
    diagonals = [1 - 1j, 1 + 1j, -1 - 1j, -1 + 1j]
    for d in diagonals:
        if grid.get(point + d) != plant and grid.get(point + d.real) == plant and grid.get(point + d.imag * 1j) == plant:
            corners.add(point + d)
        if grid.get(point + d.real) != plant and grid.get(point + d.imag * 1j) != plant:
            corners.add(point + d)
    return list(corners)


def discover_region(point, grid, seen):
    plant, region, perimeter, corners, to_visit = grid[point], set(), [], [], [point]
    while to_visit:
        p = to_visit.pop()
        if p in grid and grid[p] == plant:
            if p not in seen:
                seen.add(p)
                region.add(p)
                corners += get_corners(p, grid, plant)
                to_visit = to_visit + [p + d for d in [1, 1j, -1, -1j]]
        else:
            perimeter.append(p)
    return region, perimeter, corners


def find_regions(filename):
    grid = {x + y * 1j: c for y, r in enumerate(open(filename)) for x, c in enumerate(r.strip())}
    regions, seen = [], set()
    for p in grid:
        if not p in seen:
            regions.append(discover_region(p, grid, seen))
    return regions


def part1(filename):
    return sum(len(plants) * len(perimeter) for (plants, perimeter, _) in find_regions(filename))


def part2(filename):
    return sum(len(plants) * len(corners) for (plants, _, corners) in find_regions(filename))


assert part1('day12_input_test.txt') == 1930
print(f'Part 1: {part1('day12_input.txt')}')

assert part2('day12_input_test.txt') == 1206
print(f'Part 2: {part2('day12_input.txt')}')
