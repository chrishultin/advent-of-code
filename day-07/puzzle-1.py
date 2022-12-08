INPUT_FILE = 'input.txt'


current_directory = {}
directory_structure = {'/': current_directory}

big_dirs = []

def calculate_directory_size(path: list, directory: dict):
    total_size = 0
    for item, value in directory.items():
        if isinstance(value, int):
            total_size += value
        else:
            path.append(item)
            total_size += calculate_directory_size(path, value)
    if total_size <= 100000:
        big_dirs.append(('/'.join(path), total_size))
    return total_size

with open(INPUT_FILE, 'r') as input_file:
    current_path = ['/']
    #skip first line
    command_line = input_file.readline()
    while True:
        command_line = input_file.readline().strip()
        if not command_line:
            break

        if command_line[0] == '$':
            if command_line[2:4] == 'ls':
                pass
            elif command_line[5:7] == '..':
                current_path.pop()
                current_directory = directory_structure
                for i in current_path:
                    current_directory = current_directory[i]
            else:
                current_path.append(f'{command_line[5:]}')
                current_directory = current_directory[command_line[5:]]

        else:
            if command_line[0:3] == 'dir':
                current_directory[command_line[4:]] = {}
            else:
                size, file_name = command_line.split(' ')
                current_directory[file_name] = int(size)

    print(directory_structure)

    calculate_directory_size(["/"], directory_structure)
    # print(big_dirs)
    total_size = 0
    for dir, size in big_dirs:
        total_size += size
    print(total_size)