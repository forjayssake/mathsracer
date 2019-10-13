import random
from config import gameConfig as config


def get_next_sum() -> dict:
    """
    return a new random sum, consisting of a dictionary containing:
    a randomly selected mathematical operator
    2 randomly selected numbers
    a known result
    """

    sum = {'operator': fetch_operator()}
    sum['values'] = fetch_integers_for_operator(sum['operator'][0])
    sum['answer'] = calculate_answer(sum)
    return sum


def calculate_answer(sum: dict) -> int:
    operator = sum['operator']

    if '+' == operator:
        return sum['values'][0] + sum['values'][1]
    elif '-' == operator:
        return sum['values'][0] - sum['values'][1]
    elif '/' == operator:
        return sum['values'][0] / sum['values'][1]
    elif '*' == operator:
        return sum['values'][0] * sum['values'][1]

    raise ValueError('Operator: ' + operator + 'is invalid')


def fetch_integers_for_operator(operator: str) -> tuple:
    """
    fetch two random integers valid for a given mathematical operator
    :param operator: 
    :return: tuple
    """

    value1 = fetch_random_number()
    value2 = fetch_random_number()

    if '-' == operator:
        # swap order of integers so smaller number
        # is subtracted from larger number
        if value1 != value2 and value2 > value1:
            return value2, value1

    elif '/' == operator:
        # division should always result in an integer
        while not isinstance(value1 / value2, int):
            value1 = fetch_random_number()
            value2 = fetch_random_number()
            # and alway divide the larger number by the smaller
            if value1 != value2 and value2 > value1:
                temp = value1
                value1 = value2
                value2 = temp

    elif '*' == operator:
        # at least one value must be <= max_multiple_value
        if value1 > config['max_multiple_value']:
            while value1 > config['max_multiple_value']:
                value1 = fetch_random_number()

            return value1, value2
        elif value2 > config['max_multiple_value']:
            while value2 > config['max_multiple_value']:
                value2 = fetch_random_number()

    else:
        raise ValueError('Operator: ' + operator + 'is invalid')

    return value1, value2


def fetch_operator() -> tuple:
    """
    fetch a operator containing symbol and text description
    from available operators
    """
    return random.choice(list(config['sum_operators'].keys()))


def fetch_random_number() -> int:
    """
    fetch a number randomly from the list of available numbers
    """
    return random.choice(config['sum_numbers'])
