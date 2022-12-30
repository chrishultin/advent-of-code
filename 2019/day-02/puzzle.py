import advent_of_code.intcode_sim as intcode

def part_one(input_file_name: str):
    with open(input_file_name) as input_file:
        instructions = input_file.readline().strip().split(',')
    instructions = [int(i) for i in instructions]

    # Part One Position Changes
    instructions[1] = 12
    instructions[2] = 2

    ship_comp = intcode.IntCodeComputer(instructions)
    while ship_comp.execute_instruction():
        print(ship_comp)

    return ship_comp.instructions[0]

def part_two(input_file_name: str):
    with open(input_file_name) as input_file:
        instructions = input_file.readline().strip().split(',')
    instructions = [int(i) for i in instructions]
    for noun in range(1, 100):
        for verb in range(1, 100):
            new_instructions = [instructions[0]] + [noun, verb] + instructions[3:]
            ship_comp = intcode.IntCodeComputer(new_instructions)
            while ship_comp.execute_instruction():
                continue
            if ship_comp.instructions[0] == 19690720:
                print([noun, verb])
                return [noun, verb]
if __name__ == '__main__':
    # print(part_one('input.txt'))
    part_2_answer = part_two('input.txt')
    print((100 * part_2_answer[0]) + part_2_answer[1])