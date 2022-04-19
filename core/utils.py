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

    return profile["brawlers"][brawler_name]["skins"][
        profile["brawlers"][brawler_name]["selected"] - 1
    ]


def max_gadgets(brawler_name):
    return len(constants.brawlers.brawlers[brawler_name]["gadgets"])
