
def puzzle_1(input_file_name: str):
    monkeys = []
    monkey_counts = []
    with open(input_file_name, 'r') as input_file:
        while True:
            monkey = {}

            line = input_file.readline().strip()
            monkey_id = line[1][:-1]

            line = input_file.readline().strip().split(': ')
            monkey['items'] = [int(i) for i in line[1].split(', ')]

            line = input_file.readline().strip().split(': ')
            monkey['operation'] = line[1][line[1].find('=')+ 2:]

            line = input_file.readline().strip().split(': ')
            monkey['divisor'] = int(line[1].split(' ')[2])

            line = input_file.readline().strip().split(': ')
            monkey['true'] = int(line[1].split(' ')[3])

            line = input_file.readline().strip().split(': ')
            monkey['false'] = int(line[1].split(' ')[3])

            monkeys.append(monkey)
            monkey_counts.append(0)
            if not input_file.readline():
                break

    print(monkeys)

    for round in range(0, 20):
        for index, monkey in enumerate(monkeys):
            for i in range(0, len(monkey['items'])):
                item = monkey['items'][i]
                new_value = eval(monkey['operation'], {'old': item})
                new_value = int(new_value / 3)
                if new_value % monkey['divisor'] == 0:
                    print(f'throwing to {monkey["true"]}')
                    next_monkey = monkey["true"]
                else:
                    print(f'throwing to {monkey["false"]}')
                    next_monkey = monkey["false"]
                monkey_counts[index] += 1

                monkeys[next_monkey]['items'].append(new_value)
            monkey['items'] = []
        print(monkeys)

    highest_values = sorted(monkey_counts, reverse=True)[0:2]
    return highest_values[0] * highest_values[1]

def puzzle_2(input_file_name: str):
    monkeys = []
    monkey_counts = []
    with open(input_file_name, 'r') as input_file:
        while True:
            monkey = {}

            line = input_file.readline().strip()
            monkey_id = line[1][:-1]

            line = input_file.readline().strip().split(': ')
            monkey['items'] = [int(i) for i in line[1].split(', ')]

            line = input_file.readline().strip().split(': ')
            monkey['operation'] = line[1][line[1].find('=')+ 2:]

            line = input_file.readline().strip().split(': ')
            monkey['divisor'] = int(line[1].split(' ')[2])

            line = input_file.readline().strip().split(': ')
            monkey['true'] = int(line[1].split(' ')[3])

            line = input_file.readline().strip().split(': ')
            monkey['false'] = int(line[1].split(' ')[3])

            monkeys.append(monkey)
            monkey_counts.append(0)
            if not input_file.readline():
                break
    for round in range(0, 10000):
        print(round)
        for index, monkey in enumerate(monkeys):
            for i in range(0, len(monkey['items'])):
                item = monkey['items'][i]
                new_value = eval(monkey['operation'], {'old': item})
                if new_value % monkey['divisor'] == 0:
                    # print(f'throwing to {monkey["true"]}')
                    next_monkey = monkey["true"]
                else:
                    # print(f'throwing to {monkey["false"]}')
                    next_monkey = monkey["false"]
                monkey_counts[index] += 1

                monkeys[next_monkey]['items'].append(new_value)
            monkey['items'] = []


    highest_values = sorted(monkey_counts, reverse=True)[0:2]
    return highest_values[0] * highest_values[1]

if __name__ == '__main__':
    # print(puzzle_1('test_input.txt'))
    # print(puzzle_1('input.txt'))

    print(puzzle_2('test_input.txt'))