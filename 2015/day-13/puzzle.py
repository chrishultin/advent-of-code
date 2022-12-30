import itertools
import typing

POSNEG = {'gain': 1, 'lose': -1}

def parser(input_file_name: str) -> typing.Dict:
    value_map = {}
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().split(' ')
            source_name = line[0]
            if source_name not in value_map:
                value_map[source_name] = {}
            dest_name = line[-1][:-1]
            gainlose = POSNEG[line[2]]
            happy_value = int(line[3])
            value_map[source_name][dest_name] = gainlose * happy_value

    return value_map

def part_one(input_data):
    options = itertools.permutations(input_data.keys())
    max_score = 0
    for seating in options:
        print(seating)
        score = 0
        for i in range(0, len(seating)):
            score += input_data.get(seating[i], {}).get(seating[(i+1)%len(seating)], 0)
            score += input_data.get(seating[i], {}).get(seating[(i-1)%len(seating)], 0)
        if score > max_score:
            max_score = score
    print(max_score)

if __name__ == '__main__':
    input_data = parser('input.txt')

    part_one(input_data)

    part_two_data = input_data
    part_two_data['Me'] = {}
    part_one(part_two_data)