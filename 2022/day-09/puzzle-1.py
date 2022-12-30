INPUT_FILE = 'input.txt'

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

head_positions = {(0, 0)}
tail_positions = {(0, 0)}

head = (0,0)
tail = (0,0)
for direction, distance in instructions:
    for i in range(0, distance):
        if direction == 'U':
            head = (head[0], head[1] + 1)
        if direction == 'D':
            head = (head[0], head[1] - 1)
        if direction == 'L':
            head = (head[0] - 1, head[1])
        if direction == 'R':
            head = (head[0] + 1, head[1])


        head_positions.add(head)
        if tail_must_move(head, tail):
            tail = calculate_tail_position(head, tail)
            tail_positions.add(tail)

print(len(tail_positions))
