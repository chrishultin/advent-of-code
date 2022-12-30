import string


def characters_after_escape(input_string: str):
    line = input_string[1:-1]

    i = line.find("\\")
    while i != -1:
        if i+1 < len(line):
            if line[i+1] == '"' or line[i+1] == '\\':
                line = line[:i] + '#' + line[i+2:]
            i = line.find("\\", i+1)

    i = line.find('\\x')

    while i != -1:
        if i+3 < len(line):
            if line[i+2] in string.hexdigits and line[i+3] in string.hexdigits:
                # print('removing hex')
                # print(line)
                line = line[:i] + '#' + line[i+4:]
                # print(line)
                i = line.find('\\x')
            else:
                print('characters not hex, ignoring')
                i = line.find('\\x', i + 1)
        else:
            break
    return line

def escape_characters(input_string: str):
    output_string = ""
    for character in input_string:
        if character == '"':
            output_string += '\\"'
        elif character == '\\':
            output_string += '\\\\'
        else:
            output_string += character
    return f'"{output_string}"'


if __name__ == '__main__':
    #part 1
    # with open('test_input.txt', 'r') as input_file:
    #     totals = []
    #     for line in input_file.readlines():
    #         line = line.strip()
    #         # print(f'in: {line}')
    #         # print(characters_after_escape(line))
    #         # print(len(characters_after_escape(line)))
    #         # print(len(line) - len(characters_after_escape(line)))
    #         totals.append(len(line) - len(characters_after_escape(line)))
    # print(sum(totals))

    #part 2
    with open('input.txt', 'r') as input_file:
        totals = []
        for line in input_file.readlines():
            line = line.strip()
            output = escape_characters(line)
            print(f'in : {line}')
            print(f'out: {output}')
            totals.append(len(output) - len(line))
    print(sum(totals))