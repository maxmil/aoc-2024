import re


def parse(filename):
    claws = [c.split('\n') for c in (open(filename).read().split('\n\n'))]
    return [(
        (int(a[12:14]), int(a[18:20])),
        (int(b[12:14]), int(b[18:20])),
        (int(re.split(r'X=|,', prizes)[1]), int(prizes.split('Y=')[1]))
    ) for a, b, prizes in claws]


def tokens(claw):
    a = ((claw[1][0] * claw[2][1]) - (claw[1][1] * claw[2][0])) / ((claw[1][0] * claw[0][1]) - (claw[1][1] * claw[0][0]))
    b = ((claw[0][0] * claw[2][1]) - (claw[0][1] * claw[2][0])) / ((claw[0][0] * claw[1][1]) - (claw[1][0] * claw[0][1]))
    if a.is_integer() and b.is_integer(): return int(a * 3 + b)
    else: return 0


def part1(filename):
    return sum(tokens(claw) for claw in (parse(filename)))


def part2(filename):
    claws = [(*claw[:2], [n + 10 ** 13 for n in claw[2]]) for claw in (parse(filename))]
    return sum(tokens(claw) for claw in claws)


assert part1('day13_input_test.txt') == 480
print(f'Part 1: {part1('day13_input.txt')}')
print(f'Part 2: {part2('day13_input.txt')}')
