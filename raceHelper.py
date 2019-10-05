from config import gameConfig as config
import sumHelper
import random


def ai_should_fail(level: int)-> bool:
    threshold  = config['ai_error_level_' + str(level)]

    return random.uniform(0, 1) > threshold


def ai_answer_sum(sum: dict, level: int)-> int:
    if ai_should_fail(level):
        return sum['answer'] + 1

    return sum['answer']