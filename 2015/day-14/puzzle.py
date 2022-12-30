def parser(input_file_name: str):
    reindeer = {}
    with open(input_file_name, 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip().split(' ')
            name = line[0]
            speed = int(line[3])
            duration = int(line[6])
            wait = int(line[13])
            reindeer[name] = {
                'speed': speed,
                'duration': duration,
                'wait': wait,
                'distance': speed * duration,
                'time': duration + wait
            }
            print(f'{name} {speed} {duration} {wait}')
    return reindeer

def part_one(reindeer: dict, time = 1000):
    max_distance = 0
    for name, deer in reindeer.items():
        total_cycles, remainder = divmod(time, deer['time'])
        distance = (deer['distance'] * total_cycles) + (deer['speed'] * min(remainder, deer['duration']))
        max_distance = max(max_distance, distance)
    print(max_distance)

def part_two(reindeer: dict, time = 1000):
    scores = {}
    for i in range(1, time + 1):
        current_first = [None]
        current_max_dist = -1
        for name, deer in reindeer.items():
            total_cycles, remainder = divmod(i, deer['time'])
            distance = (deer['distance'] * total_cycles) + (deer['speed'] * min(remainder, deer['duration']))
            if distance > current_max_dist:
                current_first = [name]
                current_max_dist = distance
            elif distance == current_max_dist:
                current_first.append(name)

        for j in current_first:
            scores[j] = scores.get(j, 0) + 1

    print(scores)


if __name__ == '__main__':
    data = parser('input.txt')
    # part_one(data, 2503)
    part_two(data, 2503)