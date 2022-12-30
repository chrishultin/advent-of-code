import itertools
from collections import deque as queue

def route_parser(input_file_name: str) -> dict:
    santamap = {}
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip()
            components = line.split(' ')

            start = components[0]
            end = components[2]
            distance = int(components[4])

            # Set in both directions
            start_map = santamap.get(start, {})
            start_map[end] = distance
            santamap[start] = start_map

            end_map = santamap.get(end, {})
            end_map[start] = distance
            santamap[end] = end_map
    return santamap

def calculate_best_paths(santa_map):
    possible_routes = itertools.permutations(santa_map.keys())
    best_distance = 99999999999
    for route in possible_routes:
        # print(route)
        distance = 0
        for index in range(1, len(route)):
            additional_distance = santa_map[route[index - 1]].get(route[index])
            if additional_distance is None:
                break
            else:
                distance += additional_distance
        if distance < best_distance:
            best_distance = distance
            print(route)

    return best_distance

def calculate_worst_paths(santa_map):
    possible_routes = itertools.permutations(santa_map.keys())
    best_distance = 0
    for route in possible_routes:
        # print(route)
        distance = 0
        for index in range(1, len(route)):
            additional_distance = santa_map[route[index - 1]].get(route[index])
            if additional_distance is None:
                break
            else:
                distance += additional_distance
        if distance > best_distance:
            best_distance = distance
            print(route)

    return best_distance


if __name__ == '__main__':
    santa_map = route_parser('test_input.txt')

    print(calculate_best_paths(santa_map))
    print(calculate_worst_paths(santa_map))