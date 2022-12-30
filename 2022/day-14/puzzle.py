class PartOneSimulator:
    def __init__(self, rocks: list[list[int]]):
        self.state = []
        self.current_sand = (500, 0)
        self.prev_path = [(500, 0)]
        self.floor = 0
        for x in range(0, 1000):
            self.state.append([])
            for y in range(0, 1000):
                self.state[x].append('.')

        for rock in rocks:
            self.state[rock[0]][rock[1]] = '#'
            if rock[1] > self.floor:
                self.floor = rock[1]

        # build floor
        for x in range(0, 1000):
            self.state[x][self.floor + 2] = '#'

    def display_state(self):
        for y in range(0, 175):
            print(''.join([self.state[x][y] for x in range(0, 1000)]))
        print(" ")

    def count_sand(self):
        sand = 0
        for row in self.state:
            for cell in row:
                if cell == 'o':
                    sand += 1
        return sand

    def simulate_round(self, floor = 1000):
        # self.display_state()
        # print(self.prev_path)
        if self.current_sand is None:
            for index, location in enumerate(reversed(self.prev_path)):
                if self.state[location[0]][location[1]] == '.':
                    self.current_sand = location
                    self.prev_path = list(reversed(self.prev_path))
                    self.prev_path = self.prev_path[:index]
                    break
            else:
                self.current_sand = (500, 0)

        #move sand vertically as much as possible

        for i in range(self.current_sand[1], 1000):
            if self.state[self.current_sand[0]][i] in ['#', 'o']:
                self.current_sand = (self.current_sand[0], i - 1)
                # Check diagonal left
                if self.state[self.current_sand[0] - 1][i] not in ['#', 'o']:
                    self.prev_path.append(self.current_sand)
                    self.current_sand = (self.current_sand[0] - 1, i)
                    return True

                # Check diagonal right
                if self.state[self.current_sand[0] + 1][i] not in ['#', 'o']:
                    self.prev_path.append(self.current_sand)
                    self.current_sand = (self.current_sand[0] + 1, i)
                    return True

                # Store sand in state and set current_sand to None
                self.state[self.current_sand[0]][self.current_sand[1]] = 'o'
                if self.current_sand == (500, 0):
                    return False
                self.current_sand = None
                return True


        else:
            print('did the sand fall off?')

    @staticmethod
    def create_segment(first, second):
        if first[0] == second[0]:
            start, finish = sorted([first[1], second[1]])
            return [(first[0], i)for i in range(start, finish + 1)]

        elif first[1] == second[1]:
            start, finish = sorted([first[0], second[0]])
            return [(i, first[1])for i in range(start, finish + 1)]

def to_int_coord(input: list[str]):
    return [int(i) for i in input]

if __name__ == '__main__':
    input_contents = []
    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip()
            components = line.split(' -> ')
            input_contents.append([to_int_coord(i.split(',')) for i in components])

    part_one_lines = []
    for line in input_contents:
        for i in range(0, len(line) - 1):
            part_one_lines.extend(PartOneSimulator.create_segment(line[i], line[i+1]))

    part_one = PartOneSimulator(part_one_lines)
    rounds = 0
    print(part_one.floor)

    #part 2
    while part_one.simulate_round():
        rounds += 1
        # print(f'Keep going! {rounds}')

    print(part_one.count_sand())
