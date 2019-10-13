from config import gameConfig as config
import random


def ai_should_fail(level: int)-> bool:
    threshold  = config['ai_error_level_' + str(level)]

    return random.uniform(0, 1) > threshold


def ai_answer_sum(sum: dict, level: int)-> int:
    if ai_should_fail(level):
        return sum['answer'] + 1

    return sum['answer']


def answer_is_correct(sum: dict, answer: int)->bool:
    """
    return whether a given answer is correct for a given sum
    :param sum:
    :param answer:
    :return: bool
    """

def driver_crash(player: dict):
    """
    player has crashed
    move back one place on the track if able
    :param player:
    :return: void
    """

def driver_advance(player: dict):
    """
    move player one place forward on the track
    :param player:
    :return: void
    """

def has_won(player: dict, track: dict)->bool:
    """
    determine if a given player has reached the end of the track
    :param player:
    :param track:
    :return: bool
    """

def lost_race(player: dict):
    """
    set a lost race status against a given player
    :param player:
    :return: bool
    """