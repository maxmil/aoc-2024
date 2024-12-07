plus = lambda a, b: a + b
multiply = lambda a, b: a * b
concat = lambda a, b: int(str(a) + str(b))


def parse_input(filename):
    equations = [(int(r), [int(n) for n in o.split()]) for l in open(filename).read().split('\n') for r, o in
                 [l.split(':')]]
    return equations


def has_solution(target, operands, operators, value=0):
    if target == value and len(operands) == 0:
        return True
    elif target < value or len(operands) == 0:
        return False
    return any(has_solution(target, operands[1:], operators, o(value, operands[0])) for o in operators)


def part1(filename):
    equations = parse_input(filename)
    return sum(e[0] for e in equations if has_solution(e[0], e[1], [plus, multiply]))


def part2(filename):
    equations = parse_input(filename)
    return sum(e[0] for e in equations if has_solution(e[0], e[1], [plus, multiply, concat]))


assert part1('day07_input_test.txt') == 3749
print(f'Part 1: {part1('day07_input.txt')}')

assert part2('day07_input_test.txt') == 11387
print(f'Part 2: {part2('day07_input.txt')}')
