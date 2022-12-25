from collections import deque as queue

def part_one(input_file_name: str):
    input_cubes = []
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().split(',')
            input_cubes.append([int(i) for i in line])
    exposed_sides = 0
    for i in input_cubes:
        exposed_sides += check_adjacent_cubes(i, input_cubes)

    print(exposed_sides)
    return exposed_sides

def check_adjacent_cubes(current_cube, all_cubes):
    adjacent_spots = [
        [current_cube[0] + 1, current_cube[1], current_cube[2]],
        [current_cube[0] - 1, current_cube[1], current_cube[2]],
        [current_cube[0], current_cube[1] + 1, current_cube[2]],
        [current_cube[0], current_cube[1] - 1, current_cube[2]],
        [current_cube[0], current_cube[1], current_cube[2] + 1],
        [current_cube[0], current_cube[1], current_cube[2] - 1],
    ]
    exposed_sides = len([s for s in adjacent_spots if s not in all_cubes])
    return exposed_sides

def spot_in_range(spot, max_size):
    return all([s in range(0, max_size) for s in spot])

def get_adjacent_cubes(current_cube, all_cubes, max_size):
    adjacent_spots = [
        (current_cube[0] + 1, current_cube[1], current_cube[2],),
        (current_cube[0] - 1, current_cube[1], current_cube[2],),
        (current_cube[0], current_cube[1] + 1, current_cube[2],),
        (current_cube[0], current_cube[1] - 1, current_cube[2],),
        (current_cube[0], current_cube[1], current_cube[2] + 1,),
        (current_cube[0], current_cube[1], current_cube[2] - 1,),
    ]
    exposed_sides = [s for s in adjacent_spots if (tuple(s) not in all_cubes) and spot_in_range(s, max_size)]
    return exposed_sides

def part_two(input_file_name):
    input_cubes = []
    max_size = 0
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().split(',')
            input_cubes.append(tuple(int(i) for i in line))
            max_size = max(max_size, *[int(i) for i in line])

    max_size += 1

    current_spot = (0,0,0)
    visited = set([current_spot])
    q = queue([current_spot])

    while q:
        current_spot = q.popleft()
        adjacent_cubes = get_adjacent_cubes(current_spot, input_cubes, max_size)
        for cube in adjacent_cubes:
            if cube not in visited and cube not in input_cubes:
                visited.add(cube)
                q.append(cube)

    all_cubes = {(x,y,z) for x in range(0,max_size) for y in range(0,max_size) for z in range(0,max_size)}
    center_cubes = (all_cubes - visited)
    for i in input_cubes:
        assert i in center_cubes
        center_cubes.remove(i)


    # center_cubes = [(1,1,1,), (1,1,2,)]
    print(list(center_cubes))
    exposed_sides = 0
    for i in list(center_cubes):
        adj_cubes = get_adjacent_cubes(i, center_cubes, max_size)
        for adj_cube in adj_cubes:
            if adj_cube not in center_cubes:
                exposed_sides += 1
    print(exposed_sides)

    print(part_one(input_file_name) - exposed_sides)




if __name__ == '__main__':
    part_two('input.txt')