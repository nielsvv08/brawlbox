from math import ceil

from core.constants import Constants as constants


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


def split_in_three(long_list):
    cursor = ceil(len(long_list) / 3)

    return (
        long_list[:cursor],
        long_list[cursor : 2 * cursor],
        long_list[2 * cursor :],
    )


def split_in_two(long_list):
    cursor = ceil(len(long_list) / 2)

    return long_list[:cursor], long_list[cursor:]
