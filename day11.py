from functools import cache


@cache
def stones(stone, blinks):
    if blinks == 0: return 1
    if stone == 0: return stones(1, blinks - 1)
    s = str(stone)
    if len(s) % 2 == 0:
        return sum(stones(s, blinks - 1) for s in map(int, (s[:len(s) // 2], s[len(s) // 2:])))
    return stones(stone * 2024, blinks - 1)


def solve(filename, blinks):
    return sum(stones(s, blinks) for s in map(int, open(filename).read().split()))


assert solve('day11_input_test.txt', 25) == 55312
print(f'Part 1: {solve('day11_input.txt', 25)}')
print(f'Part 2: {solve('day11_input.txt', 75)}')
