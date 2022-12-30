from typing import Generator


def gas_cycle_iterator(input_file_name: str) -> Generator[int, None, None]:
    INPUT_MAP = {
        '<': -1,
        '>': 1
    }
    with open(input_file_name, 'r') as input_file:
        input_string = input_file.readline().strip()

    while True:
        for index, character in enumerate(input_string):
            yield (index, INPUT_MAP[character])

def rock_iterator() -> Generator[list, None, None]:
    ROCK_LIST = [
        (0, 1, 2, 3),                # -
        (1, 0+1j, 1+1j, 2+1j, 1+2j), # +
        (0, 1, 2, 2+1j, 2+2j),       # _|
        (0, 0+1j, 0+2j, 0+3j),       # |
        (0, 1, 0+1j, 1+1j)           # []
    ]
    while True:
        for index, rock in enumerate(ROCK_LIST):
            yield (index, rock)

def position_is_empty(rock: complex, tower):
    # check if real/x component is in range(0, 7) for all points in rock
    return (rock.real in range(0, 7)
            and rock.imag > 0
            and rock not in tower)

def check_rock_position(position, direction, rock, tower):
    return all(position_is_empty(position + direction + rock_piece, tower) for rock_piece in rock)

def part_one(gas_jets, rocks):
    height = 0
    tower = set()
    height_cache = dict()
    for i in range(int(1e12)):
        rock_index, rock = next(rocks)
        jet_index, gas_jet_direction = next(gas_jets)

        current_position = complex(2, height + 4)

        cache_key = rock_index,jet_index
        if cache_key in height_cache:
            prev_move, prev_height = height_cache[cache_key]
            loops, remainder = divmod(int(1e12) - i, prev_move - i)
            if not remainder:
                print(height + ((prev_height - height)*loops))
                break
        else:
            height_cache[cache_key] = i,height

        while True:
            # Check if we can move to the side
            if check_rock_position(current_position, gas_jet_direction, rock, tower):
                current_position += gas_jet_direction
            # Check if we can move down
            if check_rock_position(current_position, -1j, rock, tower):
                current_position += -1j
                jet_index, gas_jet_direction = next(gas_jets)
            else:
                break

        tower.update({current_position + r for r in rock})
        height = max(height, *[(current_position + r).imag for r in rock])

if __name__ == '__main__':
    gas_jets = gas_cycle_iterator('input.txt')
    part_one(gas_jets, rock_iterator())