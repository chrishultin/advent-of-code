def parser(input_file_name):
    aunts = {}
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().replace(':', '').split(' ')
            number = int(line[1])
            key1 = line[2]
            key1value = int(line[3][:-1])
            key2 = line[4]
            key2value = int(line[5][:-1])
            key3 = line[6]
            key3value = int(line[7])

            aunts[number] = {
                key1: key1value,
                key2: key2value,
                key3: key3value
            }
    return aunts

def part_one(match_data, aunts):
    for aunt_num, i in aunts.items():
        matching_values = 0
        for key, value in i.items():
            if match_data[key] == value:
                matching_values += 1
        if matching_values == 3:
            print(aunt_num)

def part_two(match_data, aunts):
    for aunt_num, i in aunts.items():
        matching_values = 0
        for key, value in i.items():
            if key in ['cats', 'trees']:
                if match_data[key] < value:
                    matching_values += 1
            elif key in ['pomeranians', 'goldfish']:
                if match_data[key] > value:
                    matching_values += 1
            else:
                if match_data[key] == value:
                    matching_values += 1
        if matching_values == 3:
            print(aunt_num)

if __name__ == '__main__':
    aunts = parser('input.txt')
    match_data = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    part_two(match_data, aunts)