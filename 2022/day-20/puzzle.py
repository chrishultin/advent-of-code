from collections import deque


def parser(input_file_name: str):
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            yield int(line.strip())

def part_one(inputs):
    current_state = list(inputs)

    indices = deque(range(len(current_state)))
    numbers = deque(current_state)

    for num_index in range(len(current_state)):
        # Locate the item by its index
        # Will match with position in `numbers`
        location = indices.index(num_index)

        # Rotate to put the `location` on the left side
        numbers.rotate(-location)
        indices.rotate(-location)

        current_number = numbers.popleft()
        current_index = indices.popleft()

        # Rotate in the opposite direction of the number
        numbers.rotate(-current_number)
        indices.rotate(-current_number)

        numbers.appendleft(current_number)
        indices.appendleft(current_index)

    location = numbers.index(0)
    total = 0
    for i in [location + 1000, location + 2000, location + 3000]:
        total += numbers[i%len(numbers)]

    print(total)

def part_two(inputs):
    current_state = [811589153 * i for i in inputs]

    indices = deque(range(len(current_state)))
    numbers = deque(current_state)
    for i in range(0, 10):
        for num_index in range(len(current_state)):
            # Locate the item by its index
            # Will match with position in `numbers`
            location = indices.index(num_index)

            # Rotate to put the `location` on the left side
            numbers.rotate(-location)
            indices.rotate(-location)

            current_number = numbers.popleft()
            current_index = indices.popleft()

            # Rotate in the opposite direction of the number
            numbers.rotate(-current_number)
            indices.rotate(-current_number)

            numbers.appendleft(current_number)
            indices.appendleft(current_index)

    location = numbers.index(0)
    total = 0
    for i in [location + 1000, location + 2000, location + 3000]:
        total += numbers[i % len(numbers)]

    print(total)
if __name__ == '__main__':
    # part_one(parser('input.txt'))
    part_two(parser('input.txt'))