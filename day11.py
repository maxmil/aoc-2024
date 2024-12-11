def count_stones(stone, blinks, max_blinks, cache):
    if blinks == max_blinks:
        return 1
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]
    cache[(stone, blinks)] = (
        count_stones(1, blinks + 1, max_blinks, cache) if stone == 0 else
        sum(count_stones(s, blinks + 1, max_blinks, cache) for s in map(int, (str(stone)[:l // 2], str(stone)[l // 2:]))) if (l := len(str(stone))) % 2 == 0 else
        count_stones(stone * 2024, blinks + 1, max_blinks, cache)
    )
    return cache[(stone, blinks)]


def solve(filename, blinks):
    return sum(count_stones(s, 0, blinks, {}) for s in list(map(int, open(filename).read().split())))


def part1(filename):
    return solve(filename, 25)


def part2(filename):
    return solve(filename, 75)


assert part1('day11_input_test.txt') == 55312
print(f'Part 1: {part1('day11_input.txt')}')

print(f'Part 2: {part2('day11_input.txt')}')
