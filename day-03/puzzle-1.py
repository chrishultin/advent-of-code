RUCKSACK_FILE = 'input.txt'

def get_intersection(compartment_1: str, compartment_2: str) -> str:
    return [item for item in compartment_1 if item in compartment_2]

def get_value(rucksack_item: str):
    ord_value = ord(rucksack_item)
    if ord_value < 97:
        return ord_value - 38
    else:
        return ord_value - 96

total_priorities = 0

with open(RUCKSACK_FILE, 'r') as rucksack_contents:
    for line in rucksack_contents.readlines():
        compartment_size = int(len(line.strip()) / 2)
        priority_contents = get_intersection(line[0:compartment_size],
                               line[compartment_size:])
        total_priorities += get_value(priority_contents[0])

print(total_priorities)