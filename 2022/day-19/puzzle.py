from collections import deque as queue

def parser(input_file_name: str):
    blueprints = {}
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().split(' ')
            blueprint_number = int(line[1][:-1])
            ore_for_ore = int(line[6])
            ore_for_clay = int(line[12])
            ore_for_obsidian = int(line[18])
            clay_for_obsidian = int(line[21])
            ore_for_geode = int(line[27])
            obsidian_for_geode = int(line[30])

            blueprint = {
                'id': blueprint_number,
                'geode': (ore_for_geode, 0, obsidian_for_geode, 0,),
                'obsidian': (ore_for_obsidian, clay_for_obsidian, 0, 0,),
                'clay': (ore_for_clay, 0, 0, 0,),
                'ore': (ore_for_ore, 0, 0, 0,),
                'max': (max(ore_for_ore, ore_for_geode, ore_for_obsidian, ore_for_clay), clay_for_obsidian, obsidian_for_geode,)
            }
            blueprints[blueprint_number] = blueprint
    return blueprints

def part_one(blueprints):
    total = 0
    for blueprint in blueprints.values():
        bp_score = part_one_bfs(blueprint, 25)
        # print(bp_score)
        total += blueprint['id'] * bp_score
    print(total)

def can_build(current_resources, blueprint_costs):
    for resource_count, required_count in zip(current_resources, blueprint_costs):
        if resource_count < required_count:
            return False
    return True

def cap_resources(current_resources, max_resources):
    # print(current_resources)
    return (min(current_resources[0], max_resources[0] * 2),
            min(current_resources[1], max_resources[1] * 2),
            min(current_resources[2], max_resources[2] * 2),
            current_resources[3],)

def part_one_bfs(blueprint, time):
    initial_state = ((0,0,0,0),(1,0,0,0))
    q = queue([initial_state])
    visited = set()

    for minute in range(1, time):
        # Iterate over each item _currently_ in the queue.
        # Intentionally stop before we encounter new entries
        # print(f'options at minute {minute}: {len(q)}')
        for _ in range(len(q)):
            current_state = q.popleft()

            if current_state in visited:
                continue
            visited.add(current_state)

            current_resources = current_state[0]
            current_bots = current_state[1]

            gathered_ore = current_state[1]
            next_ore = tuple(c+g for c,g in zip(current_resources, gathered_ore))
            # Can we build a 'Geode Cracker'?
            if can_build(current_resources, blueprint['geode']):
                # print('buy geode')
                # Next ore = current + gathered - cost
                next_ore_q = tuple(n - cost for n, cost in zip(next_ore, blueprint['geode']))
                next_bots = (current_bots[0], current_bots[1], current_bots[2], current_bots[3] + 1)
                q.append((cap_resources(next_ore_q, blueprint['max']), next_bots))

            if can_build(current_resources, blueprint['obsidian']):
                if current_bots[2] < blueprint['geode'][2]:
                    # print('buy obsidian')
                    # Next ore = current + gathered - cost
                    next_ore_q = tuple(n - cost for n, cost in zip(next_ore, blueprint['obsidian']))
                    next_bots = (current_bots[0], current_bots[1], current_bots[2] + 1, current_bots[3])
                    q.append((cap_resources(next_ore_q, blueprint['max']), next_bots))
                # else:
                #     print('capped on obsidian bots')

            if can_build(current_resources, blueprint['clay']) and current_bots[1]<blueprint['obsidian'][1]:
                # print('buy clay')
                # Next ore = current + gathered - cost
                next_ore_q = tuple(n - cost for n, cost in zip(next_ore, blueprint['clay']))
                next_bots = (current_bots[0], current_bots[1] + 1, current_bots[2], current_bots[3])
                q.append((cap_resources(next_ore_q, blueprint['max']), next_bots))

            if can_build(current_resources, blueprint['ore']) and current_bots[0]<blueprint['max'][0]:
                # print('buy ore')
                # Next ore = current + gathered - cost
                next_ore_q = tuple(n - cost for n, cost in zip(next_ore, blueprint['ore']))
                next_bots = (current_bots[0] + 1, current_bots[1], current_bots[2], current_bots[3])
                q.append((cap_resources(next_ore_q, blueprint['max']), next_bots))

            # print('buy nothing')
            q.append((cap_resources(next_ore, blueprint['max']), current_bots,))

    max_geodes = 0
    for i in q:
        if i[0][3] > max_geodes:
            max_geodes = i[0][3]
    return(max_geodes)

def part_two(blueprints):
    total = 1
    for index, blueprint in enumerate(blueprints.values()):
        if index >= 3:
            break
        bp_score = part_one_bfs(blueprint, 33)
        print(bp_score)
        # break
        total *= bp_score
    print(total)

if __name__ == '__main__':
    blueprints = parser('input.txt')
    print(part_one(blueprints))
    # print(part_two(blueprints))