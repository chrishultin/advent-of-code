import itertools


def part_one(minimum: int, maximum: int):
    total_valid = 0
    for possible_password in range(minimum, maximum + 1):
        if part_one_is_valid(str(possible_password)):
            total_valid += 1

    print(total_valid)

def part_one_is_valid(password: str) -> bool:
    has_duplicate = False
    for i in range(0, len(password) - 1):
        if password[i] == password[i + 1]:
            has_duplicate = True
        if password[i] > password[i + 1]:
            return False

    if not has_duplicate:
        return False

    return True

def part_two_is_valid(password: str) -> bool:
    has_duplicate = False
    for i,g in itertools.groupby(password):
        if len(list(g)) == 2:
            has_duplicate = True
    for i in range(0, len(password) - 1):
        if password[i] > password[i + 1]:
            return False

    if not has_duplicate:
        return False

    return True

def part_two(minimum: int, maximum: int):
    total_valid = 0
    for possible_password in range(minimum, maximum + 1):
        if part_two_is_valid(str(possible_password)):
            total_valid += 1

    print(total_valid)

if __name__ == '__main__':
    # part_one(123453,123457)
    part_two(264360,746325)