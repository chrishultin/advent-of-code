def puzzle_1(input_file_name: str):
    horizontal_position = 0
    vertical_position = 0

    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            command = line.strip().split(' ')
            if command[0] == 'forward':
                horizontal_position += int(command[1])
            elif command[0] == 'down':
                vertical_position += int(command[1])
            elif command[0] == 'up':
                vertical_position -= int(command[1])
    print(f'horizontal: {horizontal_position}')
    print(f'vertical: {vertical_position}')

    print(vertical_position * horizontal_position)

def puzzle_2(input_file_name: str):
    horizontal_position = 0
    vertical_position = 0
    aim = 0

    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            command = line.strip().split(' ')
            direction = command[0]
            distance = int(command[1])
            if direction == 'forward':
                horizontal_position += distance
                vertical_position += aim * distance
            elif direction == 'down':
                aim += distance
            elif direction == 'up':
                aim -= distance
    print(f'horizontal: {horizontal_position}')
    print(f'vertical: {vertical_position}')
    print(vertical_position * horizontal_position)

if __name__ == '__main__':
    puzzle_2('input.txt')