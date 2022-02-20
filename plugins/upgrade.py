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
                current_level - 1 : level - 1
            ]
        )

        required_pp = constants.various.upgrades[str(level)]["powerpoints"]

        if required_coins <= current_coins and required_pp <= current_pp:
            return level, required_coins

    return -1, 0


@discourtesy.command("upgrade")
async def upgrade_command(application, interaction):
    brawler_name = interaction["data"]["options"][0]["value"].title()

    brawler_name = constants.brawlers.alternative_brawlers.get(
        brawler_name, brawler_name
    )

    if brawler_name not in constants.brawlers.brawlers:
        return f"`{brawler_name}` is not a valid brawler."

    user = interaction["member"]["user"]

    profile, db = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    if (
        not profile["brawlers"]
        .get(brawler_name, {"unlocked": False})
        .get("unlocked", True)
    ):
        return f"You need to unlock {brawler_name} before upgrading."

    current_level = profile["brawlers"][brawler_name]["level"]

    if current_level >= 9:
        return f"{brawler_name} is already maxed out!"

    highest_level, required_coins = check_upgrade(profile, brawler_name)

    if highest_level in (current_level, -1):
        return f"You cannot upgrade {brawler_name} at the moment!"

    set_query = {f"brawlers.{brawler_name}.level": highest_level}
    inc_query = {"coins": required_coins * -1}

    await mongo.update_profile(user["id"], db, set_query, inc_query)

    skin = get_skin(profile, brawler_name)
    emoji = constants.brawlers.emoji[skin]

    return f"You upgraded {emoji} {brawler_name} to level {highest_level}!"
