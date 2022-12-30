import itertools

import advent_of_code.intcode_sim as intcode

# program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def calculate_part_one(value_one, value_two, value_three, value_four, value_five, program):
    scheduler = intcode.IntCodeScheduler()

    scheduler.add_vm('a', program)
    scheduler.add_vm('b', program)
    scheduler.add_vm('c', program)
    scheduler.add_vm('d', program)
    scheduler.add_vm('e', program)
    scheduler.vms['a'].input.append(value_one)
    scheduler.vms['a'].input.append(0)
    scheduler.vms['b'].input.append(value_two)
    scheduler.vms['c'].input.append(value_three)
    scheduler.vms['d'].input.append(value_four)
    scheduler.vms['e'].input.append(value_five)
    scheduler.add_connection('b', 'a')
    scheduler.add_connection('c', 'b')
    scheduler.add_connection('d', 'c')
    scheduler.add_connection('e', 'd')

    return scheduler.run_system()

def part_one(program):
    possible_combos = itertools.permutations([0,1,2,3,4])
    max_value = 0
    for combo in possible_combos:
        value = calculate_part_one(*combo, program)
        if value > max_value:
            max_value = value
            print(combo)
    print(max_value)

def calculate_part_two(value_one, value_two, value_three, value_four, value_five, program):
    scheduler = intcode.IntCodeScheduler()

    scheduler.add_vm('a', program)
    scheduler.add_vm('b', program)
    scheduler.add_vm('c', program)
    scheduler.add_vm('d', program)
    scheduler.add_vm('e', program)
    scheduler.vms['a'].input.append(value_one)
    scheduler.vms['a'].input.append(0)
    scheduler.vms['b'].input.append(value_two)
    scheduler.vms['c'].input.append(value_three)
    scheduler.vms['d'].input.append(value_four)
    scheduler.vms['e'].input.append(value_five)
    scheduler.add_connection('b', 'a')
    scheduler.add_connection('c', 'b')
    scheduler.add_connection('d', 'c')
    scheduler.add_connection('e', 'd')
    scheduler.add_connection('a', 'e')

    return scheduler.run_system()

def part_two(program):
    possible_combos = itertools.permutations([5,6,7,8,9])
    max_value = 0
    for combo in possible_combos:
        value = calculate_part_two(*combo, program)
        if value > max_value:
            max_value = value
            print(combo)
    print(max_value)

if __name__ == '__main__':
    with open('input.txt') as input_file:
        program = input_file.readline().strip().split(',')
        program = [int(i) for i in program]
    # program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    part_two(program)
    # print(calculate_part_two(9,7,8,5,6, program))