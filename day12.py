def discover_region(point, grid, seen):
    plant = grid[point]
    seen.add(point)
    region = {point}
    perimeter = []
    to_visit = [point + d for d in [1, 1j, -1, -1j]]
    while to_visit:
        p = to_visit.pop()
        if p in grid and grid[p] == plant:
            if p not in seen:
                seen.add(p)
                region.add(p)
                to_visit = to_visit + [p + d for d in [1, 1j, -1, -1j]]
        else:
            perimeter.append(p)
    return region, perimeter

def part1(filename):
    grid = {x + y * 1j: c for y, r in enumerate(open(filename)) for x, c in enumerate(r.strip())}
    regions = []
    seen = set()
    for p in grid:
        if not p in seen:
            regions.append(discover_region(p, grid, seen))
    ans = sum(len(plants) * len(perimeter) for (plants, perimeter) in regions)
    print(regions)
    print(ans)
    return ans


def part2(filename):
    return 0


assert part1('day12_input_test.txt') == 1930
print(f'Part 1: {part1('day12_input.txt')}')

assert part2('day12_input_test.txt') == 55312
print(f'Part 2: {part2('day12_input.txt')}')
