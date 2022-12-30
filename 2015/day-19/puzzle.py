import collections


def lazy_parser(input_file_name):
    permutation_map = {}
    with open(input_file_name) as input_file:
        line = input_file.readline().strip()
        while line != "":
            line = line.split(' => ')
            permutation_map[line[0]] = permutation_map.get(line[0], []) + [line[1]]
            line = input_file.readline().strip()

        starting_molecule = input_file.readline().strip()
    return permutation_map, starting_molecule

def split_molecule_str(possible_elements, molecule):
    i = 0
    split_molecule = []
    while i < len(molecule):
        if molecule[i] in possible_elements \
                and i < len(molecule) - 1 \
                and molecule[i:i+2] not in possible_elements:
                split_molecule.append(molecule[i])
                i += 1
        elif molecule[i:i+2] in possible_elements:
            split_molecule.append(molecule[i:i+2])
            i += 2
        else:
            split_molecule.append(molecule[i])
            i += 1
    return split_molecule

def part_one(permutation_map, input_string):
    split_molecule = split_molecule_str(permutation_map.keys(), input_string)

    possible_combinations = set()
    for i in range(len(split_molecule)):
        if split_molecule[i] not in permutation_map:
            continue
        for substitution in permutation_map[split_molecule[i]]:
            new_molecule = split_molecule.copy()
            new_molecule[i] = substitution
            possible_combinations.add(''.join(new_molecule))

    return len(possible_combinations)

def part_two(permutation_map, target_string):
    possible_elements = list(permutation_map.keys())
    possible_elements.append('Ar')
    possible_elements.append('Rn')
    split_molecule = split_molecule_str(possible_elements, target_string)

    # Logical method, instead of iterating/recursing
    return len(split_molecule) - split_molecule.count('Rn') - split_molecule.count('Ar') - 2*split_molecule.count('Y') - 1

if __name__ == '__main__':
    input_data, starting_molecule = lazy_parser('input.txt')

    print(part_two(input_data, starting_molecule))