import discourtesy

from core import mongo
from core.constants import Constants as constants


@discourtesy.command("buy")
async def buy_commands(application, interaction):
    user = interaction["member"]["user"]
    number = interaction["data"]["options"][0]["value"]

    profile, db = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    try:
        amount = interaction["data"]["options"][1]["value"]
    except IndexError:
        amount = 1

    if amount > 1 and number not in (1, 2, 3, 4):
        amount = 1

    set_query = None

    match number:
        case 1:
            inc_query = {"coins": -2000 * amount, "bigboxes": amount}
        case 2:
            inc_query = {"gems": -30 * amount, "bigboxes": amount}
        case 3:
            inc_query = {"coins": -3000 * amount, "megaboxes": amount}
        case 4:
            inc_query = {"gems": -45 * amount, "megaboxes": amount}
        case num if 5 <= num <= 25:
            skin, (brawler_name, emoji, price) = tuple(
                constants.brawlers.shop_gem_skins.items()
            )[number - 5]

            if profile["brawlers"].get(brawler_name) is None:
                profile["brawlers"][brawler_name] = {
                    "unlocked": False,
                    "level": 1,
                    "powerpoints": 0,
                }

            if profile["brawlers"][brawler_name].get("skins") is None:
                profile["brawlers"][brawler_name]["skins"] = []

            if skin in profile["brawlers"][brawler_name]["skins"]:
                return f"You already purchased the {emoji} {skin} skin. ❌"

            profile["brawlers"][brawler_name]["skins"].append(skin)

            inc_query = {"gems": -price}
            set_query = {
                f"brawlers.{brawler_name}": profile["brawlers"][brawler_name]
            }
        case num if 26 <= num <= 31:
            skin, (brawler_name, emoji, price) = tuple(
                constants.brawlers.shop_star_skins.items()
            )[number - 26]

            if profile["brawlers"].get(brawler_name) is None:
                profile["brawlers"][brawler_name] = {
                    "unlocked": False,
                    "level": 1,
                    "powerpoints": 0,
                }

            if profile["brawlers"][brawler_name].get("skins") is None:
                profile["brawlers"][brawler_name]["skins"] = []

            if skin in profile["brawlers"][brawler_name]["skins"]:
                return f"You already purchased the {emoji} {skin} skin. ❌"

            profile["brawlers"][brawler_name]["skins"].append(skin)

            inc_query = {"starpoints": -price}
            set_query = {
                f"brawlers.{brawler_name}": profile["brawlers"][brawler_name]
            }
        case _:
            return f"There is no item associated with the number {number}."

    currency = tuple(inc_query)[0]
    currency_amount = abs(tuple(inc_query.items())[0][1])

    if profile[currency] < currency_amount:
        return f"You don't have enough {currency} to purchase this item."

    await mongo.update_profile(user["id"], db, set_query, inc_query)

    match number:
        case num if num in (1, 2):
            suffix = "es" if amount != 1 else ""
            return f"You purchased **{amount}** big box{suffix}! ✅"
        case num if num in (3, 4):
            suffix = "es" if amount != 1 else ""
            return f"You purchased **{amount}** mega box{suffix}! ✅"
        case _:
            return f"You purchased the {emoji} **{skin}** skin! ✅"
