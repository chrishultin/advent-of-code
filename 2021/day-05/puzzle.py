import math


def puzzle_1(input_file_name: str):
    row_range = 0
    column_range = 0

    lines = []

    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            start, end = line.strip().split(' -> ')
            start = start.split(',')
            start = [int(i) for i in start]
            end = end.split(',')
            end = [int(i) for i in end]
            if start[0] > row_range:
                row_range = start[0]
            if end[0] > row_range:
                row_range = end[0]
            if start[1] > column_range:
                column_range = start[1]
            if end[1] > column_range:
                column_range = end[1]

            lines.append([start, end])
    row_range += 1
    column_range += 1
    print(f'{row_range} {column_range}')

    line_values = []
    for row in range(0, row_range + 1):
        line_values.append([])
        for column in range(0, column_range + 1):
            line_values[row].append(0)

    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            #horizontal/vertical
            x_start, x_end = sorted([line[0][0], line[1][0]])
            y_start, y_end = sorted([line[0][1], line[1][1]])
            for row in range(x_start, x_end + 1):
                for column in range(y_start, y_end + 1):
                    print(f'{row} {column}')
                    line_values[row][column] += 1

    num_gte_2 = 0
    for row in reversed(line_values):
        print(row)
        for value in row:
            if value >= 2:
                num_gte_2 += 1

    print(num_gte_2)

def puzzle_2(input_file_name: str):
    row_range = 0
    column_range = 0

    lines = []

    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            start, end = line.strip().split(' -> ')
            start = start.split(',')
            start = [int(i) for i in start]
            end = end.split(',')
            end = [int(i) for i in end]
            if start[0] > row_range:
                row_range = start[0]
            if end[0] > row_range:
                row_range = end[0]
            if start[1] > column_range:
                column_range = start[1]
            if end[1] > column_range:
                column_range = end[1]

            lines.append([start, end])
    row_range += 1
    column_range += 1
    print(f'{row_range} {column_range}')

    line_values = []
    for row in range(0, row_range + 1):
        line_values.append([])
        for column in range(0, column_range + 1):
            line_values[row].append(0)

    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            #horizontal/vertical
            x_start, x_end = sorted([line[0][0], line[1][0]])
            y_start, y_end = sorted([line[0][1], line[1][1]])
            for row in range(x_start, x_end + 1):
                for column in range(y_start, y_end + 1):
                    print(f'{row} {column}')
                    line_values[row][column] += 1
        else:
            x_dir = int(math.copysign(1, line[1][0] - line[0][0]))
            y_dir = int(math.copysign(1, line[1][1] - line[0][1]))
            current_pos = line[0].copy()
            line_values[current_pos[0]][current_pos[1]] += 1
            while current_pos[0] != line[1][0] or current_pos[1] != line[1][1]:
                current_pos[0] += x_dir
                current_pos[1] += y_dir
                line_values[current_pos[0]][current_pos[1]] += 1

    num_gte_2 = 0
    for row in reversed(line_values):
        print(row)
        for value in row:
            if value >= 2:
                num_gte_2 += 1

    print(num_gte_2)


if __name__ == '__main__':
    puzzle_2('input.txt')