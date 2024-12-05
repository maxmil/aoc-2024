def part1_1(filename):
    rules, updates_block = [block.split('\n') for block in open(filename).read().split('\n\n')]
    ans = 0
    for update in updates_block:
        pages = update.split(',')
        windowed = [pages[i:i + 2] for i in range(len(pages) - 1)]
        if all(f'{p[0]}|{p[1]}' in rules for p in windowed):
            print(f'Correct {update}')
            ans += int(pages[len(pages) // 2])
    return ans

def part1(filename):
    rules, updates_block = [block.split('\n') for block in open(filename).read().split('\n\n')]
    ans = 0
    for update in updates_block:
        pages = update.split(',')
        print(f'{pages} {quick_sort(rules, pages)}')
        if quick_sort(rules, pages) == pages:
            print(f'Correct {update}')
            ans += int(pages[len(pages) // 2])
    print(ans)
    return ans

def compare(rules, page1, page2):
    if page1 == page2:
        return 0
    elif f'{page1}|{page2}' in rules:
        return 1
    else:
        return -1

def quick_sort(rules, pages):
    # print(pages)
    if len(pages) <= 1:
        return pages
    else:
        pivot = pages[len(pages) // 2]
        less = [p for p in pages if compare(rules, p, pivot) == 1]
        equal = [p for p in pages if compare(rules, p, pivot) == 0]
        greater = [p for p in pages if compare(rules, p, pivot) == -1]
        # print(f'{pivot} {less} {greater}')
        return quick_sort(rules, less) + [pivot] + quick_sort(rules, greater)

def part2(filename):
    rules, updates_block = [block.split('\n') for block in open(filename).read().split('\n\n')]
    ans = 0
    for update in updates_block:
        pages = update.split(',')
        sorted_pages = quick_sort(rules, pages)
        if sorted_pages != pages:
            ans += int(sorted_pages[len(sorted_pages) // 2])
    print(ans)
    return ans


assert part1('day05_input_test.txt') == 143
print(f'Part 1: {part1('day05_input.txt')}')

assert part2('day05_input_test.txt') == 123
print(f'Part 2: {part2('day05_input.txt')}')