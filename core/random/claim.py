import datetime
import random

from core.constants import Constants as constants


# loot table: normal amount, boosted amount, db_type, fmt_type, emoji

loot_table = [
    (15, 20, "gems", "gems", constants.emoji.gems),
    (75, 100, "starpoints", "star points", constants.emoji.star_points),
    (2, 3, "megaboxes", "mega boxes", constants.emoji.mega_box),
]


def is_weekend():
    return datetime.datetime.utcnow().weekday in (4, 5, 6)


def claim():
    reward = random.choice(loot_table)

    if is_weekend():
        return reward[1:]

    return reward[:1] + reward[2:]
