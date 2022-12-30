def parser(input_file_name: str):
    sensor_pairs = []
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            components = line.strip().split(' ')
            sensor_x = int(components[2][2:-1])
            sensor_y = int(components[3][2:-1])

            beacon_x = int(components[8][2:-1])
            beacon_y = int(components[9][2:])

            sensor_pairs.append([(sensor_x, sensor_y), (beacon_x, beacon_y), calculate_distance((sensor_x, sensor_y), (beacon_x, beacon_y))])

    return sensor_pairs

def calculate_distance(start, end):
    return (abs(start[0] - end[0]) + abs(start[1] - end[1]))

def calculate_blocked_range(start, distance, row):
    y_range = range(start[1] - distance, start[1] + distance + 1)
    if row in y_range:
        y_distance = abs(start[1] - row)
        x_distance = distance - y_distance
        if x_distance < 0:
            return
        return (start[0] - x_distance, start[0] + x_distance)
    return


def areas_in_range(start, distance, row):
    areas = []
    for x in range(start[0] - distance, start[0] + distance + 1):
        max_y = start[1] + (distance - abs(x - start[0])) + 1
        min_y = start[1] - (distance - abs(x - start[0]))
        y_range = range(min_y, max_y)
        if row in y_range:
            areas.append((x, row))
    return areas



def part_one(sensor_pairs: list[list[tuple[int, int], tuple[int, int], int]], row):
    # make grid
    blocked_areas = set()

    for pair in sensor_pairs:
        areas = areas_in_range(pair[0], pair[2], row)
        for area in areas:
            if area != pair[1]:
                blocked_areas.add(area)

    blocked_count = 0
    for area in blocked_areas:
        if area[1] == row:
            blocked_count += 1

    print(blocked_count)

def part_two(sensor_pairs):
    for row in range(0, 4000000):
        # print(f'row {row}')
        ranges = []
        for pair in sensor_pairs:
            blocked = calculate_blocked_range(pair[0], pair[2], row)
            if blocked:
                ranges.append(blocked)
        ranges.sort()
        compact_ranges = []
        low_x, high_x = ranges[0]
        for new_low_x, new_high_x in ranges[1:]:
            if new_low_x - 1 <= high_x:
                # if they overlap
                high_x = max(high_x, new_high_x)
            else:
                compact_ranges.append((low_x, high_x))
                low_x, high_x = new_low_x, new_high_x
        compact_ranges.append((low_x, high_x))
        if len(compact_ranges) == 2:
            y = row
            x = compact_ranges[0][1] + 1
            print((4000000 * x) + y)
            return


if __name__ == '__main__':
    # part_one(parser('test_input.txt'), 10)
    # part_one(parser('input.txt'), 2000000)
    part_two(parser('input.txt'))