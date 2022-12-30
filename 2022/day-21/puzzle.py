def parser(input_file_name):
    monkeys = dict()
    with open(input_file_name) as input_file:
        for line in input_file.readlines():
            line = line.strip().split(' ')
            if len(line) == 4:
                monkey = {
                    'monkeys': [line[1], line[3]],
                    'operation': line[2]
                }
                monkeys[line[0][:-1]] = monkey
            elif len(line) == 2:
                monkey = {
                    'value': int(line[1])
                }
                monkeys[line[0][:-1]] = monkey
    return monkeys

OPERATION_MAP = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: int(a/b)
}

def part_one(monkeys):
    while True:
        for monkey, monkey_details in monkeys.items():
            # Check if the monkey is already set
            if monkey_details.get('value'):
                if monkey == 'root':
                    print(monkey_details.get('value'))
                    return

                continue

            # Check if we can calculate the value
            monkey_values = [monkeys[i].get('value') for i in monkey_details['monkeys'] if monkeys[i].get('value') is not None]
            if len(monkey_values) == 2:
                monkey_details['value'] = OPERATION_MAP[monkey_details['operation']](*monkey_values)
                print(f'monkey {monkey} value now set to {monkey_details["value"]}')


def part_two(monkeys, humn_value):
    cached_values = {
        'humn': humn_value
    }
    while True:
        for monkey, monkey_details in monkeys.items():
            if monkey == 'root':
                monkey_values = [cached_values.get(i) for i in monkey_details['monkeys'] if cached_values.get(i) is not None]
                if len(monkey_values) == 2:
                    return monkey_values[0] - monkey_values[1]
            # Check if the monkey is already set
            if monkey in cached_values:
                continue
            else:
                if monkey_details.get('value') is not None:
                    cached_values[monkey] = monkey_details.get('value')
                else:
                    # Check if we can calculate the value
                    monkey_values = [cached_values.get(i) for i in monkey_details['monkeys'] if cached_values.get(i) is not None]
                    if len(monkey_values) == 2:
                        cached_values[monkey] = OPERATION_MAP[monkey_details['operation']](*monkey_values)
                        # print(f'monkey {monkey} value now set to {cached_values[monkey]}')

if __name__ == '__main__':
    monkeys = parser('input.txt')
    # part_one(monkeys)
    l = 1
    r = 10 ** 15

    bsearch_value = None
    while l + 1 < r:
        mid = (l + r) >> 1
        p2_value = part_two(monkeys, mid)

        if p2_value == 0:
            print(f'part2: {mid}')
            bsearch_value = mid
            break

        if p2_value < 0:
            r = mid
        else:
            l = mid

    for i in range(bsearch_value, 0, -1):
        if part_two(monkeys, i) != 0:
            print(i+1)
            break