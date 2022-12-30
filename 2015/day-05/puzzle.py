def naughty_or_nice_1(word: str) -> bool:
    banned_patterns = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'
    # Check for banned patterns and short-circuit
    for pattern in banned_patterns:
        if pattern in word:
            return False

    # Check for 3 vowels
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1

    # Check for double letters
    double_letters = False
    for i in range(0, len(word) - 1):
        if word[i] == word[i+1]:
            double_letters = True

    return double_letters and vowel_count >= 3

def naughty_or_nice_2(word: str) -> bool:
    double_letters = False

    for i in range(0, len(word) - 1):
        for j in range(0, len(word) - 1):
            if j not in range(i - 1, i + 2):
                if word[i:i+2] == word[j:j+2]:
                    print(word[i:i+2])
                    print(word[j:j+2])
                    double_letters = True
            else:
                print('overlapping')

    repeat_with_gap = False
    for i in range(0, len(word) - 2):
        if word[i] == word[i + 2]:
            repeat_with_gap = True
            print(word)
            print(i)

    return double_letters and repeat_with_gap

def puzzle_1(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        nice_strings = [i for i in input_file.readlines() if naughty_or_nice_1(i.strip())]
    print(len(nice_strings))

def puzzle_2(input_file_name: str):
    with open(input_file_name, 'r') as input_file:
        nice_strings = [i for i in input_file.readlines() if naughty_or_nice_2(i.strip())]
    print(len(nice_strings))

if __name__ == '__main__':
    test_inputs = [
        ('ugknbfddgicrmopn', True),
        ('aaa', True),
        ('jchzalrnumimnmhp', False),
        ('haegwjzuvuyypxyu', False),
        ('dvszwmarrgswjxmb', False)
    ]
    for input, result in test_inputs:
        assert naughty_or_nice_1(input) == result

    # puzzle_1('input.txt')

    test_inputs = [
        ('qjhvhtzxzqqjkmpb', True),
        ('xxyxx', True),
        ('uurcxstgmygtbstg', False),
        ('ieodomkazucvgmuy', False),
        ('aaa', False),
        ('aabcdefegaa', True)
    ]
    for input, result in test_inputs:
        assert naughty_or_nice_2(input) == result

    puzzle_2('input.txt')