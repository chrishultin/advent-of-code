from collections import deque as queue

def get_height(input: str):
    return ord(input) - ord('a')

def is_valid(position, board, previous_moves):
    if position in previous_moves:
        return False
    if position[0] < 0 or position[0] >= len(board):
        return False
    if position[1] < 0 or position[1] >= len(board[0]):
        return False
    return True

def get_available_moves(position: list[int], board: list[list[int]], previous_moves: list[list[int]]):
    current_position_value = board[position[0]][position[1]]
    possible_moves = [
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
        (position[0]    , position[1] + 1),
        (position[0]    , position[1] - 1),
    ]
    valid_moves = []
    for move in possible_moves:
        if is_valid(move, board, previous_moves):
            value = board[move[0]][move[1]]
            if value <= current_position_value + 1:
                valid_moves.append(move)

    return valid_moves


def bfs(board, start_position, destination):
    q = queue([[start_position]])
    seen = set([start_position])

    while q:
        path = q.popleft()
        if destination == path[-1]:
            return path
        for possible_move in get_available_moves(path[-1], board, path):
            if possible_move not in seen:
                q.append(path + [possible_move])
                seen.add(possible_move)


def puzzle_1(input_file_name: str):
    board = []
    start_position = []
    end_position = []
    with open(input_file_name, 'r') as input_file:
        for row, line in enumerate(input_file.readlines()):
            row_contents = []
            for column, char in enumerate(line.strip()):
                height = get_height(char)
                if height == -14:
                    start_position = (row, column)
                    height = 0
                elif height == -28:
                    end_position = (row, column)
                    height = get_height('z')
                row_contents.append(height)
            board.append(row_contents)
    print(start_position)
    print(end_position)
    moves = bfs(board, start_position, end_position)
    print(len(moves) - 1)

def puzzle_2(input_file_name: str):
    board = []
    start_positions = []
    end_position = []
    with open(input_file_name, 'r') as input_file:
        for row, line in enumerate(input_file.readlines()):
            row_contents = []
            for column, char in enumerate(line.strip()):
                height = get_height(char)
                if height == 0:
                    start_positions.append((row, column))
                elif height == -28:
                    end_position = (row, column)
                    height = get_height('z')
                row_contents.append(height)
            board.append(row_contents)
    print(start_positions)
    print(end_position)
    min_moves = 9999999
    for start_position in start_positions:
        moves = bfs(board, start_position, end_position)
        if moves is not None:
            moves = len(moves)
            if moves < min_moves:
                min_moves = moves
    print(min_moves - 1)


if __name__ == '__main__':
    puzzle_2('input.txt')