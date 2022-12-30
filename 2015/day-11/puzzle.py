valid_characters = 'abcdefghijklmnopqrstuvwxyz'

def increment_string(input_string):
    if len(input_string) == 0:
        return ""
    char_to_increment = input_string[-1]
    if char_to_increment == 'z':
        return increment_string(input_string[:-1]) + 'a'
    next_char = valid_characters[valid_characters.find(char_to_increment) + 1]
    return input_string[:-1] + next_char

def char_straight(input_char):
    if input_char in ['y', 'z']:
        return ""
    output = [input_char]
    for i in range(2):
        output.append(increment_string(output[-1]))
    return ''.join(output)

def part_one_requirements(input_string):
    has_straight = False
    for i in range(0, len(input_string) - 2):
        if input_string[i:i+3] == char_straight(input_string[i]):
            has_straight = True
    if not has_straight:
        return False
    for invalid_char in ['i', 'o', 'u']:
        if invalid_char in input_string:
            return False

    num_pairs = 0
    pairs = []

    for i in range(0, len(input_string) - 1):
        if input_string[i] == input_string[i+1] and input_string[i] not in pairs:
            pairs.append(input_string[i])
            num_pairs += 1

    if num_pairs < 2:
        return False

    return True

def part_one(initial_password):
    current_password = initial_password
    while not part_one_requirements(current_password):
        current_password = increment_string(current_password)

    return current_password

if __name__ == '__main__':
    p1 = part_one('cqjxjnds')

    print(p1)
    p2_input = increment_string(p1)
    p2 = part_one(p2_input)
    print(p2)