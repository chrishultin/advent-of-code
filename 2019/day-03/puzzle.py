def parser(input_file_name: str):
    with open(input_file_name) as input_file:
        line_one = input_file.readline().strip().split(',')
        line_two = input_file.readline().strip().split(',')

    return line_one, line_two

def part_one_line(start_position: complex, instruction: str) -> list[complex]:
    direction = instruction[0]
    distance = int(''.join(instruction[1:]))
    output = []
    if direction == 'R':
        for x in range(1, distance + 1):
            output.append(start_position + x)
    elif direction == 'L':
        for x in range(1, distance + 1):
            output.append(start_position - x)
    elif direction == 'U':
        for x in range(1, distance + 1):
            output.append(start_position + (x*1j))
    elif direction == 'D':
        for x in range(1, distance + 1):
            output.append(start_position - (x*1j))
    return output

def manhattan_distance(start: complex, end: complex):
    return (abs(start.real - end.real) + abs(start.imag - end.imag))

def part_one(input_file_name):
    line_one, line_two = parser(input_file_name)
    # line_one = ['R8','U5','L5','D3']
    # line_two = ['U7', 'R6', 'D4', 'L4']

    line_one_positions = set()
    line_one_current = 0
    line_two_positions = set()
    line_two_current = 0
    for instruction in line_one:
        line = part_one_line(line_one_current, instruction)
        line_one_positions.update(line)
        line_one_current = line[-1]

    for instruction in line_two:
        line = part_one_line(line_two_current, instruction)
        line_two_positions.update(line)
        line_two_current = line[-1]

    min_distance = 9999999
    for position in line_one_positions.intersection(line_two_positions):
        distance = manhattan_distance(0, position)
        if distance < min_distance:
            min_distance = distance
        print(f'{position}: {distance}')
    print(int(min_distance))

def part_two(input_file_name):
    line_one, line_two = parser(input_file_name)

    line_one_positions = []
    line_one_current = 0
    line_two_positions = []
    line_two_current = 0

    for instruction in line_one:
        line = part_one_line(line_one_current, instruction)
        line_one_positions.extend(line)
        line_one_current = line[-1]

    for instruction in line_two:
        line = part_one_line(line_two_current, instruction)
        line_two_positions.extend(line)
        line_two_current = line[-1]

    overlapping_spots = list(set(line_one_positions).intersection(set(line_two_positions)))

    min_steps = 99999999
    for spot in overlapping_spots:
        index_one = line_one_positions.index(spot)
        index_two = line_two_positions.index(spot)

        steps = index_one + index_two + 2
        if steps < min_steps:
            min_steps = steps

    print(min_steps)


if __name__ == '__main__':
    part_two('input.txt')