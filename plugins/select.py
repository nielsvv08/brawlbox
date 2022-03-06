import asyncio

import discourtesy

from core import mongo
from core.config import Config as config
from core.constants import Constants as constants


@discourtesy.command("select")
async def select_command(application, interaction):
    brawler_name = interaction["data"]["options"][0]["value"].title()

    brawler_name = constants.brawlers.alternative_brawlers.get(
        brawler_name, brawler_name
    )

    if brawler_name not in constants.brawlers.brawlers:
        return f"`{brawler_name}` is not a valid brawler."

    user = interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    skins = profile["brawlers"][brawler_name].get("skins", [])

    if not skins:
        return f"You don't have any skins for {brawler_name} at the moment."

    options = list()

    for skin in [brawler_name] + list(set(skins)):
        emoji = constants.brawlers.emoji[skin]

        _, emoji_name, emoji_id = emoji.strip("<>").split(":")

        options.append(
            {
                "label": skin,
                "value": f"{brawler_name}-{skin}",
                "emoji": {
                    "name": emoji_name,
                    "id": emoji_id,
                },
            }
        ),

    content = (
        f"Choose a skin for {brawler_name} in the menu below.\n"
        "This menu disappears after the 15-second timeout window expires."
    )

    message = {
        "content": content,
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 3,
                        "custom_id": "select",
                        "options": options,
                        "placeholder": "Pick a skin!",
                    }
                ],
            }
        ],
    }

    asyncio.create_task(select_timeout(application, interaction))

    return message


async def select_timeout(application, interaction):
    await asyncio.sleep(15)

    await application.http.edit_original_interaction_response(
        interaction["token"],
        {"components": list()},
    )


@discourtesy.component("select", timeout=15)
async def select_component(application, interaction):
    user_id = interaction["message"]["interaction"]["user"]["id"]
    brawler_name, skin = interaction["data"]["values"][0].split("-")

    if interaction["member"]["user"]["id"] != user_id:
        return

    profile, db = await application.mongo.get_profile(user_id)

    emoji = constants.brawlers.emoji[skin]

    if skin == brawler_name:
        skin = "default"
        new_selected = 0
    else:
        new_selected = (
            profile["brawlers"][brawler_name]["skins"].index(skin) + 1
        )

    set_query = {f"brawlers.{brawler_name}.selected": new_selected}

    await mongo.update_profile(user_id, db, set_query)

    description = f"You selected the {emoji} {skin} skin for {brawler_name}!"

    embed = discourtesy.utils.embed(
        {"color": config.colour, "title": "Select", "description": description}
    )

    embed["content"] = None
    embed["components"] = list()

    return embed
