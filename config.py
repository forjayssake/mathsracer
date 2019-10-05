gameConfig = {
    # track length - number of correct sums to win
    'min_track_size': 5,
    'max_track_size': 20,
    'default_track_size': 10,

    # sum variables
    'sum_numbers': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19.20],
    'min_sum_number': 0,
    'max_sum_number': 10,

    'sum_operators': {
        '+': 'Add',
        '-': 'Subtract',
        '/': 'Divide',
        '*': 'Multiply'
    },

    # highest number to allow for one value in multiplications
    'max_multiple_value': 5,

    # computer difficulty: computer makes mistake if rand over f value
    'ai_error_level_1': 0.5,
    'ai_error_level_2': 0.7,
    'ai_error_level_3': 0.9,
}