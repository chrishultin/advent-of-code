INPUT_FILE = 'input.txt'

state = [1]

with open(INPUT_FILE, 'r') as input_file:
    for line in input_file.readlines():
        command = line.strip().split(' ')
        if command[0] == 'noop':
            state.append(state[-1])
        elif command[0] == 'addx':
            state.append(state[-1])
            state.append(state[-1] + int(command[1]))

for row in range(0, 6):
    row_data = ""
    for column in range(0, 40):
        index = (40 * row) + column
        register = state[index]
        sprite_range = range(register - 1, register + 2)
        if column in sprite_range:
            row_data = row_data + "#"
        else:
            row_data = row_data + "."
    print(row_data)