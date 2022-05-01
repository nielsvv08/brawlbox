import asyncio

import discourtesy

from core import mongo
from core.config import Config as config
from core.constants import Constants as constants


def can_prestige(profile):
    for brawler in constants.brawlers.brawlers:
        try:
            if (
                profile["brawlers"][brawler]["level"] != 11
                or len(profile["brawlers"][brawler]["starpowers"]) != 2
                or len(profile["brawlers"][brawler]["gadgets"])
                != (
                    2
                    if brawler in constants.brawlers.two_gadget_brawlers
                    else 1
                )
            ):
                return False
        except KeyError:
            return False

    return True


@discourtesy.command("prestige")
async def prestige_command(application, interaction):
    user = interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    if not can_prestige(profile):
        return discourtesy.utils.embed(
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

    embed.update(constants.buttons.prestige_confirm)

    asyncio.create_task(prestige_timeout(application, interaction))

    return embed


async def prestige_timeout(application, interaction):
    await asyncio.sleep(10)

    await application.http.edit_original_interaction_response(
        interaction["token"],
        constants.buttons.confirm_stop,
    )


@discourtesy.component("prestige_confirm", timeout=10)
async def prestige_component(application, interaction):
    user = interaction["member"]["user"]

    profile, db = await application.mongo.get_profile(user["id"])

    if not can_prestige(profile):
        return "Something went wrong!"

    for brawler in constants.brawlers.brawlers:
        profile["brawlers"][brawler]["level"] = 1
        profile["brawlers"][brawler]["powerpoints"] = 0
        del profile["brawlers"][brawler]["gadgets"]
        del profile["brawlers"][brawler]["starpowers"]

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

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": "Prestige",
            "description": constants.various.prestige_congrats.format(
                profile["tier"] + 1, extra_reward
            ),
        }
    )

    embed.update(constants.buttons.confirm_stop)

    return embed
