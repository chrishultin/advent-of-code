def puzzle_1(initial_state: list[int], rounds: int = 80):
    state = initial_state
    for i in range(0, rounds):
        print(state)
        new_fish = []
        for j in range(0, len(state)):
            if state[j] == 0:
                state[j] = 7
                new_fish.append(8)
            state[j] -= 1
        state.extend(new_fish)

    return state

def puzzle_2(initial_state: list[int], rounds=256):
    counts = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
    }
    for value in initial_state:
        counts[str(value)] += 1

    for round in range(0, rounds):
        print(counts)
        new_fish = counts['0']
        for i in range(0, 8):
            counts[str(i)] = counts[str(i + 1)]
        counts['6'] += new_fish
        counts['8'] = new_fish

    return counts

if __name__ == '__main__':
    with open('test_input.txt','r') as input_file:
        initial_state = [int(i) for i in input_file.readline().split(',')]
    fish_counts = puzzle_2(initial_state, rounds=256).values()
    print(sum(fish_counts))
