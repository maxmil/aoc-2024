import copy


def parse(filename):
    top, bottom = open(filename).read().split('\n\n')
    warehouse = {x + y * 1j: c for y, r in enumerate(top.split('\n')) for x, c in enumerate(r) if c != '\n'}
    moves = bottom.replace('\n', '')
    robot = next((k for k, v in warehouse.items() if v == '@'))
    return warehouse, moves, robot

def expand(row):
    return row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')


def parse_expand(filename):
    top, bottom = open(filename).read().split('\n\n')
    warehouse = {x + y * 1j: c for y, r in enumerate(top.split('\n')) for x, c in enumerate(expand(r)) if c != '\n'}
    moves = bottom.replace('\n', '')
    robot = next((k for k, v in warehouse.items() if v == '@'))
    return warehouse, moves, robot


def draw(warehouse):
    for y in range(100):
        for x in range(100):
            if x + y * 1j in warehouse:
                print(warehouse[x + y * 1j], end='')
        if y * 1j in warehouse:
            print()
    print()


directions = {'^': -1j, '>': 1, 'v': 1j, '<': -1}


def move(position, direction, warehouse):
    if warehouse[position + direction] == 'O':
        move(position + direction, direction, warehouse)
    if warehouse[position + direction] == '.':
        warehouse[position + direction] = warehouse[position]
        warehouse[position] = '.'
        return position + direction
    else:
        return position


def part1(filename):
    warehouse, moves, robot = parse(filename)
    for m in moves:
        robot = move(robot, directions[m], warehouse)
    return sum(int(p.real + p.imag * 100) for p in warehouse if warehouse[p] == 'O')

def move_box(position, direction, warehouse):
    # print(f'move box {position} {direction}')
    wip = copy.deepcopy(warehouse)
    nxt = position + direction
    # L blocked
    if direction != 1 and wip[nxt] in ('[', ']'):
        if wip[nxt] == '[': box = nxt
        else: box = nxt - 1
        wip = move_box(box, direction, wip)

    #R blocked
    if direction != -1 and wip[nxt + 1] in ('[', ']'):
        if wip[nxt + 1] == '[': box = nxt + 1
        else: box = nxt
        wip = move_box(box, direction, wip)

    # if not both unblocked do nothing
    if (direction == 1 or wip[nxt] == '.') and (direction == -1 or wip[nxt + 1] == '.'):
        wip[nxt] = '['
        wip[nxt + 1] = ']'
        if direction != -1: wip[position] = '.'
        if direction != 1: wip[position + 1] = '.'
        return wip
    else:
        return warehouse


def move2(position, direction, warehouse):
    nxt = position + direction
    if warehouse[nxt] in ('[', ']'):
        if warehouse[nxt] == '[': box = nxt
        else: box = nxt - 1
        warehouse = move_box(box, direction, warehouse)
    if warehouse[nxt] == '.':
        warehouse[nxt] = '@'
        warehouse[position] = '.'
        return warehouse, nxt
    else:
        return warehouse, position

def part2(filename):
    warehouse, moves, robot = parse_expand(filename)
    if filename == 'day15_input_test_3.txt':
        warehouse, moves, robot = parse(filename)
    draw(warehouse)
    for m in moves:
        warehouse, robot = move2(robot, directions[m], warehouse)
        # print(m)
        # draw(warehouse)
    draw(warehouse)
    ans = sum(int(p.real + p.imag * 100) for p in warehouse if warehouse[p] == '[')
    print(ans)
    return ans

# assert part1('day15_input_test.txt') == 10092
# print(f'Part 1: {part1('day15_input.txt')}')
# 1457740

# part2('day15_input_test_3.txt')
# exit()
assert part2('day15_input_test.txt') == 9021
print(f'Part 2: {part2('day15_input.txt')}')
#< 1486484
