def puzzle_1(instructions: str) -> tuple[int, int]:
    house_tracker = {
        '0,0': 1
    }
    current_position = (0,0)
    for instruction in instructions:
        if instruction == '^':
            current_position = (current_position[0] + 1, current_position[1])
        elif instruction == '>':
            current_position = (current_position[0], current_position[1] + 1)
        elif instruction == 'v':
            current_position = (current_position[0] - 1, current_position[1])
        elif instruction == '<':
            current_position = (current_position[0], current_position[1] - 1)
        positionStr = f"{current_position[0]},{current_position[1]}"
        house_tracker[positionStr] = house_tracker.get(positionStr, 0) + 1

    houses_gte_2 = [i for i in house_tracker.values() if i >= 1]
    return len(houses_gte_2)

def puzzle_1(instructions: str) -> tuple[int, int]:
    house_tracker = {
        '0,0': 1
    }
    current_position = (0,0)
    for instruction in instructions:
        if instruction == '^':
            current_position = (current_position[0] + 1, current_position[1])
        elif instruction == '>':
            current_position = (current_position[0], current_position[1] + 1)
        elif instruction == 'v':
            current_position = (current_position[0] - 1, current_position[1])
        elif instruction == '<':
            current_position = (current_position[0], current_position[1] - 1)
        positionStr = f"{current_position[0]},{current_position[1]}"
        house_tracker[positionStr] = house_tracker.get(positionStr, 0) + 1

    houses_gte_2 = [i for i in house_tracker.values() if i >= 1]
    return len(houses_gte_2)

def puzzle_2(instructions: str) -> tuple[int, int]:
    house_tracker = {
        '0,0': 2
    }
    santa_position = (0,0)
    robot_position = (0,0)
    for instruction in instructions[0::2]:
        if instruction == '^':
            santa_position = (santa_position[0] + 1, santa_position[1])
        elif instruction == '>':
            santa_position = (santa_position[0], santa_position[1] + 1)
        elif instruction == 'v':
            santa_position = (santa_position[0] - 1, santa_position[1])
        elif instruction == '<':
            santa_position = (santa_position[0], santa_position[1] - 1)
        positionStr = f"{santa_position[0]},{santa_position[1]}"
        house_tracker[positionStr] = house_tracker.get(positionStr, 0) + 1

    for instruction in instructions[1::2]:
        if instruction == '^':
            robot_position = (robot_position[0] + 1, robot_position[1])
        elif instruction == '>':
            robot_position = (robot_position[0], robot_position[1] + 1)
        elif instruction == 'v':
            robot_position = (robot_position[0] - 1, robot_position[1])
        elif instruction == '<':
            robot_position = (robot_position[0], robot_position[1] - 1)
        positionStr = f"{robot_position[0]},{robot_position[1]}"
        house_tracker[positionStr] = house_tracker.get(positionStr, 0) + 1

    houses_gte_2 = [i for i in house_tracker.values() if i >= 1]
    return len(houses_gte_2)

if __name__ == '__main__':
    test_inputs = [
        ('>', 2),
        ('^>v<', 4),
        ('^v^v^v^v^v', 2)
    ]
    for instruction, result in test_inputs:
        assert puzzle_1(instruction) == result

    with open('input.txt', 'r') as input_file:
        input = input_file.readline().strip()

    test_inputs = [
        ('^v', 3),
        ('^>v<', 3),
        ('^v^v^v^v^v', 11)
    ]
    for instruction, result in test_inputs:
        assert puzzle_2(instruction) == result

    print(puzzle_2(input))