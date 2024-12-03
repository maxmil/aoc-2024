import re
from functools import reduce

def mult(s):
    matches = re.finditer(r'mul\((\d+),(\d+)\)', s)
    return sum(reduce(lambda x, y: int(x) * int(y), match.groups()) for match in matches)

def part1(filename):
    return mult(open(filename).read())

def part2(filename):
    mem = open(filename).read()
    ans = 0
    enabled = True
    while len(mem) > 0:
        if enabled:
            i = len(mem) if (i := mem.find("don't()")) == -1 else i + len("don't()")
            ans += mult(mem[:i])
        else:
            i = len(mem) if (i := mem.find("do()")) == -1 else i + len("do()")
        mem = mem[i:]
        enabled = not enabled
    return ans

assert part1('day03_input_test_1.txt') == 161
print(f'Part 1: {part1('day03_input.txt')}')

assert part2('day03_input_test_2.txt') == 48
print(f'Part 2: {part2('day03_input.txt')}')
