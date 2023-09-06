import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import get_skin, r
from core.random import get_random_hint


def calculate_level(profile, brawler_name):
    current_pp = profile["brawlers"][brawler_name]["powerpoints"]

    for level in constants.various.levels_reverse:
        required_pp = constants.various.upgrades[str(level)]["powerpoints"]

        if required_pp <= current_pp:
            return level

    return 1


@discourtesy.command("brawlers")
async def brawlers_command(application, interaction):
    try:
        user = discourtesy.utils.first_option_user_or_author(interaction)
    except KeyError:
        user = interaction.get("user") or interaction["member"]["user"]

    show_all = False

    for option in interaction["data"].get("options", ()):
        if option["name"] == "all":
            show_all = option["value"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if not profile:
        complete_username = (
            user["global_name"]
            or user["username"] + "#" + user["discriminator"]
        )
        return constants.errors.profile_not_found.format(complete_username)

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

            if show_all or not "Locked" in status:
                description += f"{status}\n"

        fields.append({"name": category, "value": description, "inline": True})

    first_fields = fields[:6]
    second_fields = fields[6:]

    description = (
        "This command shows a list of brawlers and indicates their current "
        "status. Underneath each unlocked brawler, their level and power "
        "points are revealed."
        "\n\n"
        f"**Summary**: {locked_counter} locked — {in_progress_counter} in "
        f"progress — {maxed_counter} maxed."
    )

    if not show_all:
        description += (
            "\n\nNote: this is a **compressed view**. To view all brawlers, "
            "set the `all` option to true when executing this command."
        )

    return {
        "embeds": [
            {
                "title": "Brawler Progress 🌺✨",
                "description": description,
                "color": config.colour,
                "author": {
                    "name": user["username"],
                    "icon_url": discourtesy.utils.avatar_url(user),
                },
                "fields": first_fields,
            },
            {
                "color": config.colour,
                "fields": second_fields,
                "footer": {"text": f"Hint: {get_random_hint()}"},
            },
        ]
    }


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
        return f"{emoji} **{brawler_name}\n⥝** Level {level} — Maxed!"

    return (
        f"{emoji} **{brawler_name}\n⥝** Level {level} — {r(power_points)} "
        f"{constants.emoji.power_points}"
    )
