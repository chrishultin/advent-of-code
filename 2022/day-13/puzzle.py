def compare_lists(left: list, right: list):
    for leftItem, rightItem in zip(left, right):
        result = compare_items(leftItem, rightItem)
        if result is not None:
            return result


    if len(left) < len(right):
        return True
    elif len(right) < len(left):
        return False

    return None

def compare_int(left: int, right: int):
    if left == right:
        return None
    if left < right:
        return True
    if left > right:
        return False

def compare_items(left, right):
    if isinstance(left, int) and isinstance(right, int):
        # print(f'comparing ints {left} {right}')
        response = compare_int(left, right)
        # print(response)
        if response is not None:
            return response
    if isinstance(left, list) and isinstance(right, list):
        response = compare_lists(left, right)
        if response is not None:
            return response
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
        response = compare_lists(left, right)
        if response is not None:
            return response
    if isinstance(right, int) and isinstance(left, list):
        right = [right]
        response = compare_lists(left, right)
        if response is not None:
            return response




def puzzle_1(input_file_name):
    with open(input_file_name, 'r') as input_file:
        index = 0
        indexSum = 0
        while True:
            index += 1
            print(index)
            left = eval(input_file.readline().strip())
            right = eval(input_file.readline().strip())

            # print(left)
            # print(right)
            if (compare_lists(left, right)):
                indexSum += index
            if not input_file.readline():
                break
        print(indexSum)

def puzzle_2(input_file_name):
    all_packets = []
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            if line.strip() != "":
                all_packets.append(eval(line.strip()))

        all_packets.append([[2]])
        all_packets.append([[6]])

        while True:
            outOfOrder = False
            for i in range(0, len(all_packets) - 1):
                left = all_packets[i]
                right = all_packets[i + 1]

                result = compare_lists(left, right)
                if result is False:
                    outOfOrder = True
                    all_packets[i] = right
                    all_packets[i+1] = left
            if not outOfOrder:
                break

        twoIndex = 0
        sixIndex = 0
        for i, packet in enumerate(all_packets):
            if packet == [[6]]:
                sixIndex = i + 1
            if packet == [[2]]:
                twoIndex = i + 1

        print(twoIndex * sixIndex)


if __name__ == '__main__':
    puzzle_2('input.txt')