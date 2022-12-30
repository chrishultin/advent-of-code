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

print('break')
strengths = []
for i in [20, 60, 100, 140, 180, 220]:
    strengths.append(i * state[i - 1])

print(strengths)
print(sum(strengths))