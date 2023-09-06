import discourtesy

from core import mongo
from core.constants import Constants as constants
from core.utils import get_skin


def check_upgrade(profile, brawler_name):
    current_coins = profile["coins"]

    current_level = profile["brawlers"][brawler_name]["level"]
    current_pp = profile["brawlers"][brawler_name]["powerpoints"]

    for level in constants.various.levels_reverse:
        required_coins = sum(
            constants.various.upgrades[str(prev_level)]["coins"]
            for prev_level in constants.various.levels[
                current_level - 1 : level - 1  # noqa: E203
            ]
        )

        required_pp = constants.various.upgrades[str(level)]["powerpoints"]

        if required_coins <= current_coins and required_pp <= current_pp:
            return level, required_coins

    return -1, 0
