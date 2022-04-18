import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import get_skin


@discourtesy.command("brawlers")
async def brawlers_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    fields = []

    for (
        category,
        brawler_names,
    ) in constants.brawlers.brawler_categories.items():
        description = ""

        for brawler_name in brawler_names:
            description += (
                f"{get_status(application, profile, brawler_name)}\n"
            )

        fields.append({"name": category, "value": description, "inline": True})

    first_fields = fields[:6]
    second_fields = fields[6:]

    return {
        "embeds": [
            {
                "title": "Brawlers",
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
            },
        ]
    }


def get_status(application, profile, brawler_name):
    skin = get_skin(application, profile, brawler_name)
    emoji = constants.brawlers.emoji[skin]

    unlocked = (
        profile["brawlers"]
        .get(brawler_name, {"unlocked": False})
        .get("unlocked", True)
    )

    if unlocked:
        locked_unlocked = "**Unlocked**"
    else:
        locked_unlocked = "Locked"

    return f"{emoji} {brawler_name} — {locked_unlocked}"
