from core.constants import Constants as constants


def r(number):
    return "{:,}".format(number)


def get_skin(profile, brawler_name):
    selected = (
        profile["brawlers"]
        .get(brawler_name, {"selected": 0})
        .get("selected", 0)
    )

    if selected <= 0:
        return brawler_name

    return profile["brawlers"][brawler_name]["skins"][
        profile["brawlers"][brawler_name]["selected"] - 1
    ]


def max_gadgets(brawler_name):
    return len(constants.brawlers.brawlers[brawler_name]["gadgets"])
