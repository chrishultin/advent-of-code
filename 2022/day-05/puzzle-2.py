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
        src_stack = int(src) - 1
        dest_stack = int(dest) - 1
        boxes = stack_contents[src_stack][-1 * int(num_to_move):]
        stack_contents[dest_stack].extend(boxes)
        stack_contents[src_stack] = stack_contents[src_stack][:-1 * int(num_to_move)]

print(''.join([stack_contents[i][-1] for i in range(0, 9)]))