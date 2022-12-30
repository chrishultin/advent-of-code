def parser(input_file_name: str):
    with open(input_file_name) as input_file:
        line = input_file.readline().strip()

    yield from line

def part_one(width: int, height: int, input):
    layers = []
    min_zeros = width * height
    checksum_layer = None
    try:
        while True:
            layer = []
            zeros = 0
            ones = 0
            twos = 0
            for y in range(height):
                line = []
                for x in range(width):
                    value = next(input)
                    line.append(value)
                    if value == '0':
                        zeros += 1
                    elif value == '1':
                        ones += 1
                    elif value == '2':
                        twos += 1
                layer.append(line)
            layers.append(layer)
            if zeros < min_zeros:
                min_zeros = zeros
                result = ones * twos
                checksum_layer = len(layers) - 1
    except:
        pass

    print(checksum_layer)
    print(result)

def part_two(width: int, height: int, input):
    layers = []
    try:
        while True:
            layer = []
            for y in range(height):
                line = []
                for x in range(width):
                    value = next(input)
                    line.append(value)
                layer.append(line)
            layers.append(layer)
    except:
        pass

    for layer in layers:
        print(layer)

    output = []
    for y in range(0, height):
        line = []
        for x in range(0, width):
            for layer in layers:
                print(x,y)
                if layer[y][x] == '2':
                    pass
                else:
                    line.append(layer[y][x])
                    break
        output.append(line)

    for line in output:
        print(''.join(line).replace('0',' '))

if __name__ == '__main__':
    part_two(25,6, parser('input.txt'))