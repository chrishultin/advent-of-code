import collections


def parser(input_file_name: str):
    orbit_dict = {}
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            line = line.strip().split(')')

            orbit_dict[line[0]] = orbit_dict.get(line[0], []) + [line[1]]

    return orbit_dict

def part_one(orbits: dict):
    orbit_count = 0

    queue = collections.deque([('COM', 0)])
    while queue:
        current_planet, current_depth = queue.popleft()
        print(current_planet)

        orbiting_planets = orbits.get(current_planet)
        orbit_count += current_depth
        if orbiting_planets is None:
            continue

        for orbiting_planet in orbiting_planets:
            queue.append((orbiting_planet, current_depth + 1))

    print(orbit_count)

def path_to_planet(orbits: dict, planet: str):
    queue = collections.deque([['COM']])
    while queue:
        current_path = queue.popleft()
        if current_path[-1] == planet:
            return current_path

        orbiting_planets = orbits.get(current_path[-1])
        if orbiting_planets is None:
            continue

        for orbiting_planet in orbiting_planets:
            queue.append(current_path + [orbiting_planet])



if __name__ == '__main__':
    orbits = parser('input.txt')

    path_to_you = path_to_planet(orbits, 'YOU')

    path_to_san = path_to_planet(orbits, 'SAN')
    matching_lengths = 0
    while True:
        if path_to_you[matching_lengths] == path_to_san[matching_lengths]:
            matching_lengths += 1
        else:
            break
    print(matching_lengths)
    print(len(path_to_you) + len(path_to_san) - (2*matching_lengths) - 2)