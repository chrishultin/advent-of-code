ASSIGNMENT_FILE = 'input.txt'

overlapping = 0

def overlaps(assignment_1_start, assignment_1_end, assignment_2_start, assignment_2_end):
    assign_1_range = list(range(int(assignment_1_start), int(assignment_1_end) + 1))
    assign_2_range = list(range(int(assignment_2_start), int(assignment_2_end) + 1))
    assign_1_contained = True
    assign_2_contained = True
    for i in assign_1_range:
        if i not in assign_2_range:
            assign_1_contained = False
    for i in assign_2_range:
        if i not in assign_1_range:
            assign_2_contained = False
    return assign_1_contained or assign_2_contained

with open(ASSIGNMENT_FILE, 'r') as assignment_file:
    for line in assignment_file.readlines():
        assignment_1, assignment_2 = line.strip().split(',')
        assignment_1_start, assignment_1_end = assignment_1.split('-')
        assignment_2_start, assignment_2_end = assignment_2.split('-')
        if overlaps(assignment_1_start, assignment_1_end, assignment_2_start, assignment_2_end):
            print(line)
            overlapping += 1
        else:
            print(f'not {line}')

print(overlapping)