class LightGrid1:
    def __init__(self):
        self.grid = []

        # Init a 1000x1000 grid of False
        for x in range(0, 1000):
            self.grid.append([])
            for y in range(0, 1000):
                self.grid[x].append(False)

    def toggle(self, start_x, start_y, end_x, end_y):
        x_order = sorted([start_x, end_x])
        y_order = sorted([start_y, end_y])

        for x in range(x_order[0], x_order[1] + 1):
            for y in range(y_order[0], y_order[1] + 1):
                self.grid[x][y] = not self.grid[x][y]

    def set_state(self, start_x, start_y, end_x, end_y, state):
        x_order = sorted([start_x, end_x])
        y_order = sorted([start_y, end_y])

        for x in range(x_order[0], x_order[1] + 1):
            for y in range(y_order[0], y_order[1] + 1):
                self.grid[x][y] = state

    def count_lights(self):
        light_count = 0
        for x in range(0, 1000):
            for y in range(0, 1000):
                if self.grid[x][y]:
                    light_count += 1

        return light_count

class LightGrid2:
    def __init__(self):
        self.grid = []

        # Init a 1000x1000 grid of False
        for x in range(0, 1000):
            self.grid.append([])
            for y in range(0, 1000):
                self.grid[x].append(0)

    def toggle(self, start_x, start_y, end_x, end_y):
        x_order = sorted([start_x, end_x])
        y_order = sorted([start_y, end_y])

        for x in range(x_order[0], x_order[1] + 1):
            for y in range(y_order[0], y_order[1] + 1):
                self.grid[x][y] += 2

    def set_state(self, start_x, start_y, end_x, end_y, state):
        x_order = sorted([start_x, end_x])
        y_order = sorted([start_y, end_y])

        for x in range(x_order[0], x_order[1] + 1):
            for y in range(y_order[0], y_order[1] + 1):
                if state:
                    self.grid[x][y] += 1
                else:
                    self.grid[x][y] -= 1
                    if self.grid[x][y] < 0:
                        self.grid[x][y] = 0

    def get_brightness(self):
        light_count = 0
        for x in range(0, 1000):
            for y in range(0, 1000):
                light_count += self.grid[x][y]

        return light_count

if __name__ == '__main__':
    # grid_1 = LightGrid1()
    #
    #
    # with open('input.txt', 'r') as input_file:
    #     for line in input_file.readlines():
    #         command = line.strip().split(' ')
    #         if command[0] == 'turn':
    #             position_a = command[2].split(',')
    #             position_b = command[4].split(',')
    #             if command[1] == 'on':
    #                 grid_1.set_state(int(position_a[0]), int(position_a[1]), int(position_b[0]), int(position_b[1]), True)
    #             elif command[1] == 'off':
    #                 grid_1.set_state(int(position_a[0]), int(position_a[1]), int(position_b[0]), int(position_b[1]), False)
    #         elif command[0] == 'toggle':
    #             position_a = command[1].split(',')
    #             position_b = command[3].split(',')
    #             grid_1.toggle(int(position_a[0]), int(position_a[1]), int(position_b[0]), int(position_b[1]))
    # print(grid_1.count_lights())
    #
    grid_2 = LightGrid2()


    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            command = line.strip().split(' ')
            if command[0] == 'turn':
                position_a = command[2].split(',')
                position_b = command[4].split(',')
                if command[1] == 'on':
                    grid_2.set_state(int(position_a[0]), int(position_a[1]), int(position_b[0]), int(position_b[1]), True)
                elif command[1] == 'off':
                    grid_2.set_state(int(position_a[0]), int(position_a[1]), int(position_b[0]), int(position_b[1]), False)
            elif command[0] == 'toggle':
                position_a = command[1].split(',')
                position_b = command[3].split(',')
                grid_2.toggle(int(position_a[0]), int(position_a[1]), int(position_b[0]), int(position_b[1]))
    print(grid_2.get_brightness())
