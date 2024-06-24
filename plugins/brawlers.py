from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate
from core.utils import calculate_level, get_skin, get_username, r


@discourtesy.command("brawlers")
async def brawlers_command(application, interaction):
    try:
        user = discourtesy.utils.first_option_user_or_author(interaction)
    except KeyError:
        user = interaction.get("user") or interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if not profile:
        username = get_username(user)
        return constants.errors.profile_not_found.format(username)

    fields = []

    locked_counter = 0
    maxed_counter = 0
    in_progress_counter = 0

    for (
        category,
        brawler_names,
    ) in constants.brawlers.brawler_categories.items():
        description = ""

        for brawler_name in brawler_names:
            status = get_status(application, profile, brawler_name)

            if "Locked" in status:
                locked_counter += 1
            elif "Maxed!" in status:
                maxed_counter += 1
            else:
                in_progress_counter += 1

            description += f"{status}\n"

        fields.append({"name": category, "value": description, "inline": True})

    first_fields = fields[:6]
    second_fields = fields[6:9]
    third_fields = fields[9:12]
    fourth_fields = fields[12:]

    description = (
        "This command shows a list of brawlers and indicates their current "
        "status. Underneath each unlocked brawler, their level and power "
        "points are revealed."
        "\n\n"
    )

    description += (
        f"**Summary**: {locked_counter} locked — {in_progress_counter} in "
        f"progress — {maxed_counter} maxed."
    )

    base_embed = discourtesy.utils.embed(
        {
            "title": "Brawler Progress 🌺✨",
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "color": config.colour,
        }
    )

    first_embed = deepcopy(base_embed)
    first_embed["embeds"][0]["description"] = description
    first_embed["embeds"][0]["fields"] = first_fields

    second_embed = deepcopy(base_embed)
    second_embed["embeds"][0]["fields"] = second_fields

    third_embed = deepcopy(base_embed)
    third_embed["embeds"][0]["fields"] = third_fields

    fourth_embed = deepcopy(base_embed)
    fourth_embed["embeds"][0]["fields"] = fourth_fields

    embeds = (first_embed, second_embed, third_embed, fourth_embed)

    paginate = Paginate("brawlers", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]


def get_status(application, profile, brawler_name):
    skin = get_skin(application, profile, brawler_name)
    emoji = constants.brawlers.emoji[skin]

    brawler = profile["brawlers"].get(brawler_name, {"unlocked": False})
    is_unlocked = brawler.get("unlocked", True)

    if not is_unlocked:
        return f"{emoji} {brawler_name}\n⥝ Locked"

    level = calculate_level(profile, brawler_name)
    power_points = brawler["powerpoints"]

    if power_points == constants.various.upgrades["11"]["powerpoints"]:
        return f"{emoji} **{brawler_name}\n⥝ Level {level} — Maxed!**"

    return (
        f"{emoji} **{brawler_name}\n⥝ Level {level} — {r(power_points)} **"
        f"{constants.emoji.power_points}"
    )
