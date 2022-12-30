OUTCOME_SCORE = {
    'Z': 6,
    'X': 0,
    'Y': 3
}

MOVE_SCORE = {
    'A': 1,
    'B': 2,
    'C': 3
}

OUTCOME_DICT = {
    'A': ['B', 'C'],
    'B': ['C', 'A'],
    'C': ['A', 'B']
}

total_score = 0
STRATEGY_FILE = 'input.txt'

with open(STRATEGY_FILE, 'r') as strategy_input:
    for line in strategy_input.readlines():
        opponent_move, outcome = line.strip().split(' ')
        # check if player won
        if outcome == 'Z':
            player_move = OUTCOME_DICT[opponent_move][0]
        # check if loss
        elif outcome == 'X':
            player_move = OUTCOME_DICT[opponent_move][1]
        # draw
        else:
            player_move = opponent_move
        total_score += OUTCOME_SCORE[outcome] + MOVE_SCORE[player_move]

print(total_score)