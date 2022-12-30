def puzzle_1(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        increase_count = 0
        previous_depth = int(input_file.readline().strip())
        for depth_string in input_file.readlines():
            current_depth = int(depth_string)
            if previous_depth < current_depth:
                increase_count += 1
            previous_depth = current_depth

    return increase_count

def puzzle_2(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        increase_count = 0
        current_window = []
        for i in range(0, 3):
            current_window.append(int(input_file.readline().strip()))
        for depth_string in input_file.readlines():
            new_window = current_window[1:] + [int(depth_string)]
            if sum(current_window) < sum(new_window):
                increase_count += 1
            current_window = new_window

    return increase_count

if __name__ == '__main__':
    assert puzzle_1('test_input.txt') == 7
    print(puzzle_1('input.txt'))
    print(puzzle_2('input.txt'))