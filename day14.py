import math
import re

def position_after(start, velocity, seconds, space):
    position = (start + seconds * velocity)
    return position.real % space.real + (position.imag % space.imag) * 1j

def part1(filename, space):
    robots = [ ((int(px) + int(py) * 1j), (int(vx) + int(vy) * 1j))
         for l in open(filename).read().split('\n')
         for (px, py, vx, vy) in re.findall(r'p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)', l)]
    positions = [ position_after(r[0], r[1], 100, space) for r in robots]
    draw(positions, space)
    quadrants = [0 for _ in range(4)]
    axis = (space - (1 + 1j)) / 2
    for p in positions:
        if p.real < axis.real:
            if p.imag < axis.imag: quadrants[0] += 1
            elif p.imag > axis.imag: quadrants[2] += 1
        elif p.real > axis.real:
            if p.imag < axis.imag: quadrants[1] += 1
            elif p.imag > axis.imag:
                print(p, axis)
                quadrants[3] += 1
    print(quadrants)
    return math.prod(quadrants)

def draw(positions, space):
    for y in range(int(space.imag)):
        for x in range(int(space.real)):
            cnt = positions.count(x + y * 1j)
            if cnt == 0: print('.', end='')
            else: print(str(cnt), end='')
        print()

def part2(filename):
    return 0


assert part1('day14_input_test.txt', 11 + 7j) == 12
print(f'Part 1: {part1('day14_input.txt', 101 + 103j)}')
print(f'Part 2: {part2('day14_input.txt')}')