import random

from core.constants import Constants as constants


def get_random_hint():
    return random.choice(constants.hints)
