import itertools

def part_one(containers: list, total: int):
    options = []
    for i in range(1, len(containers) + 1):
        for x in itertools.combinations(containers, i):
            if sum(x) == total:
                options.append(x)

    print(options)
    return len(options)

def part_two(containers: list, total: int):
    minimum_containers = len(containers)
    options = []
    for i in range(1, len(containers) + 1):
        for x in itertools.combinations(containers, i):
            if sum(x) == total:
                options.append(x)
                if len(x) < minimum_containers:
                    minimum_containers = len(x)

    print(minimum_containers)
    print([x for x in options if len(x) == minimum_containers])
    return len([x for x in options if len(x) == minimum_containers])


if __name__ == '__main__':
    containers = []
    with open('input.txt') as input_file:
        for line in input_file.readlines():
            containers.append(int(line.strip()))
    print(part_two(containers, 150))