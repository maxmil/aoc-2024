def count(stones, blinks=0):
    if blinks == 25:
        return len(stones)
    ans = 0
    for stone in stones:
        if stone == 0:
            ans += count([1], blinks + 1)
        elif len(str(stone)) % 2 == 0:
            l = len(str(stone))
            stones = [int(str(stone)[:l // 2]), int(str(stone)[l // 2:])]
            ans += count(stones, blinks + 1)
        else:
            ans += count([stone * 2024], blinks + 1)
    return ans


def part1(filename):
    return count(list(map(int, open(filename).read().split())))


def part2(filename):
    return 0


assert part1('day11_input_test.txt') == 55312
print(f'Part 1: {part1('day11_input.txt')}')

assert part2('day11_input_test.txt') == 81
print(f'Part 2: {part2('day11_input.txt')}')
