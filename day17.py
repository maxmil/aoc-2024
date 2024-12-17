def combo(operand, registers):
    return operand if operand < 4 or operand == 7 else registers[operand - 4]


def part1(registers, program):
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
        # print(registers)

    ans = ','.join(map(str, out))
    print(ans)
    return ans


def part2(registers, program):
    return ""


test_cases = [
    ([729, 0, 0], [0, 1, 5, 4, 3, 0], '4,6,3,5,6,3,5,2,1,0', None),
    ([10, 0, 0], [5, 0, 5, 1, 5, 4], '0,1,2', None),
    ([2024, 0, 0], [0, 1, 5, 4, 3, 0], '4,2,5,6,7,7,7,7,3,1,0', [0, 0, 0]),
    ([0, 29, 0], [1, 7], None, [0, 26, 0]),
    ([0, 2024, 43690], [4, 0], None, [0, 44354, 43690])
]

def assert_test_cases():
    for (registers, program, expected_output, expected_registers) in test_cases:
        output = part1(registers, program)
        print(output, registers)
        if expected_output: assert output == expected_output
        if expected_registers: assert registers == expected_registers

assert_test_cases()
assert part1([729, 0, 0], [0, 1, 5, 4, 3, 0]) == '4,6,3,5,6,3,5,2,1,0'
print(f'Part 1: {part1([23999685, 0, 0], [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 4, 5, 5, 3, 0])}')
# 2,4,1,5,1,6,5,5,0
# 6,5,3,6,3,3,7,7,0
# 4,4,4,3,0,6,6,2,1

#
# assert part2('day17_input_test.txt') == 45
# print(f'Part 2: {part2('day17_input.txt')}')
