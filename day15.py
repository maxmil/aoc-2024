from copy import copy

DIRECTIONS = {'^': -1j, '>': 1, 'v': 1j, '<': -1}


def parse(filename, transform=lambda c: c):
    top, bottom = open(filename).read().split('\n\n')
    warehouse = {x + y * 1j: c for y, r in enumerate(top.split('\n')) for x, c in enumerate(transform(r))}
    moves = bottom.replace('\n', '')
    robot = next((k for k, v in warehouse.items() if v == '@'))
    return warehouse, moves, robot


def push(position, direction, warehouse_before_push):
    warehouse = copy(warehouse_before_push)
    nxt = position + direction
    if direction != 1 and warehouse[nxt] in ('[', ']'):
        box = nxt if warehouse[nxt] == '[' else nxt - 1
        warehouse = push(box, direction, warehouse)
    if direction != -1 and warehouse[nxt + 1] in ('[', ']'):
        box = nxt + 1 if warehouse[nxt + 1] == '[' else nxt
        warehouse = push(box, direction, warehouse)
    if (direction == 1 or warehouse[nxt] == '.') and (direction == -1 or warehouse[nxt + 1] == '.'):
        warehouse[nxt] = '['
        warehouse[nxt + 1] = ']'
        if direction != -1: warehouse[position] = '.'
        if direction != 1: warehouse[position + 1] = '.'
        return warehouse
    else:
        return warehouse_before_push


def move(position, direction, warehouse):
    nxt = position + direction
    warehouse = move(nxt, direction, warehouse)[0] if warehouse[nxt] == 'O' else warehouse
    warehouse = push(nxt, direction, warehouse) if warehouse[nxt] == '[' else warehouse
    warehouse = push(nxt - 1, direction, warehouse) if warehouse[nxt] == ']' else warehouse

    if warehouse[nxt] != '.': return warehouse, position
    warehouse[nxt] = warehouse[position]
    warehouse[position] = '.'
    return warehouse, nxt


def part1(filename):
    warehouse, moves, robot = parse(filename)
    for m in moves: warehouse, robot = move(robot, DIRECTIONS[m], warehouse)
    return sum(int(p.real + p.imag * 100) for p in warehouse if warehouse[p] == 'O')


def part2(filename):
    expand = lambda s: s.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    warehouse, moves, robot = parse(filename, expand)
    for m in moves: warehouse, robot = move(robot, DIRECTIONS[m], warehouse)
    return sum(int(p.real + p.imag * 100) for p in warehouse if warehouse[p] == '[')


assert part1('day15_input_test.txt') == 10092
print(f'Part 1: {part1('day15_input.txt')}')

assert part2('day15_input_test.txt') == 9021
print(f'Part 2: {part2('day15_input.txt')}')
