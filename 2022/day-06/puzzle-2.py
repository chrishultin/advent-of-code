INPUT_FILE = 'input.txt'

with open(INPUT_FILE,'r') as input_file:
    line = input_file.readline().strip()
    for i in range(14, len(line)):
        if len(set(line[i-14:i])) == 14:
            print(i)
            break