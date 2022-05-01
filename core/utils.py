import math
import random
from copy import deepcopy

from core.constants import Constants as constants
from core.random import normal_distribution


def r(number):
    return "{:,}".format(number)


def get_skin(application, profile, brawler_name):
    selected = (
        profile["brawlers"]
        .get(brawler_name, {"selected": 0})
        .get("selected", 0)
    )

    if selected == 0 or not profile["brawlers"][brawler_name].get("skins"):
        return brawler_name

    if (
        brawler_name == "Shelly"
        and selected == -1
        and int(profile["id"]) in application.cache.member_ids
    ):
        return "Star Shelly"

    try:
        return profile["brawlers"][brawler_name]["skins"][
            profile["brawlers"][brawler_name]["selected"] - 1
        ]
    except IndexError:  # e.g. Star Shelly selected but no longer in server
        return brawler_name


def max_gadgets(brawler_name):
    return len(constants.brawlers.brawlers[brawler_name]["gadgets"])
