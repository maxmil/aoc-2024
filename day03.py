import re

def mult(s):
    return sum(int(match[0]) * int(match[1]) for match in (re.findall(r'mul\((\d+),(\d+)\)', s)))

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
assert part1('day03_input.txt') == 173731097
print(f'Part 1: {part1('day03_input.txt')}')

assert part2('day03_input_test_2.txt') == 48
assert part2('day03_input.txt') == 93729253
print(f'Part 2: {part2('day03_input.txt')}')
