INPUT_FILE = 'input.txt'

quadcopter_map = []
with open(INPUT_FILE) as input:
    for line in input.readlines():
        quadcopter_map.append([int(i) for i in line.strip()])

visibility_scores = []
for y in range(1, len(quadcopter_map) - 1):
    visibility_scores_row = []
    for x in range(1, len(quadcopter_map[y]) - 1):
        score = 0
        score_parts = []

        current_position = (x, y)

        # Search to left

        up_y_distance = y
        for up_y in sorted(range(0, y), reverse=True):
            # print(f'upy: {up_y}')
            if quadcopter_map[up_y][x] >= quadcopter_map[y][x]:
                up_y_distance = y - up_y
                break
        left_x_distance = x
        for left_x in sorted(range(0, x), reverse=True):
            # print(f'leftx: {left_x}')
            if quadcopter_map[y][left_x] >= quadcopter_map[y][x]:
                left_x_distance = x - left_x
                break
        down_y_distance = len(quadcopter_map) - (y + 1)
        for down_y in range(y+1, len(quadcopter_map)):
            # print(f'downy: {down_y}')
            if quadcopter_map[down_y][x] >= quadcopter_map[y][x]:
                # print("view blocked")
                down_y_distance = down_y - y
                break
        right_x_distance = len(quadcopter_map[y]) - x
        for right_x in range(x + 1, len(quadcopter_map[y])):
            print(f'rightx: {right_x} {quadcopter_map[y][right_x]} {quadcopter_map[y][x]}')
            if quadcopter_map[y][right_x] >= quadcopter_map[y][x]:
                right_x_distance = right_x - x
                break

        visibility_scores.append(left_x_distance * right_x_distance * up_y_distance * down_y_distance)
print(visibility_scores)
print(sorted(visibility_scores, reverse=True)[0])
