def sort(rules, pages):
    if len(pages) <= 1:
        return pages
    else:
        pivot = pages[len(pages) // 2]
        less = [p for p in pages if p != pivot and f'{p}|{pivot}' in rules]
        greater = [p for p in pages if p != pivot and not f'{p}|{pivot}' in rules]
        return sort(rules, less) + [pivot] + sort(rules, greater)

def part1(filename):
    rules, updates_block = [block.split('\n') for block in open(filename).read().split('\n\n')]
    ans = 0
    for update in updates_block:
        pages = update.split(',')
        if sort(rules, pages) == pages:
            ans += int(pages[len(pages) // 2])
    return ans

def part2(filename):
    rules, updates_block = [block.split('\n') for block in open(filename).read().split('\n\n')]
    ans = 0
    for update in updates_block:
        pages = update.split(',')
        sorted_pages = sort(rules, pages)
        if sorted_pages != pages:
            ans += int(sorted_pages[len(sorted_pages) // 2])
    return ans


assert part1('day05_input_test.txt') == 143
print(f'Part 1: {part1('day05_input.txt')}')

assert part2('day05_input_test.txt') == 123
print(f'Part 2: {part2('day05_input.txt')}')