import asyncio
import time

import discourtesy

from core import mongo, random
from core.config import Config as config
from core.constants import Constants as constants

emoji = constants.emoji


async def remove_buttons(application, interaction):
    await application.http.edit_followup_message(
        interaction["token"],
        interaction["message"]["id"],
        constants.buttons.confirm_stop,
    )


async def box_timeout(
    application, interaction, confirm_buttons=None, first=False
):
    if not first:
        await asyncio.sleep(3)

        await application.http.edit_original_interaction_response(
            interaction["token"],
            confirm_buttons,
        )

    await asyncio.sleep(10)

    await application.http.edit_original_interaction_response(
        interaction["token"],
        constants.buttons.confirm_stop,
    )


async def general_box_command(application, interaction, tries):
    user = interaction["member"]["user"]

    if user["id"] in application.box_cooldown:
        if application.box_cooldown[user["id"]] + 13 < time.time():
            del application.box_cooldown[user["id"]]
        else:
            return (
                "The previous cooldown window hasn't expired yet.\n"
                "You can't open two boxes at the same time."
            )

    application.box_cooldown.update({user["id"]: time.time()})

    match tries:
        case 1:
            title = f"{emoji.box} Brawl Box"
            confirm_buttons = constants.buttons.box_confirm
        case 4:
            title = f"{emoji.big_box} Big Box"
            confirm_buttons = constants.buttons.bigbox_confirm
        case 8:
            title = f"{emoji.mega_box} Mega Box"
            confirm_buttons = constants.buttons.megabox_confirm

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": title,
            "description": "Click the check mark button below to open a box!",
        }
    )

    embed.update(confirm_buttons)

    asyncio.create_task(box_timeout(application, interaction, first=True))

    return embed


async def general_box_component(application, interaction, tries):
    try:
        author_id = interaction["message"]["interaction"]["user"]["id"]
        first_time = True
    except KeyError:
        author_id = interaction["message"]["embeds"][0]["author"][
            "icon_url"  # very hacky but whatever
        ].split("?id=")[-1]
        first_time = False

    user = interaction["member"]["user"]

    if user["id"] != author_id:
        return

    profile, db = await application.mongo.get_profile(user["id"])

    if not profile:
        await application.mongo.insert_profile(user["id"])
        profile, db = await application.mongo.get_profile(user["id"])

    if not first_time and user["id"] in application.box_cooldown:
        if application.box_cooldown[user["id"]] + 3 > time.time():
            return  # double clicking

    match tries:
        case 1:
            profile["boxcounter"] += 1

            confirm_buttons = constants.buttons.box_another_confirm
            thumbnail = constants.various.box_thumbnail
        case 4:
            if profile["bigboxes"] < 1:
                embed = discourtesy.utils.embed(
                    {
                        "title": f"{emoji.big_box} Big Box",
                        "color": config.colour,
                        "description": "You don't have any big boxes to open.",
                    }
                )

                embed.update(constants.buttons.confirm_stop)
                return embed

            profile["bigboxes"] -= 1
            profile["bigcounter"] += 1

            confirm_buttons = constants.buttons.bigbox_another_confirm
            thumbnail = constants.various.bigbox_thumbnail
        case 8:
            if profile["megaboxes"] < 1:
                embed = discourtesy.utils.embed(
                    {
                        "title": f"{emoji.mega_box} Mega Box",
                        "color": config.colour,
                        "description": (
                            "You don't have any mega boxes to open."
                        ),
                    }
                )

                embed.update(constants.buttons.confirm_stop)
                return embed

            profile["megaboxes"] -= 1
            profile["megacounter"] += 1

            confirm_buttons = constants.buttons.megabox_another_confirm
            thumbnail = constants.various.megabox_thumbnail

    application.box_cooldown.update({user["id"]: time.time()})

    asyncio.create_task(remove_buttons(application, interaction))
    asyncio.create_task(
        box_timeout(application, interaction, confirm_buttons, first=False)
    )

    coins = random.generate_coins(tries)
    profile["coins"] += coins

    gems = random.generate_gems(tries)
    profile["gems"] += gems

    description = f"{emoji.coins} {coins}\n"

    if gems:
        description += f"{emoji.gems} {gems}\n"

    for _ in range(tries):
        profile, item = random.get_random_box_item(profile)
        description += f"{item}\n"

    icon_url_with_id = f"{discourtesy.utils.avatar_url(user)}?id={user['id']}"

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "description": description,
            "author": {
                "name": user["username"],
                "icon_url": icon_url_with_id,
            },
            "thumbnail": {"url": thumbnail},
        }
    )

    embed.update(constants.buttons.box_another_grey)

    await mongo.update_profile(user["id"], db, profile)

    return embed


@discourtesy.command("box")
async def box_command(application, interaction):
    return await general_box_command(application, interaction, 1)


@discourtesy.command("bigbox")
async def bigbox_command(application, interaction):
    return await general_box_command(application, interaction, 4)


@discourtesy.command("megabox")
async def megabox_command(application, interaction):
    return await general_box_command(application, interaction, 8)


@discourtesy.component("box_confirm", callback_type=4, timeout=13)
async def box_component(application, interaction):
    return await general_box_component(application, interaction, 1)


@discourtesy.component("bigbox_confirm", callback_type=4, timeout=13)
async def bigbox_component(application, interaction):
    return await general_box_component(application, interaction, 4)


@discourtesy.component("megabox_confirm", callback_type=4, timeout=13)
async def megabox_component(application, interaction):
    return await general_box_component(application, interaction, 8)
