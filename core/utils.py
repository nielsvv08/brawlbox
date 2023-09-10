from core.constants import Constants as constants


def r(number):
    return "{:,}".format(number)


def calculate_level(profile, brawler_name):
    try:
        current_pp = profile["brawlers"][brawler_name]["powerpoints"]
    except KeyError:
        return 0

    for level in constants.various.levels_reverse:
        required_pp = constants.various.upgrades[str(level)]["powerpoints"]

        if required_pp <= current_pp:
            return level

    return 1


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


def get_username(user):
    return (
        user["global_name"] or user["username"] + "#" + user["discriminator"]
    )


def max_gadgets(brawler_name):
    return len(constants.brawlers.brawlers[brawler_name]["gadgets"])
