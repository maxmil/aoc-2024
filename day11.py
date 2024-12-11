def count(stones, max_blinks, cache, blinks):
    if blinks == max_blinks:
        return len(stones)
    key = (tuple(stones), blinks)
    if key in cache:
        return cache[key]
    ans = 0
    for stone in stones:
        if stone == 0:
            ans += count([1], max_blinks, cache, blinks + 1)
        elif len(str(stone)) % 2 == 0:
            divided = list(map(int, (str(stone)[:len(str(stone)) // 2], str(stone)[len(str(stone)) // 2:])))
            ans += count(divided, max_blinks, cache, blinks + 1)
        else:
            ans += count([stone * 2024], max_blinks, cache, blinks + 1)
    cache[key] = ans
    return ans


def part1(filename):
    return count(list(map(int, open(filename).read().split())), 25, {}, 0)


def part2(filename):
    return count(list(map(int, open(filename).read().split())), 75, {}, 0)


assert part1('day11_input_test.txt') == 55312
print(f'Part 1: {part1('day11_input.txt')}')

print(f'Part 2: {part2('day11_input.txt')}')
