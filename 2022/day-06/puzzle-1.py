INPUT_FILE = 'input.txt'

with open(INPUT_FILE,'r') as input_file:
    line = input_file.readline().strip()
    for i in range(4, len(line)):
        if len(set(line[i-4:i])) == 4:
            print(i)
            break