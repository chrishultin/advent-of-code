import math


def snafu_to_int(snafu: str) -> int:
    VALUE_MAP = {
        '2': 2,
        '1': 1,
        '0': 0,
        '-': -1,
        '=': -2
    }
    total_value = 0
    for position,value in enumerate(reversed(snafu)):
        total_value += math.pow(5,position) * VALUE_MAP[value]

    return total_value

def int_to_snafu(input: int) -> str:
    remaining_value = input
    output = ''
    while remaining_value != 0:
        current_digit = remaining_value % 5
        if current_digit <= 2:
            output = str(int(current_digit)) + output
            remaining_value -= current_digit
        elif current_digit == 3:
            output = '=' + output
            remaining_value += 2
        elif current_digit == 4:
            output = '-' + output
            remaining_value += 1
        remaining_value = remaining_value // 5

    return output



if __name__ == '__main__':
    # total = 0
    # with open('input.txt') as input_file:
    #     for line in input_file.readlines():
    #         line = line.strip()
    #         total += snafu_to_int(line)
    # print(total)
    print(int_to_snafu(15))