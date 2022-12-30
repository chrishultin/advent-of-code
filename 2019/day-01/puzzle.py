def calculate_part_one_fuel(mass: int) -> int:
    return int(mass / 3) - 2

def calculate_part_one(input_file_name: str):
    total = 0
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            line_value = int(line.strip())
            total += calculate_part_one_fuel(line_value)

    return total

def calculate_part_two(input_file_name: str) -> int:
    total = 0
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            input_mass = int(line.strip())
            fuel_required = calculate_part_one_fuel(input_mass)
            total += fuel_required
            while fuel_required > 0:
                fuel_required = calculate_part_one_fuel(fuel_required)
                if fuel_required > 0:
                    total += fuel_required

    return total
if __name__ == '__main__':
    part_one_tests = [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
    ]
    for test_input, expected_output in part_one_tests:
        assert calculate_part_one_fuel(test_input) == expected_output

    p1_ans = calculate_part_one('input.txt')
    print(f'2019 Day 1 P1: {p1_ans}')

    p2_ans = calculate_part_two('input.txt')
    print(f'2019 Day 1 P2: {p2_ans}')