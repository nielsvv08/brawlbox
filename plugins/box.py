import asyncio
import time

import discourtesy

from core import mongo, random
from core.config import Config as config
from core.constants import Constants as constants

emoji = constants.emoji


async def box_timeout(application, interaction, first=False):
    if not first:
        await asyncio.sleep(3)

        await application.http.edit_original_interaction_response(
            interaction["token"],
            constants.buttons.box_another_confirm,
        )

    await asyncio.sleep(10)

    if interaction["member"]["user"]["id"] in application.box_cooldown:
        application.box_cooldown.remove(interaction["member"]["user"]["id"])

    await application.http.edit_original_interaction_response(
        interaction["token"],
        constants.buttons.confirm_stop,
    )


async def remove_buttons(application, interaction):
    await application.http.edit_followup_message(
        interaction["token"],
        interaction["message"]["id"],
        constants.buttons.confirm_stop,
    )


@discourtesy.command("box")
async def box_command(application, interaction):
    user = interaction["member"]["user"]

    if user["id"] in application.box_cooldown:
        return (
            "The cooldown window hasn't expired yet.\n"
            "You can't open two boxes at the same time."
        )

    application.box_cooldown.append(user["id"])

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": f"{emoji.box} Brawl Box",
            "description": "Click the check mark button below to open a box!",
        }
    )

    embed.update(constants.buttons.box_confirm)

    asyncio.create_task(box_timeout(application, interaction, first=True))

    return embed


@discourtesy.command("bigbox")
async def bigbox_command(application, interaction):
    user = interaction["member"]["user"]

    if user["id"] in application.box_cooldown:
        return (
            "The 5 second cooldown window hasn't expired yet.\n"
            "You (or a server moderator) should set a slowmode for this "
            "channel, in order to prevent it."
        )

    application.box_cooldown.append(user["id"])

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": f"{emoji.big_box} Big Box",
            "description": "Click the check mark button below to open a box!",
        }
    )

    embed.update(constants.buttons.bigbox_confirm)

    asyncio.create_task(box_timeout(application, interaction, first=True))

    return embed


@discourtesy.command("megabox")  # yes i did this three times, deal with it
async def megabox_command(application, interaction):
    user = interaction["member"]["user"]

    if user["id"] in application.box_cooldown:
        return (
            "The 5 second cooldown window hasn't expired yet.\n"
            "You (or a server moderator) should set a slowmode for this "
            "channel, in order to prevent it."
        )

    application.box_cooldown.append(user["id"])

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": f"{emoji.mega_box} Mega Box",
            "description": "Click the check mark button below to open a box!",
        }
    )

    embed.update(constants.buttons.megabox_confirm)

    asyncio.create_task(box_timeout(application, interaction, first=True))

    return embed


@discourtesy.component("box_confirm", callback_type=4)
async def box_component(application, interaction):
    try:
        author_id = interaction["message"]["interaction"]["user"]["id"]
    except KeyError:
        author_id = interaction["message"]["embeds"][0]["author"][
            "icon_url"  # very hacky but whatever
        ].split("/")[4]

    user = interaction["member"]["user"]

    if user["id"] != author_id:
        return

    profile, db = await application.mongo.get_profile(user["id"])

    if not profile:
        await application.mongo.insert_profile(user["id"])
        profile, db = await application.mongo.get_profile(user["id"])

    application.box_cooldown.append(user["id"])

    profile["boxcounter"] += 1

    coins = random.generate_coins(1)
    profile["coins"] += coins

    gems = random.generate_gems(1)
    profile["gems"] += gems

    description = f"{emoji.coins} {coins}\n"

    if gems:
        description += f"{emoji.gems} {gems}\n"

    profile, item = random.get_random_box_item(profile)
    description += f"{item}\n"

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "description": description,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "thumbnail": {"url": constants.various.box_thumbnail},
        }
    )

    embed.update(constants.buttons.box_another_grey)

    await mongo.update_profile(user["id"], db, profile)

    asyncio.create_task(remove_buttons(application, interaction))
    asyncio.create_task(box_timeout(application, interaction))

    return embed


@discourtesy.component("bigbox_confirm", callback_type=4)
async def bigbox_component(application, interaction):
    author = interaction["message"]["interaction"]["user"]
    user = interaction["member"]["user"]

    if user["id"] != author["id"]:
        return

    profile, db = await application.mongo.get_profile(user["id"])

    if not profile:
        await application.mongo.insert_profile(user["id"])
        profile, db = await application.mongo.get_profile(user["id"])

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

    coins = random.generate_coins(4)
    profile["coins"] += coins

    gems = random.generate_gems(4)
    profile["gems"] += gems

    description = f"{emoji.coins} {coins}\n"

    if gems:
        description += f"{emoji.gems} {gems}\n"

    for _ in range(4):
        profile, item = random.get_random_box_item(profile)
        description += f"{item}\n"

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "description": description,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "thumbnail": {"url": constants.various.bigbox_thumbnail},
        }
    )

    await mongo.update_profile(user["id"], db, profile)

    asyncio.create_task(remove_buttons(application, interaction))

    embed.update(constants.buttons.confirm_stop)

    return embed


@discourtesy.component("megabox_confirm", callback_type=4)
async def megabox_component(application, interaction):
    author = interaction["message"]["interaction"]["user"]
    user = interaction["member"]["user"]

    if user["id"] != author["id"]:
        return

    profile, db = await application.mongo.get_profile(user["id"])

    if not profile:
        await application.mongo.insert_profile(user["id"])
        profile, db = await application.mongo.get_profile(user["id"])

    if profile["megaboxes"] < 1:
        embed = discourtesy.utils.embed(
            {
                "title": f"{emoji.mega_box} Mega Box",
                "color": config.colour,
                "description": "You don't have any mega boxes to open.",
            }
        )

        embed.update(constants.buttons.confirm_stop)
        return embed

    profile["megaboxes"] -= 1
    profile["megacounter"] += 1

    coins = random.generate_coins(8)
    profile["coins"] += coins

    gems = random.generate_gems(8)
    profile["gems"] += gems

    description = f"{emoji.coins} {coins}\n"

    if gems:
        description += f"{emoji.gems} {gems}\n"

    for _ in range(8):
        profile, item = random.get_random_box_item(profile)
        description += f"{item}\n"

    embed = discourtesy.utils.embed(
        {
            "color": config.colour,
            "description": description,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "thumbnail": {"url": constants.various.megabox_thumbnail},
        }
    )

    await mongo.update_profile(user["id"], db, profile)

    asyncio.create_task(remove_buttons(application, interaction))

    embed.update(constants.buttons.confirm_stop)

    return embed
