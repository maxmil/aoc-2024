def read_lines(filename):
    return open(filename).read().splitlines()

def read_input(filename):
    list1, list2 = zip(*[(int(note1), int(note2)) for note1, note2 in (line.split() for line in read_lines(filename))])
    return list(list1), list(list2)

def part1(filename):
    list1, list2 = (sorted(l) for l in read_input(filename))
    distances = [abs(a - b) for a, b in zip(list1, list2)]
    return sum(distances)

def part2(filename):
    list1, list2 = read_input(filename)
    return sum(map(lambda n: list2.count(n) * n, list1))

assert part1('day01_input_test.txt') == 11
print(f'Part1 {part1('day01_input.txt')}')

assert part2('day01_input_test.txt') == 31
print(f'Part2 {part2('day01_input.txt')}')
