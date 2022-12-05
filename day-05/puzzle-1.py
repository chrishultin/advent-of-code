INPUT_FILE = 'input.txt'

stack_contents = [[], [], [], [], [], [], [], [], []]

with open(INPUT_FILE, 'r') as stack_file:
    for i in range(0, 8):
        line = stack_file.readline()
        for j in range(0, 9):
            box_content = line[(j*4)+1:(j*4)+2]
            if box_content != ' ':
                stack_contents[j].insert(0, box_content)

    for _ in range(0, 2):
        stack_file.readline()

    while True:
        line = stack_file.readline().strip()
        if not line:
            break
        _, num_to_move, _, src, _, dest = line.split(' ')
        for i in range(0, int(num_to_move)):
            print(stack_contents)
            stack_contents[int(dest) - 1].append(stack_contents[int(src) - 1].pop())

print(''.join([stack_contents[i][-1] for i in range(0, 9)]))