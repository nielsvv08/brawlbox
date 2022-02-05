import discourtesy

from core import mongo
from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Confirm


@discourtesy.command("prestige")
async def prestige_command(application, interaction):
    user = interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    can_prestige = True

    for brawler in constants.brawlers.brawlers:
        try:
            if (
                profile["brawlers"][brawler]["level"] != 10
                or len(profile["brawlers"][brawler]["starpowers"]) != 2
                or len(profile["brawlers"][brawler]["gadgets"])
                != (
                    2
                    if brawler in constants.brawlers.two_gadget_brawlers
                    else 1
                )
            ):
                can_prestige = False
        except KeyError:
            can_prestige = False

    if not can_prestige:
        return discourtesy.utils.embed(
            {
                "color": config.colour,
                "title": "Prestige",
                "description": constants.various.prestige_explanation,
            }
        )

    discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": "Prestige",
            "description": constants.various.prestige_explanation,
        }
    )

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": "Prestige",
            "description": constants.various.prestige_confirm_message,
        }
    )

    confirm = Confirm(
        "prestige", prestige_callback, application, interaction, embed
    )
    await confirm.start()

    return embed


async def prestige_callback(application, interaction):
    user = interaction["member"]["user"]

    profile, db = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    for brawler in constants.brawlers.brawlers:
        profile["brawlers"][brawler]["level"] = 1
        profile["brawlers"][brawler]["powerpoints"] = 0
        del profile["brawlers"][brawler]["starpowers"]
        del profile["brawlers"][brawler]["gadgets"]

        if brawler != "Shelly":
            profile["brawlers"][brawler]["unlocked"] = False

    reward = str()

    if profile["tier"] + 1 == 4:
        reward = "Dragon Knight Jessie"
    elif profile["tier"] + 1 == 8:
        reward = "Night Witch Mortis"

    if reward:
        brawler = reward.split(" ")[-1]

        if not profile["brawlers"][brawler].get("skins"):
            profile["brawlers"][brawler]["skins"] = []

        profile["brawlers"][brawler]["skins"].append(reward)

    set_query = {"brawlers": profile["brawlers"], "tr_exp": 0}
    inc_query = {"gems": 200, "tier": 1}

    await mongo.update_profile(user["id"], db, set_query, inc_query)

    await application.mongo.delete_shop(user["id"])

    if reward:
        extra_reward = (
            f" and the {constants.brawlers.emoji[reward]} {reward} skin"
        )
    else:
        extra_reward = str()

    return discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": "Prestige",
            "description": constants.various.prestige_congrats.format(
                profile["tier"] + 1, extra_reward
            ),
        }
    )
