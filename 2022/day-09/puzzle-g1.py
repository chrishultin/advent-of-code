INPUT_FILE = 'input_2.txt'

def calculate_distance(head_pos: tuple, tail_pos: tuple) -> float:
    x_distance = head_pos[0] - tail_pos[0]
    y_distance = head_pos[1] - tail_pos[1]

    return abs((x_distance * x_distance) + (y_distance * y_distance))

def tail_must_move(head_pos: tuple, tail_pos: tuple) -> bool:
    if head_pos[0] not in range(tail_pos[0] - 1, tail_pos[0] + 2):
        return True
    if head_pos[1] not in range(tail_pos[1] - 1, tail_pos[1] + 2):
        return True
    return False

def calculate_tail_position(head_pos: tuple, tail_pos: tuple) -> tuple:
    closest_position = tail_pos
    closest_distance = calculate_distance(head_pos, tail_pos)
    possible_moves = [
        (tail_pos[0]    , tail_pos[1] - 1),
        (tail_pos[0]    , tail_pos[1] + 1),
        (tail_pos[0] + 1, tail_pos[1] - 1),
        (tail_pos[0] + 1, tail_pos[1]),
        (tail_pos[0] + 1, tail_pos[1] + 1),
        (tail_pos[0] - 1, tail_pos[1] - 1),
        (tail_pos[0] - 1, tail_pos[1]),
        (tail_pos[0] - 1, tail_pos[1] + 1),
    ]
    for position in possible_moves:
        distance = calculate_distance(head_pos, position)
        if distance < closest_distance:
            closest_position = position
            closest_distance = distance

    return closest_position

instructions = []
with open(INPUT_FILE, 'r') as input_file:
    for line in input_file.readlines():
        direction, distance = line.strip().split(' ')
        instructions.append((direction, int(distance)))

tail_positions = {(0, 0)}

ROPE_LENGTH = 10

rope = []
for i in range(0, ROPE_LENGTH):
    rope.append((0,0))

for direction, distance in instructions:
    for i in range(0, distance):
        if direction == 'U':
            rope[0] = (rope[0][0], rope[0][1] + 1)
        if direction == 'D':
            rope[0] = (rope[0][0], rope[0][1] - 1)
        if direction == 'L':
            rope[0] = (rope[0][0] - 1, rope[0][1])
        if direction == 'R':
            rope[0] = (rope[0][0] + 1, rope[0][1])

        for i in range(1, len(rope)):
            is_tail = (i == (len(rope) - 1))
            must_move = tail_must_move(rope[i - 1], rope[i])
            if is_tail and must_move:
                rope.append(rope[i])
            if must_move:
                rope[i] = calculate_tail_position(rope[i - 1], rope[i])


print(len(rope))
print(rope)
