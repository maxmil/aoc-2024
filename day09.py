def part1(filename):
    disk = list(map(int, open(filename).read()))
    defrag = []
    front_ind = 0
    front_id = 0
    back_ind = len(disk) - 1
    back_id = back_ind // 2
    move = []
    while front_ind <= back_ind:
        for i in range(disk[front_ind]):
            defrag.append(front_id)
        front_ind +=1
        space = disk[front_ind]
        while len(move) < space and back_ind > front_ind:
            for j in range(disk[back_ind]):
                move.insert(0, back_id)
            back_ind -= 2
            back_id -=1
        for k in range(min(space, len(move))):
            defrag.append(move.pop())
        front_ind += 1
        front_id += 1
    for i in range(len(move)):
        defrag.append(move.pop())
    # print(''.join(map(str, defrag)))
    ans = sum(i * id for i, id in enumerate(defrag))
    return ans


def part2(filename):
    return 0


assert part1('day09_input_test.txt') == 1928
print(f'Part 1: {part1('day09_input.txt')}')
# 6259790630969

assert part2('day09_input_test.txt') == 2858
print(f'Part 2: {part2('day09_input.txt')}')