from collections import Counter

def puzzle_1(input_file_name: str):
    file_contents = []
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            file_contents.append(line.strip())

    gamma_values = []
    epsilon_values = []
    for i in range(0, len(file_contents[0])):
        values = [line[i] for line in file_contents]
        occurrence_count = Counter(values).most_common()
        gamma_values.append(occurrence_count[0][0])
        epsilon_values.append(occurrence_count[1][0])

    print(gamma_values)
    gamma = int(''.join(gamma_values), 2)
    print(epsilon_values)
    epsilon = int(''.join(epsilon_values), 2)

    print(gamma * epsilon)

def puzzle_2(input_file_name: str):
    file_contents = []
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            file_contents.append(line.strip())

    oxygen_rating_values = file_contents.copy()
    co2_rating_values = file_contents.copy()
    for i in range(0, len(file_contents[0])):
        oxygen_occurrence_count = Counter([line[i] for line in oxygen_rating_values]).most_common()
        co2_occurence_count = Counter([line[i] for line in co2_rating_values]).most_common()

        # oxygen rating
        if len(oxygen_rating_values) > 1:
            if oxygen_occurrence_count[0][1] == oxygen_occurrence_count[1][1]:
                most_common_value = '1'
            else:
                most_common_value = oxygen_occurrence_count[0][0]

            oxygen_rating_values = [v for v in oxygen_rating_values if v[i] == most_common_value]

        # co2 rating

        if len(co2_rating_values) > 1:
            if co2_occurence_count[0][1] == co2_occurence_count[1][1]:
                least_common_value = '0'
            else:
                least_common_value = co2_occurence_count[1][0]
            co2_rating_values = [v for v in co2_rating_values if v[i] == least_common_value]

    print(oxygen_rating_values)
    print(co2_rating_values)

    print(oxygen_rating_values)
    gamma = int(''.join(oxygen_rating_values), 2)
    print(co2_rating_values)
    epsilon = int(''.join(co2_rating_values), 2)

    print(gamma * epsilon)

if __name__ == '__main__':
    puzzle_2('input.txt')