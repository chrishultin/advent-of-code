import typing


def parser(input_file_name: str) -> typing.List:
    instructions = []
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            line = line.strip().replace(',', '').split(' ')
            if len(line) == 3:
                instructions.append([line[0], line[1], int(line[2])])
            else:
                instructions.append([line[0], line[1]])

    return instructions

def part_one(instructions: typing.List):
    register_a = 0
    register_b = 0
    current_index = 0
    max_index = len(instructions)

    while current_index < max_index:
        current_instruction = instructions[current_index]
        print(current_index, current_instruction)
        print(register_a, register_b)
        instruction = current_instruction[0]
        register = current_instruction[1]

        if instruction == 'hlf':
            if register == 'a':
                register_a = register_a // 2
            elif register == 'b':
                register_b = register_b // 2
            current_index += 1
        elif instruction == 'tpl':
            if register == 'a':
                register_a = register_a * 3
            elif register == 'b':
                register_b = register_b * 3
            current_index += 1
        elif instruction == 'inc':
            if register == 'a':
                register_a = register_a + 1
            elif register == 'b':
                register_b = register_b + 1
            current_index += 1
        elif instruction == 'jmp':
            current_index += int(register)
        elif instruction == 'jie':
            if register == 'a' and register_a%2==0:
                current_index += int(current_instruction[2])
            elif register == 'b' and register_b%2==0:
                current_index += int(current_instruction[2])
            else:
                current_index += 1
        elif instruction == 'jio':
            if register == 'a' and register_a==1:
                current_index += int(current_instruction[2])
            elif register == 'b' and register_b==1:
                current_index += int(current_instruction[2])
            else:
                current_index += 1

    print(register_a, register_b)

def part_two(instructions: typing.List):
    register_a = 1
    register_b = 0
    current_index = 0
    max_index = len(instructions)

    while current_index < max_index:
        current_instruction = instructions[current_index]
        print(current_index, current_instruction)
        print(register_a, register_b)
        instruction = current_instruction[0]
        register = current_instruction[1]

        if instruction == 'hlf':
            if register == 'a':
                register_a = register_a // 2
            elif register == 'b':
                register_b = register_b // 2
            current_index += 1
        elif instruction == 'tpl':
            if register == 'a':
                register_a = register_a * 3
            elif register == 'b':
                register_b = register_b * 3
            current_index += 1
        elif instruction == 'inc':
            if register == 'a':
                register_a = register_a + 1
            elif register == 'b':
                register_b = register_b + 1
            current_index += 1
        elif instruction == 'jmp':
            current_index += int(register)
        elif instruction == 'jie':
            if register == 'a' and register_a%2==0:
                current_index += int(current_instruction[2])
            elif register == 'b' and register_b%2==0:
                current_index += int(current_instruction[2])
            else:
                current_index += 1
        elif instruction == 'jio':
            if register == 'a' and register_a==1:
                current_index += int(current_instruction[2])
            elif register == 'b' and register_b==1:
                current_index += int(current_instruction[2])
            else:
                current_index += 1

    print(register_a, register_b)

if __name__ == '__main__':
    instructions = parser('input.txt')
    part_two(instructions)