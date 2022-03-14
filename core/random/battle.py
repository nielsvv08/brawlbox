import random

from core.constants import Constants as constants


def generate_description(win):
    if win:
        return random.choice(constants.battle.win_phrases)

    return random.choice(constants.battle.lose_phrases)


def generate_reward(win):
    number = random.randint(1, 3)

    if win:
        match number:
            case 1:
                return (
                    int(random.normalvariate(140, 10)),
                    "starpoints",
                    "star points",
                )
            case 2:
                return int(random.normalvariate(15, 2)), "gems", "gems"
            case 3:
                return (
                    int(random.normalvariate(3, 0.5)),
                    "megaboxes",
                    "mega boxes",
                )

    match number:
        case 1:
            return (
                int(random.normalvariate(110, 10)),
                "starpoints",
                "star points",
            )
        case 2:
            return int(random.normalvariate(12, 2)), "gems", "gems"
        case 3:
            return int(random.normalvariate(3, 0.5)), "bigboxes", "big boxes"


def play_battle():
    number = random.randint(1, 10)

    return number > 3  # 1-3 false, 4-10 true ==> 70% win rate


def random_game_mode():
    return random.choice(constants.battle.game_modes)
