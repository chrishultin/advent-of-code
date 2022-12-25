from typing import Union, Generator


class TwoDimensionGrid:
    def __init__(self):
        self.positions: dict[complex,str] = dict()
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None

    def add_position(self, x_value: int, y_value:int, value: str):
        self.positions[x_value+(y_value*1j)] = value

        if self.min_x is None or x_value < self.min_x:
            self.min_x = x_value

        if self.max_x is None or x_value > self.max_x:
            self.max_x = x_value

        if self.min_y is None or y_value < self.min_y:
            self.min_y = y_value

        if self.max_y is None or y_value > self.max_y:
            self.max_y = y_value

    def render(self):
        for y in range(self.min_y, self.max_y + 1):
            print(''.join([self.positions.get(x+(y*1j),' ') for x in range(self.min_x, self.max_x + 1)]))

    def get_row(self, y_value) -> Generator[tuple[int, int], None, None]:
        keys = [(int(i.real), int(i.imag),) for i in self.positions.keys() if i.imag == y_value]
        yield from sorted(keys)

    def get_column(self, x_value) -> Generator[tuple[int, int], None, None]:
        keys = [(int(i.real), int(i.imag),) for i in self.positions.keys() if i.real == x_value]
        yield from sorted(keys)

    def get_position(self, x_value, y_value) -> Union[str, None]:
        return self.positions.get(x_value+(y_value*1j))

    def set_position(self, x_value: int, y_value: int, new_value: str):
        if self.get_position(x_value, y_value):
            self.positions[x_value+(y_value*1j)] = new_value

class TwoDimensionGridPoint:
    def __init__(self, x_value: int, y_value: int):
        self.x = x_value
        self.y = y_value
