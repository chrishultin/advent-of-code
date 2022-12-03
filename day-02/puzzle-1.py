OUTCOME_SCORE = {
    'WIN': 6,
    'LOSE': 0,
    'DRAW': 3
}

MOVE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

OUTCOME_DICT = {
    'A': ['Y', 'Z'],
    'B': ['Z', 'X'],
    'C': ['X', 'Y']
}

total_score = 0
STRATEGY_FILE = 'input.txt'

with open(STRATEGY_FILE, 'r') as strategy_input:
    for line in strategy_input.readlines():
        opponent_move, player_move = line.strip().split(' ')
        # check if player won
        if OUTCOME_DICT[opponent_move][0] == player_move:
            total_score += OUTCOME_SCORE['WIN'] + MOVE_SCORE[player_move]
        # check if loss
        elif OUTCOME_DICT[opponent_move][1] == player_move:
            total_score += OUTCOME_SCORE['LOSE'] + MOVE_SCORE[player_move]
        # draw
        else:
            total_score += OUTCOME_SCORE['DRAW'] + MOVE_SCORE[player_move]

print(total_score)