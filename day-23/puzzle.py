
def parser(input_file_name: str):
    elves = set()
    with open(input_file_name) as input_file:
        for y_index, line in enumerate(input_file.readlines()):
            line = line.strip()
            for x_index, value in enumerate(line):
                if value == '#':
                    elves.add(x_index+(y_index*1j))

    return elves

def print_elves(elves, max_value=5):
    for y in range(0, max_value):
        row = ''
        for x in range(0, max_value):
            if (x+(y*1j)) in elves:
                row = row+"#"
            else:
                row = row + "."
        print(row)

def get_part_one_move(all_elves, current_elf, direction_order):
    for i in direction_order:
        if i == 'n':
            check_positions = [(current_elf - 1j - 1),
                               (current_elf - 1j),
                               (current_elf - 1j + 1)]
            next_position = (current_elf - 1j)
        elif i == 's':
            check_positions = [(current_elf + 1j - 1),
                               (current_elf + 1j),
                               (current_elf + 1j + 1)]
            next_position = (current_elf + 1j)
        elif i == 'w':
            check_positions = [(current_elf - 1 - 1j),
                               (current_elf - 1),
                               (current_elf - 1 + 1j), ]
            next_position = (current_elf - 1)
        elif i == 'e':
            check_positions = [(current_elf + 1 - 1j),
                               (current_elf + 1),
                               (current_elf + 1 + 1j), ]
            next_position = (current_elf + 1)
        for check_position in check_positions:
            if check_position in all_elves:
                break
        else:
            return next_position
    return current_elf

def get_adjacent_positions(elf_position):
    return [
        elf_position - 1 - 1j,
        elf_position - 1,
        elf_position - 1 + 1j,
        elf_position + 1j,
        elf_position + 1 + 1j,
        elf_position + 1,
        elf_position + 1 - 1j,
        elf_position - 1j
    ]

def part_one(input_file_name):
    elves = parser(input_file_name)
    print_elves(elves, 10)

    round = 1
    direction_order = ['n','s','w','e']
    while True:
        proposed_moves = {}
        remain_still = set()
        for elf_position in elves:
            for position in get_adjacent_positions(elf_position):
                if position in elves:
                    new_move = get_part_one_move(elves, elf_position, direction_order)
                    current_proposed = proposed_moves.get(new_move, [])
                    current_proposed.append(elf_position)
                    proposed_moves[new_move] = current_proposed
                    break
            else:
                remain_still.add(elf_position)
        direction_order = direction_order[1:] + [direction_order[0]]

        new_elves = remain_still.copy()
        for destination, elves_info in proposed_moves.items():
            if len(elves_info) == 1:
                # print(f'{elves_info[0][0]} can move - {destination}')
                new_elves.add(destination)
            else:
                for i in elves_info:
                    # print(f'{i[0]} cant move')
                    new_elves.add(i)

        if len(remain_still) == len(elves):
            print(elves)
            return new_elves
        else:
            elves = new_elves
            if round % 10 == 0:
                print_elves(elves, 14)
                return elves
            round += 1

def part_two(input_file_name):
    elves = parser(input_file_name)
    print_elves(elves, 10)

    round = 1
    direction_order = ['n','s','w','e']
    while True:
        proposed_moves = {}
        remain_still = set()
        for elf_position in elves:
            for position in get_adjacent_positions(elf_position):
                if position in elves:
                    new_move = get_part_one_move(elves, elf_position, direction_order)
                    current_proposed = proposed_moves.get(new_move, [])
                    current_proposed.append(elf_position)
                    proposed_moves[new_move] = current_proposed
                    break
            else:
                remain_still.add(elf_position)
        direction_order = direction_order[1:] + [direction_order[0]]

        new_elves = remain_still.copy()
        for destination, elves_info in proposed_moves.items():
            if len(elves_info) == 1:
                # print(f'{elves_info[0][0]} can move - {destination}')
                new_elves.add(destination)
            else:
                for i in elves_info:
                    # print(f'{i[0]} cant move')
                    new_elves.add(i)

        if len(remain_still) == len(elves):
            print(elves)
            return round
        else:
            elves = new_elves
            # if round % 10 == 0:
            #     print_elves(elves, 14)
            #     return elves
            round += 1


if __name__ == '__main__':
    # p1_final_positions = part_one('input.txt')
    # max_x = max(*[v.real for v in p1_final_positions])
    # min_x = min(*[v.real for v in p1_final_positions])
    # max_y = max(*[v.imag for v in p1_final_positions])
    # min_y = min(*[v.imag for v in p1_final_positions])
    #
    # print(f'{max_x} {min_x} {max_y} {min_y}')
    # total_area = (1 + max_x - min_x) * (1 + max_y - min_y)
    # print(total_area)
    # print(len(p1_final_positions))
    # print(total_area - len(p1_final_positions))

    print(part_two('input.txt'))