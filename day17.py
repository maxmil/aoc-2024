def combo(operand, registers):
    return operand if operand < 4 or operand == 7 else registers[operand - 4]


def run(program, registers):
    out = []
    pointer = 0
    while pointer < len(program):
        opcode, operand = program[pointer:pointer + 2]
        if opcode == 0:
            registers[0] = registers[0] // 2 ** combo(operand, registers)
        if opcode == 1:
            registers[1] = registers[1] ^ operand
        if opcode == 2:
            registers[1] = combo(operand, registers) % 8
        if opcode == 3:
            if registers[0] != 0:
                pointer = operand
                continue
        if opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        if opcode == 5:
            out.append(combo(operand, registers) % 8)
        if opcode == 6:
            registers[1] = registers[0] // 2 ** combo(operand, registers)
        if opcode == 7:
            registers[2] = registers[0] // 2 ** combo(operand, registers)
        pointer += 2
        if program[0:len(out)] != out:
            return out
        # print(registers)
    return out


def part1(registers, program):
    return ','.join(map(str, run(program, registers)))


def part2(program):
    i = 0
    while True:
        if run(program, [i, 0, 0]) == program:
            return i
        i += 1


# assert part1([729, 0, 0], [0, 1, 5, 4, 3, 0]) == '4,6,3,5,6,3,5,2,1,0'
# print(f'Part 1: {part1([23999685, 0, 0], [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 4, 5, 5, 3, 0])}')

# assert part2([0,3,5,4,3,0]) == 117440
# print(f'Part 2: {part2([2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 4, 5, 5, 3, 0])}')
# def prog(a):
#     out, b, c = [], 0, 0
#     while a != 0: # 3, 0
#         b = a % 8  # 2, 4
#         b = b ^ 1  # 1, 1
#         c = a // 2 ** b  # 7, 5
#         b = b ^ 5  # 1, 5
#         a = a // 2 ** 3  # 0, 3
#         b = b ^ c  # 4, 4
#         out.append(b % 8)  # 5, 5
#     print(out)
#     return out

# def prog(a):
#     out, b, c = [], 0, 0
#     while a != 0:
#         b = a % 8 # 2, 4
#         b = b ^ 1 # 1, 1
#         #c = a // 2 ** b # 7, 5
#         #b = b ^ 5 # 1, 5
#         b = (b ^ 5) ^ (a // 2 ** b)  # b = b ^ c  (4, 4)
#         a = a // 2 ** 3  # 0, 3
#         out.append(b % 8) # 5, 5
#     print(out)
#     return out

# def prog(a):
#     out, b, c = [], 0, 0
#     while a != 0:
#         b = (a % 8) ^ 1 ^ 5 ^ (a // 2 ** ((a % 8) ^ 1))
#         a = a // 8
#         out.append(b % 8)
#     print(out)
#     return out

def prog(a):
    out, b, c = [], 0, 0
    while a != 0:
        out.append(((a % 8) ^ (a // 2 ** ((a % 8) ^ 1)) % 8) ^ 4)
        a = a // 8
    # print(out)
    return out


def output(a):
    return ((a % 8) ^ (a // 2 ** ((a % 8) ^ 1)) % 8) ^ 4



# for a in range(100):
#     print(f'{a} {len(prog(a))}')
# exit()
#


target = [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 4, 5, 5, 3, 0]

def find_digits_before(index, sum):
    if index == -1:
        return sum
    for a in range(sum * 8, (sum + 1) * 8):
        # print(a)
        out = output(a)
        print(out)
        # if digit == 15: print(out)
        # print(out, target[len(target) - digit - 1])
        if out == target[index]:
            print(index)
            print(a)
            print(prog(a))
            print()
            found = find_digits_before(index - 1, a)
            if found != -1:
                return found
        a += 1
    return -1

ans=find_digits_before(len(target) - 1, 0)
print(ans)
print(prog(ans))

exit()
# exit()

# for i  in possible: print(prog(i))

# print(prog(possible[-1]))
# print(prog(possible[-2]))


# (a % 8) ^ 1 ^ 5 ^ (a // 2 ** ((a % 8) ^ 1)) == n

# assert prog(23999685) == [5, 0, 3, 5, 7, 6, 1, 5, 4]

# print(f'Part 1: {part1([23999685, 0, 0], [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 4, 5, 5, 3, 0])}')


# print([2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 4, 5, 5, 3, 0])
# for i in range(100):
#     print(prog(10 ** 14 + i * 10 ** 2))
