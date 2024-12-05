def sort(rules, pages):
    if len(pages) <= 1:
        return pages
    else:
        pivot = pages[len(pages) // 2]
        less = [p for p in pages if p != pivot and (p, pivot) in rules]
        greater = [p for p in pages if p != pivot and not (p, pivot) in rules]
        return sort(rules, less) + [pivot] + sort(rules, greater)


def parse(filename):
    rules_block, updates_block = open(filename).read().split('\n\n')
    rules = [(k, v) for r in rules_block.split('\n') for k, v in [r.split('|')]]
    updates = [u.split(',') for u in updates_block.split('\n')]
    return rules, updates


def part1(filename):
    rules, updates = parse(filename)
    return sum(int(pages[len(pages) // 2]) for pages in updates if sort(rules, pages) == pages)


def part2(filename):
    rules, updates = parse(filename)
    return sum(int(sorted_pages[len(sorted_pages) // 2]) for pages in updates if (sorted_pages := sort(rules, pages)) != pages)


assert part1('day05_input_test.txt') == 143
print(f'Part 1: {part1('day05_input.txt')}')

assert part2('day05_input_test.txt') == 123
print(f'Part 2: {part2('day05_input.txt')}')
