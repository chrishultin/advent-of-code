# puzzle 1 instructions
def puzzle_1(instructions: str) -> int:
    upCount = len([i for i in instructions if i == '('])
    downCount = len([i for i in instructions if i == ')'])

    return upCount - downCount

def puzzle_2(instructions: str) -> int:
    currentFloor = 0
    instruction_map = {'(': 1, ')': -1}
    for instruction_index, instruction in enumerate(instructions):
        currentFloor += instruction_map[instruction]
        if currentFloor < 0:
            return instruction_index + 1

if __name__ == '__main__':
    test_inputs = [
        ('(())', 0),
        ('()()', 0),
        ('(((', 3),
        ('(()(()(', 3),
        ('))(((((', 3),
        ('())', -1),
        ('))(', -1),
        (')))', -3),
        (')())())', -3)
    ]
    for instructions, result in test_inputs:
        actual_result = puzzle_1(instructions)
        assert actual_result == result
    print('Tests passed; Attempting Part 1')
    # with open('input.txt', 'r') as input_file:
        # print(puzzle_1(input_file.readline().strip()))

    test_inputs = [
        (')', 1),
        ('()())', 5)
    ]
    for instructions, result in test_inputs:
        actual_result = puzzle_2(instructions)
        assert actual_result == result
    with open('input.txt', 'r') as input_file:
        print(puzzle_2(input_file.readline().strip()))