import re
from functools import reduce


def parse_input(filename):
    return [[int(x) for x in l.split()] for l in open(filename).read().splitlines()]

def mult(s):
    matches = re.finditer(r'mul\((\d+),(\d+)\)', s)
    return sum(reduce(lambda x, y: int(x) * int(y), match.groups()) for match in matches)

def part1(filename):
    return mult(open(filename).read())

def part2(filename):
    data = open(filename).read()
    ans =0
    enabled = True
    while len(data) > 0:
        if enabled:
            i = data.find("don't()")
            if i == -1:
                i = len(data)
            else:
                i += len("don't()")
            ans += mult(data[:i])
            data = data[i:]
            enabled = False
        else:
            i = data.find("do()")
            if i == -1:
                i = len(data)
            else:
                i += len("do()")
            data = data[i:]
            enabled = True
        print(data)
        print(ans)
    print(ans)
    return ans

# def part2(filename):
#     return sum(any(is_safe(record[:i] + record[i + 1:]) for i in range(len(record))) for record in parse_input(filename))

# assert part1('day03_input_test_1.txt') == 161
# assert part1('day03_input.txt') == 173731097
# print(f'Part 1: {part1('day03_input.txt')}')
#

assert part2('day03_input_test_2.txt') == 48
print(f'Part 2: {part2('day03_input.txt')}')