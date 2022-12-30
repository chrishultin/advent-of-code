import itertools


def look_and_say(input_string: str) -> str:
    return ''.join(f'{len(list(v))}{k}' for k,v in itertools.groupby(input_string))

if __name__ == '__main__':
    TEST_CASES = [
        ('1', '11'),
        ('11', '21'),
        ('21', '1211'),
        ('1211', '111221'),
        ('111221', '312211')
    ]
    for input, expected in TEST_CASES:
        print(f'input: {input}')
        output = look_and_say(input)
        print(f'output: {output} expected: {expected}')
        assert output == expected

    input_string = "1321131112"
    # for i in range(0, 40):
    #     input_string = look_and_say(input_string)
    #
    # part_one = str(len(input_string))
    # print(f'part one: {part_one}')
    part_two_input = input_string
    for i in range(0, 50):
        print(i)
        part_two_input = look_and_say(part_two_input)

    print(f'part two: {len(part_two_input)}')