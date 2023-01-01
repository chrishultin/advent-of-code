def calculate_houses_p1(max_house: int, target_value: int):
    houses = [0 for _ in range(max_house)]
    for elf_num in range(1, max_house + 1):
        for house_num in range(elf_num - 1, max_house, elf_num):
            houses[house_num] += 10*elf_num

    for index, house in enumerate(houses):
        if house >= target_value:
            return index + 1

def calculate_houses_p2(max_house: int, target_value: int):
    houses = [0 for _ in range(max_house * 50)]
    for elf_num in range(1, max_house + 1):
        for i in range(1, 51):
            houses[(i * elf_num - 1)] += 11*elf_num

    for index, house in enumerate(houses):
        if house >= target_value:
            return index + 1

if __name__ == '__main__':
    print(calculate_houses_p2(3600000, 36000000))