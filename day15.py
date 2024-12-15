def parse(filename):
    top, bottom = open(filename).read().split('\n\n')
    warehouse = {x + y * 1j: c for y, r in enumerate(top.split('\n')) for x, c in enumerate(r) if c != '\n'}
    moves = bottom.replace('\n', '')
    robot = next((k for k, v in warehouse.items() if v == '@'))
    return warehouse, moves, robot




def draw(warehouse):
    for y in range(50):
        for x in range(50):
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


assert part1('day15_input_test.txt') == 10092
print(f'Part 1: {part1('day15_input.txt')}')
# 1457740
