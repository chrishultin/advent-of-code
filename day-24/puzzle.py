from collections import deque


def parser(input_file_name: str):
    grid = set()
    blizzards = {
        '^': set(),
        'v': set(),
        '<': set(),
        '>': set()
    }
    with open(input_file_name) as input_file:
        first_line = input_file.readline().strip()
        starting_position = None
        # Starting position: only "." in first row
        ending_position = None
        # Ending position: last '.' added
        for x, state in enumerate(first_line):
            if state == '.':
                grid.add(x+0j)
                starting_position = x+0j
                break
        for y, line in enumerate(input_file.readlines()):
            for x, state in enumerate(line.strip()):
                if state != '#':
                    grid.add(x + ((y+1) * 1j))
                    if state != '.':
                        blizzards[state].add(x + ((y+1) * 1j))
                    else:
                        ending_position = x + ((y+1) * 1j)

    return grid, starting_position, ending_position, blizzards

def part_one(valid_positions: set[complex], starting_position: complex, ending_position: complex, blizzards: dict[str, set[complex]]):
    DIRECTION_OFFSET_MODIFIER = {
        '^': -1j,
        'v': 1j,
        '<': -1,
        '>': 1
    }

    # BFS using queue
    queue = deque([starting_position])
    visited = set()

    time = 0
    print(valid_positions)
    while True:
        for _ in range(len(queue)):
            current_position = queue.popleft()

            if (time, current_position) in visited:
                continue

            visited.add((time, current_position))

            if current_position == ending_position:
                return (time - 1), blizzards
            # Check if we can move
            possible_moves = [
                current_position,
                current_position + 1,
                current_position - 1,
                current_position + 1j,
                current_position - 1j
            ]
            for move in possible_moves:
                if move in valid_positions:
                    # Check if move is occupied by a blizzard
                    for blizzard in blizzards.values():
                        if move in blizzard:
                            break
                    else:
                        queue.append(move)
        # move blizzards for next round
        new_blizzards: dict[str, set[complex]] = {
            '^': set(),
            'v': set(),
            '<': set(),
            '>': set()
        }
        for direction, blizzard_set in blizzards.items():
            for blizzard in blizzard_set:
                new_position = blizzard + DIRECTION_OFFSET_MODIFIER[direction]
                if new_position in valid_positions:
                    new_blizzards[direction].add(new_position)
                else:
                    if direction == '^':
                        new_position = sorted(i.imag for i in valid_positions if i.real == blizzard.real)[-1]*1j + blizzard.real
                        new_blizzards[direction].add(new_position)
                    if direction == '>':
                        new_position = sorted(i.real for i in valid_positions if i.imag == blizzard.imag)[0] + blizzard.imag * 1j
                        new_blizzards[direction].add(new_position)
                    if direction == 'v':
                        new_position = sorted(i.imag for i in valid_positions if i.real == blizzard.real)[0]*1j + blizzard.real
                        new_blizzards[direction].add(new_position)
                    if direction == '<':
                        new_position = sorted(i.real for i in valid_positions if i.imag == blizzard.imag)[-1] + blizzard.imag * 1j
                        new_blizzards[direction].add(new_position)

        blizzards = new_blizzards
        time += 1


def part_two(valid_positions: set[complex], starting_position: complex, ending_position: complex, blizzards: dict[str, set[complex]]):
    time_for_p1, p2_blizzards = part_one(valid_positions, starting_position, ending_position, blizzards)
    time_for_p2, p3_blizzards = part_one(valid_positions, ending_position, starting_position, p2_blizzards)
    time_for_p3, _ = part_one(valid_positions,starting_position,ending_position,p3_blizzards)

    return time_for_p1+time_for_p2+time_for_p3 + 2

if __name__ == '__main__':
    # print(part_one(*parser('input.txt'))[0])
    print(part_two(*parser('input.txt')))