def part1(filename):
    rules, updates_block = [block.split('\n') for block in open(filename).read().split('\n\n')]
    print(rules)
    ans = 0
    for update in updates_block:
        pages = update.split(',')
        windowed = [pages[i:i + 2] for i in range(len(pages) - 1)]
        if all(f'{p[0]}|{p[1]}' in rules for p in windowed):
            print(f'Correct {update}')
            ans += int(pages[len(pages) // 2])
    return ans


def part2(filename):
    return 0


assert part1('day05_input_test.txt') == 143
print(f'Part 1: {part1('day05_input.txt')}')

assert part2('day05_input_test.txt') == 9
print(f'Part 2: {part2('day05_input.txt')}')