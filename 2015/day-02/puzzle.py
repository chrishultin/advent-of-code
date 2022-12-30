def calculate_wrapping_paper(length: int, width: int, height: int) -> int:
    sides = sorted([
        width * height,
        width * length,
        length * height
    ])
    totalArea = (sides[0] * 3) + ((sides[1] + sides[2]) * 2)
    return totalArea

def calculate_ribbon(length: int, width: int, height: int) -> int:
    sides = sorted([
        length,
        width,
        height
    ])
    wrap = sum(sides[0:2]) * 2
    bow = length * width * height
    return wrap + bow

def puzzle_1(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        total_paper = 0
        for line in input_file.readlines():
            length, width, height = line.strip().split('x')
            length = int(length)
            width = int(width)
            height = int(height)
            total_paper += calculate_wrapping_paper(length, width, height)
    print(total_paper)

def puzzle_2(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        total_ribbon = 0
        for line in input_file.readlines():
            length, width, height = line.strip().split('x')
            length = int(length)
            width = int(width)
            height = int(height)
            total_ribbon += calculate_ribbon(length, width, height)
    print(total_ribbon)


if __name__ == '__main__':
    test_inputs = [
        ((2,3,4), 58),
        ((1,1,10), 43)
    ]
    for instruction, result in test_inputs:
        assert calculate_wrapping_paper(*instruction) == result

    # puzzle_1('input.txt')
    test_inputs = [
        ((2,3,4), 34),
        ((1,1,10), 14)
    ]
    for instruction, result in test_inputs:
        assert calculate_ribbon(*instruction) == result

    puzzle_2('input.txt')