import json
import typing


def part_one_recursive(input_data: typing.Union[typing.List, typing.Dict, int]) -> int:
    if isinstance(input_data, int):
        return input_data
    if isinstance(input_data, typing.Dict):
        total_value = 0
        for i in input_data.values():
            total_value += part_one_recursive(i)
        return total_value
    if isinstance(input_data, typing.List):
        total_value = 0
        for i in input_data:
            total_value += part_one_recursive(i)
        return total_value
    return 0


def part_two_recursive(input_data: typing.Union[typing.List, typing.Dict, int]) -> int:
    if isinstance(input_data, int):
        return input_data
    if isinstance(input_data, typing.Dict):
        total_value = 0
        if 'red' not in input_data.values():
            for i in input_data.values():
                total_value += part_two_recursive(i)
        return total_value
    if isinstance(input_data, typing.List):
        total_value = 0
        for i in input_data:
            total_value += part_two_recursive(i)
        return total_value
    return 0


if __name__ == '__main__':
    TEST_CASES = [
        ([1,2,3], 6),
        ({"a":2,"b":4}, 6),
        ([[[3]]], 3),
        ({"a":{"b":4},"c":-1}, 3),
        ({"a":[-1,1]}, 0),
        ([-1,{"a":1}], 0),
        ([], 0),
        ({}, 0)
    ]
    for input, expected in TEST_CASES:
        assert part_one_recursive(input) == expected
    print('P1 TESTS PASSED, ATTEMPTING PROBLEM')

    with open('input.txt') as input_file:
        input_data = json.load(input_file)
    print(part_one_recursive(input_data))

    P2_TEST_CASES = [
        ([1,2,3], 6),
        ([1,{"c":"red","b":2},3], 4),
        ({"d":"red","e":[1,2,3,4],"f":5}, 0),
        ([1,"red",5], 6)
    ]
    for input, expected in P2_TEST_CASES:
        actual = part_two_recursive(input)
        assert actual == expected
    print('P2 TESTS PASSED, ATTEMPTING PROBLEM')
    print(part_two_recursive(input_data))