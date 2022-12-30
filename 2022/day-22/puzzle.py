import advent_of_code.two_dimension_grid

def part_one_parser(input_file_name: str):
    map_grid = advent_of_code.two_dimension_grid.TwoDimensionGrid()
    instructions = []

    with open(input_file_name) as input_file:
        y_index = 0
        while True:
            line = input_file.readline()
            if line.strip() != '':
                for x,i in enumerate(line[:-1]):
                    if i != ' ':
                        map_grid.add_position(x, y_index, i)
                y_index += 1
            else:
                break
                # Map is done being loaded.  Load instructions in

        instructions_line = input_file.readline().strip()

        while len(instructions_line) > 0:
            if instructions_line.isnumeric():
                instructions.append(int(instructions_line))
                break
            next_directions = [instructions_line.find('L'), instructions_line.find('R')]
            next_turn_index = min(*[d for d in next_directions if d != -1], len(instructions_line))
            instructions.append(int(instructions_line[0:next_turn_index]))
            instructions.append(instructions_line[next_turn_index])
            instructions_line = instructions_line[next_turn_index+1:]

    return map_grid, instructions

def part_one(input_file_name: str):

    DIRECTION_VALUE_MAP = {
        'right': 0,
        'down': 1,
        'left': 2,
        'up': 3
    }
    map_grid, instructions = part_one_parser(input_file_name)

    start_position = list(map_grid.get_row(0))[0]
    print(start_position)
    direction = "right"
    print(direction)

    ROTATION_MAP = {
        'right': ['up', 'down'],
        'down': ['right', 'left'],
        'left': ['down', 'up'],
        'up': ['left', 'right']
    }

    # map_grid.render()
    current_position = start_position
    for instruction in instructions:
        if isinstance(instruction, int):
            if direction == 'right':
                next_position = current_position
                for i in range(1, instruction + 1):
                    prev_position = next_position
                    next_position = (next_position[0] + 1, next_position[1])
                    next_value = map_grid.get_position(next_position[0], next_position[1])
                    if next_value and next_value in '.<>^v':
                        map_grid.set_position(next_position[0], next_position[1], '>')
                        continue
                    if next_value == '#':
                        next_position = prev_position
                        break
                    if next_value == None:
                        # Loop around to left
                        next_position = list(map_grid.get_row(next_position[1]))[0]
                        next_value = map_grid.get_position(next_position[0], next_position[1])
                        if next_value in '.<>^v':
                            map_grid.set_position(next_position[0], next_position[1], '>')
                            continue
                        if next_value == '#':
                            next_position = prev_position
                            break
            if direction == 'down':
                next_position = current_position
                for i in range(1, instruction + 1):
                    prev_position = next_position
                    next_position = (next_position[0], next_position[1] + 1)
                    next_value = map_grid.get_position(next_position[0], next_position[1])
                    if next_value and next_value in '.<>^v':
                        map_grid.set_position(next_position[0], next_position[1], 'v')
                        continue
                    if next_value == '#':
                        next_position = prev_position
                        break
                    if next_value == None:
                        # Loop around to top
                        next_position = list(map_grid.get_column(next_position[0]))[0]
                        next_value = map_grid.get_position(next_position[0], next_position[1])
                        if next_value in '.<>^v':
                            map_grid.set_position(next_position[0], next_position[1], 'v')
                            continue
                        if next_value == '#':
                            next_position = prev_position
                            break
            if direction == 'up':
                next_position = current_position
                for i in range(1, instruction + 1):
                    prev_position = next_position
                    next_position = (next_position[0], next_position[1] - 1)
                    next_value = map_grid.get_position(next_position[0], next_position[1])
                    if next_value and next_value in '.<>^v':
                        map_grid.set_position(next_position[0], next_position[1], '^')
                        continue
                    if next_value == '#':
                        next_position = prev_position
                        break
                    if next_value == None:
                        # Loop around to bottom
                        next_position = list(map_grid.get_column(next_position[0]))[-1]
                        next_value = map_grid.get_position(next_position[0], next_position[1])
                        if next_value in '.<>^v':
                            map_grid.set_position(next_position[0], next_position[1], '^')
                            continue
                        if next_value == '#':
                            next_position = prev_position
                            break
            if direction == 'left':
                next_position = current_position
                for i in range(1, instruction + 1):
                    prev_position = next_position
                    next_position = (next_position[0] - 1, next_position[1])
                    next_value = map_grid.get_position(next_position[0], next_position[1])
                    if next_value and next_value in '.<>^v':
                        map_grid.set_position(next_position[0], next_position[1], '<')
                        continue
                    if next_value == '#':
                        next_position = prev_position
                        break
                    if next_value == None:
                        # Loop around to right
                        next_position = list(map_grid.get_row(next_position[1]))[-1]
                        next_value = map_grid.get_position(next_position[0], next_position[1])
                        if next_value in '.<>^v':
                            map_grid.set_position(next_position[0], next_position[1], '<')
                            continue
                        if next_value == '#':
                            next_position = prev_position
                            break
            current_position = next_position
            print(f'{DIRECTION_VALUE_MAP[direction]} ({current_position[1] + 1}, {current_position[0] + 1})')
        if isinstance(instruction, str):
            # print('turning')
            if instruction == 'L':
                direction = ROTATION_MAP[direction][0]
            if instruction == 'R':
                direction = ROTATION_MAP[direction][1]
            print(f'now facing {direction}')
    print(current_position)


    print(((current_position[1] + 1) * 1000) + ((current_position[0] + 1) * 4) + DIRECTION_VALUE_MAP[direction])

# E OFFSET - Y 100, X 50

def part_two_wrap_horizontal(grid: advent_of_code.two_dimension_grid.TwoDimensionGrid, y_value, direction):
    if direction == 'right':
        if y_value in range(0, 50):
            # Wrapping from B to E - Y value flips
            new_y = (100 + (49 - y_value))
            row = list(grid.get_row(new_y))
            return (row[-1], 'left')
        elif y_value in range(50, 100):
            # Wrapping from C to B, rotating Right
            new_x = y_value + 50
            column = list(grid.get_column(new_x))
            return (column[-1], 'up')
        elif y_value in range(100, 150):
            # Wrapping from E to B - Y value flips
            new_y = 49 - (y_value - 100)
            row = list(grid.get_row(new_y))
            return (row[-1], 'left')
        elif y_value in range(150, 200):
            # Wrapping from F to E, rotating Right
            new_x = y_value - 100
            column = list(grid.get_column(new_x))
            return (column[-1], 'up')
    elif direction == 'left':
        if y_value in range(0, 50):
            # Wrapping from A to D - Y value flips
            new_y = (100 + (49 - y_value))
            row = list(grid.get_row(new_y))
            return (row[0], 'right')
        elif y_value in range(50, 100):
            # Wrapping from C to D, rotating Left
            new_x = y_value - 50
            column = list(grid.get_column(new_x))
            return (column[0], 'down')
        elif y_value in range(100, 150):
            # Wrapping from D to A - Y value flips
            new_y = 49 - (y_value - 100)
            row = list(grid.get_row(new_y))
            return (row[0], 'right')
        elif y_value in range(150, 200):
            # Wrapping from F to A, rotating Left
            new_x = y_value - 100
            column = list(grid.get_column(new_x))
            return (column[0], 'down')

    return

def part_two_wrap_vertical(grid: advent_of_code.two_dimension_grid.TwoDimensionGrid, x_value, direction):
    if direction == 'up':
        if x_value in range(0, 50):
            # Wrapping from D to C, rotating Right
            new_y = x_value + 50
            row = list(grid.get_row(new_y))
            return (row[0], 'right')
        elif x_value in range(50, 100):
            # Wrapping from A to F, rotating Right
            new_y = x_value + 100
            row = list(grid.get_row(new_y))
            return (row[0], 'right')
        elif x_value in range(100,150):
            # Wrapping from B to F
            new_x = x_value - 100
            column = list(grid.get_column(new_x))
            return (column[-1], 'up')
    elif direction == 'down':
        if x_value in range(0, 50):
            # Wrapping from F to B
            new_x = x_value + 100
            column = list(grid.get_column(new_x))
            return (column[0], 'down')
        elif x_value in range(50, 100):
            # Wrapping from E to F, rotating Left
            new_y = x_value + 100
            row = list(grid.get_row(new_y))
            return (row[-1], 'left')
        elif x_value in range(100,150):
            # Wrapping from B to C
            new_y = x_value - 50
            row = list(grid.get_row(new_y))
            return (row[-1], 'left')

        return

def part_two(input_file_name: str):
    map_grid, instructions = part_one_parser(input_file_name)
    ROTATION_MAP = {
        'right': ['up', 'down'],
        'down': ['right', 'left'],
        'left': ['down', 'up'],
        'up': ['left', 'right']
    }
    DIRECTION_VALUE_MAP = {
        'right': 0,
        'down': 1,
        'left': 2,
        'up': 3
    }

    start_position = list(map_grid.get_row(0))[0]
    print(start_position)
    direction = "right"
    # print(direction)
    current_position = start_position
    for instruction in instructions:
        if isinstance(instruction, int):
            print(f'{direction} ({current_position[1] + 1}, {current_position[0] + 1}) {instruction}')
            next_position, next_direction = p2_make_move(map_grid, current_position, direction, instruction)
            current_position = next_position
            direction = next_direction
            print(f'{DIRECTION_VALUE_MAP[direction]} ({current_position[1] + 1}, {current_position[0] + 1})')
        elif isinstance(instruction, str):
            # print('turning')
            if instruction == 'L':
                direction = ROTATION_MAP[direction][0]
            if instruction == 'R':
                direction = ROTATION_MAP[direction][1]
            print(f'now facing {direction}')

    print(f'{direction} ({current_position[1] + 1}, {current_position[0] + 1})')
    print(((current_position[1] + 1) * 1000) + ((current_position[0] + 1) * 4) + DIRECTION_VALUE_MAP[direction])

def p2_make_move(map_grid, current_position, direction, instruction):
    next_position = current_position
    if direction == 'right':
        next_position = current_position
        for i in range(1, instruction + 1):
            prev_position = next_position
            next_position = (next_position[0] + 1, next_position[1])
            next_value = map_grid.get_position(next_position[0], next_position[1])
            if next_value and next_value in '.<>^v':
                map_grid.set_position(next_position[0], next_position[1], '>')
                continue
            if next_value == '#':
                next_position = prev_position
                break
            if next_value == None:
                # Loop around to left
                next_position, new_direction = part_two_wrap_horizontal(map_grid, next_position[1], direction)
                next_value = map_grid.get_position(next_position[0], next_position[1])
                if next_value in '.<>^v':
                    direction = new_direction
                    return p2_make_move(map_grid, next_position, direction, instruction - i)
                    break
                if next_value == '#':
                    next_position = prev_position
                    print('blocked')
                    break
    elif direction == 'down':
        next_position = current_position
        for i in range(1, instruction + 1):
            prev_position = next_position
            next_position = (next_position[0], next_position[1] + 1)
            next_value = map_grid.get_position(next_position[0], next_position[1])
            if next_value and next_value in '.<>^v':
                map_grid.set_position(next_position[0], next_position[1], 'v')
                continue
            if next_value == '#':
                next_position = prev_position
                break
            if next_value == None:
                # Loop around to top
                next_position, new_direction = part_two_wrap_vertical(map_grid, next_position[0], direction)
                next_value = map_grid.get_position(next_position[0], next_position[1])
                if next_value in '.<>^v':
                    direction = new_direction
                    return p2_make_move(map_grid, next_position, direction, instruction - i)
                    break
                if next_value == '#':
                    next_position = prev_position
                    break
    elif direction == 'up':
        next_position = current_position
        for i in range(1, instruction + 1):
            prev_position = next_position
            next_position = (next_position[0], next_position[1] - 1)
            next_value = map_grid.get_position(next_position[0], next_position[1])
            if next_value and next_value in '.<>^v':
                map_grid.set_position(next_position[0], next_position[1], '^')
                continue
            if next_value == '#':
                next_position = prev_position
                break
            if next_value == None:
                # Loop around to bottom
                next_position, new_direction = part_two_wrap_vertical(map_grid, next_position[0], direction)
                next_value = map_grid.get_position(next_position[0], next_position[1])
                if next_value in '.<>^v':
                    direction = new_direction
                    return p2_make_move(map_grid, next_position, direction, instruction - i)
                    break
                if next_value == '#':
                    next_position = prev_position
                    break
    elif direction == 'left':
        next_position = current_position
        for i in range(1, instruction + 1):
            prev_position = next_position
            next_position = (next_position[0] - 1, next_position[1])
            next_value = map_grid.get_position(next_position[0], next_position[1])
            if next_value and next_value in '.<>^v':
                continue
            if next_value == '#':
                next_position = prev_position
                break
            if next_value == None:
                # Loop around to right
                next_position, new_direction = part_two_wrap_horizontal(map_grid, next_position[1], direction)
                next_value = map_grid.get_position(next_position[0], next_position[1])
                if next_value in '.<>^v':
                    direction = new_direction
                    return p2_make_move(map_grid, next_position, direction, instruction - i)
                    break
                if next_value == '#':
                    next_position = prev_position
                    break
    return next_position,direction

if __name__ == '__main__':
    part_two('input.txt')