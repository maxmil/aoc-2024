def plant_at(p, grid):
    return grid[p] if p in grid else None


def get_corners(point, grid, plant):
    # if plant == 'C': print(plant, point)
    corners = set()
    diagonals = [1 - 1j, 1 + 1j, -1 - 1j, -1 + 1j]

    # inner corners
    for diagonal in diagonals:
        if plant_at(point + diagonal, grid) != plant and plant_at(point + diagonal.real, grid) == plant and plant_at(point + diagonal.imag * 1j, grid) == plant:
            # if plant == 'C': print(f"inner {point} {diagonal}")
            corners.add(point + diagonal)

    # outer corners
    for diagonal in diagonals:
        if plant_at(point + diagonal.real, grid) != plant and plant_at(point + diagonal.imag * 1j, grid) != plant:
            # if plant == 'C': print(f"outer {point} {diagonal}")
            corners.add(point + diagonal)

    # if plant == 'C': print(corners)
    return list(corners)


def discover_region(point, grid, seen):
    plant = grid[point]
    seen.add(point)
    region = {point}
    perimeter = []
    corners = get_corners(point, grid, plant)
    to_visit = [point + d for d in [1, 1j, -1, -1j]]
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
    # print(corners)
    # exit()
    return region, perimeter, corners


def find_regions(filename):
    grid = {x + y * 1j: c for y, r in enumerate(open(filename)) for x, c in enumerate(r.strip())}
    regions = []
    seen = set()
    for p in grid:
        if not p in seen:
            regions.append(discover_region(p, grid, seen))
    return regions


def part1(filename):
    regions = find_regions(filename)
    return sum(len(plants) * len(perimeter) for (plants, perimeter, _) in regions)


def part2(filename):
    grid = {x + y * 1j: c for y, r in enumerate(open(filename)) for x, c in enumerate(r.strip())}
    regions = find_regions(filename)
    for plants, _, corners in regions:
        print(grid[list(plants)[0]], len(plants), len(corners))
    ans = sum(len(plants) * len(corners) for (plants, _, corners) in regions)
    print(ans)
    return ans


# assert part1('day12_input_test.txt') == 1930
# print(f'Part 1: {part1('day12_input.txt')}')
# 1437300

assert part2('day12_input_test.txt') == 1206
print(f'Part 2: {part2('day12_input.txt')}')
# 849332
