from dataclasses import dataclass
from typing import List


class Board:
    board_values: List[List[int]]
    bool_values: List[List[bool]]

    def __init__(self, board_values: List[List[int]]):
        self.bool_values = []
        self.board_values = board_values
        for row in range(0, len(board_values)):
            self.bool_values.append([])
            for column in range(0, len(board_values[row])):
                self.bool_values[row].append(False)

    def make_move(self, move_value: int):
        for row in range(0, len(self.board_values)):
            for column in range(0, len(self.board_values[row])):
                if self.board_values[row][column] == move_value:
                    print(f'setting {row} {column} to True')
                    print(self.board_values[row][column])
                    self.bool_values[row][column] = True

    def board_has_won(self):
        for row in range(0, len(self.bool_values)):
            row_has_won = True
            for column in range(0, len(self.bool_values[row])):
                if self.bool_values[row][column] == False:
                    row_has_won = False
            if row_has_won:
                # print(f'winning row {row}')
                return True

        for column in range(0, len(self.bool_values[0])):
            column_has_won = True
            for row in range(0, len(self.bool_values)):
                if self.bool_values[row][column] == False:
                    column_has_won = False
            if column_has_won:
                # print(f'winning column {column}')
                return True

        return False

    def unwanted_values(self):
        unwanted_values = []
        for row_index, row in enumerate(self.bool_values):
            for column_index, value in enumerate(row):
                if not value:
                    unwanted_values.append(self.board_values[row_index][column_index])
        return sum(unwanted_values)


def puzzle_1(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        moves = [int(i) for i in input_file.readline().strip().split(',')]
        boards = []
        while True:
            # Skip the first line (blank)
            board = []
            if not input_file.readline():
                break

            for i in range(0, 5):
                line = input_file.readline()
                # print(f'"{line}"')
                line_content = []
                for j in range(0, len(line), 3):
                    # print(line[j:j+3])
                    line_content.append(int(line[j:j+3]))
                # print(line_content)
                board.append(line_content)
            # print(' ')
            boards.append(Board(board))

    worst_board_index = 0
    worst_board_move = 0
    for index, move in enumerate(moves):
        for board_index, board in enumerate(boards):
            if not board.board_has_won():
                board.make_move(move)
                if board.board_has_won():
                    print(f'board {board_index + 1} has won on move {index + 1}')
                    print(board.unwanted_values())
                    print(move * board.unwanted_values())











if __name__ == '__main__':
    puzzle_1('input.txt')