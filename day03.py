import re

def mult(s):
    return sum(int(match[0]) * int(match[1]) for match in (re.findall(r'mul\((\d+),(\d+)\)', s)))

def part1(filename):
    return mult(open(filename).read())

def part2(filename):
    mem = open(filename).read()
    ans = 0
    state = 1
    states = ['do()', "don't()"]
    while len(mem) > 0:
        i = len(mem) if (i := mem.find(states[state])) == -1 else i + len(states[state])
        if state: ans += mult(mem[:i])
        state = (state + 1) % 2
        mem = mem[i:]
    return ans

assert part1('day03_input_test_1.txt') == 161
print(f'Part 1: {part1('day03_input.txt')}')

assert part2('day03_input_test_2.txt') == 48
print(f'Part 2: {part2('day03_input.txt')}')
