def parser(input_file_name: str):
    input_data = []
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            line = line.strip()
            input_data.append([x for x in line])

    return input_data

def get_adjacent_squares(x, y, grid):
    adjacent_coords = [
        (x-1, y+1),
        (x  , y+1),
        (x+1, y+1),
        (x-1, y),
        (x+1, y),
        (x-1, y-1),
        (x  , y-1),
        (x+1, y-1),
    ]

    filter_coords = [x for x in adjacent_coords if x[0] in range(0, len(grid)) and x[1] in range(0, len(grid))]

    return [grid[coord[1]][coord[0]] for coord in filter_coords]

def part_one_step(input_grid: list[list[str]]):
    output_grid = []
    for y, line in enumerate(input_grid):
        output_line = []
        for x, square in enumerate(line):
            adjacent_squares = get_adjacent_squares(x,y, input_grid)
            adjacent_on = [i for i in adjacent_squares if i == '#']
            if square == '#':
                if len(adjacent_on) == 2 or len(adjacent_on) == 3:
                    output_line.append('#')
                else:
                    output_line.append('.')
            else:
                if len(adjacent_on) == 3:
                    output_line.append('#')
                else:
                    output_line.append('.')
        output_grid.append(output_line)

    return output_grid

def part_one(input_grid, rounds=100):
    for i in range(0, rounds):
        for line in input_grid:
            print(''.join(line))
        input_grid = part_one_step(input_grid)
        print(' ')

    for line in input_grid:
        print(''.join(line))


    total = 0
    for line in input_grid:
        total += line.count('#')

    print(total)
    return total

def part_two(input_grid, rounds=100):
    corner_index = len(input_grid) - 1

    input_grid[0][0] = '#'
    input_grid[0][corner_index] = '#'
    input_grid[corner_index][corner_index] = '#'
    input_grid[corner_index][0] = '#'

    for i in range(0, rounds):
        for line in input_grid:
            print(''.join(line))
        input_grid = part_one_step(input_grid)

        # Force corners on
        input_grid[0][0] = '#'
        input_grid[0][corner_index] = '#'
        input_grid[corner_index][corner_index] = '#'
        input_grid[corner_index][0] = '#'


        print(' ')

    for line in input_grid:
        print(''.join(line))


    total = 0
    for line in input_grid:
        total += line.count('#')

    print(total)
    return total

if __name__ == '__main__':
    input_grid = parser('input.txt')

    part_two(input_grid)