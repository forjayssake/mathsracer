gameConfig = {
    # track length - number of correct sums to win
    'min_track_size': 5,
    'max_track_size': 20,
    'default_track_size': 10,

    'sum_operators': {
        '+': 'Add',
        '-': 'Subtract',
        '/': 'Divide',
        '*': 'Multiply'
    },

    # highest number to allow for one value in multiplications
    'max_multiple_value': 5,

    # computer difficulty: computer makes mistake if rand over x value
    'ai_error_level_1': 0.5,
    'ai_error_level_2': 0.7,
    'ai_error_level_3': 0.9,
}