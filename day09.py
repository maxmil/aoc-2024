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
        front_ind += 1
        space = disk[front_ind]
        while len(move) < space and back_ind > front_ind:
            for j in range(disk[back_ind]):
                move.insert(0, back_id)
            back_ind -= 2
            back_id -= 1
        for k in range(min(space, len(move))):
            defrag.append(move.pop())
        front_ind += 1
        front_id += 1
    for i in range(len(move)):
        defrag.append(move.pop())
    return sum(i * f for i, f in enumerate(defrag))


def part2(filename):
    disk = list(map(int, open(filename).read()))
    files = disk[::2]
    spaces = disk[1::2]
    moved = [[] for _ in range(len(disk))]
    for index, file_size in enumerate(reversed(files)):
        file_index = len(files) - index - 1
        space = -1
        for space_index, space_size in enumerate(spaces):
            if space_index > file_index:
                break
            if space_size >= file_size:
                space = space_index
                break
        if space == -1:
            moved[file_index * 2] = [(file_index, file_size)]
        else:
            moved[space * 2 + 1].append((file_index, file_size))
            spaces[space] -= file_size

    defrag = []
    for index, moved_files in enumerate(moved):
        if len(moved_files) == 0:
            if index % 2 == 0:
                for i in range(files[index // 2]):
                    defrag.append(0)
            else:
                for i in range(spaces[index // 2]):
                    defrag.append(0)
        else:
            for (file_index, file_size) in moved_files:
                for i in range(file_size):
                    defrag.append(file_index)
            if index % 2 == 1:
                for i in range(spaces[index // 2]):
                    defrag.append(0)

    return sum(i * f for i, f in enumerate(defrag))


assert part1('day09_input_test.txt') == 1928
print(f'Part 1: {part1('day09_input.txt')}')

assert part2('day09_input_test.txt') == 2858
print(f'Part 2: {part2('day09_input.txt')}')
