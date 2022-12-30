INPUT_FILE = 'input.txt'

quadcopter_map = []
with open(INPUT_FILE) as input:
    for line in input.readlines():
        quadcopter_map.append([int(i) for i in line.strip()])

visible_from_outside = set()
for y in range(0, len(quadcopter_map)):
    for x in range(0, len(quadcopter_map[y])):
        if x == 0 or x == (len(quadcopter_map[y]) - 1):
            print('on edge')
            visible_from_outside.add((y,x))
        if y == 0 or y == len(quadcopter_map) - 1:
            print('on edge')
            visible_from_outside.add((y,x))
        else:
            visible = [True, True, True, True]
            for x_sub in range(0, x):
                if quadcopter_map[y][x] <= quadcopter_map[y][x_sub]:
                    visible[0] = False
            for x_sub in range(x+1, len(quadcopter_map[y])):
                if quadcopter_map[y][x] <= quadcopter_map[y][x_sub]:
                    visible[1] = False
            for y_sub in range(0, y):
                if quadcopter_map[y][x] <= quadcopter_map[y_sub][x]:
                    visible[2] = False
            for y_sub in range(y+1, len(quadcopter_map)):
                if quadcopter_map[y][x] <= quadcopter_map[y_sub][x]:
                    visible[3] = False
            if visible[0] or visible[1] or visible[2] or visible[3]:
                print(f'{y} {x} ({quadcopter_map[y][x]})')
                visible_from_outside.add((y,x))

print(visible_from_outside)
print(len(visible_from_outside))
