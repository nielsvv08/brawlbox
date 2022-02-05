import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import get_skin


@discourtesy.command("powerpoints")
async def powerpoints_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    fields = []

    for category, brawlers in constants.brawlers.brawler_categories.items():
        description = ""

        for brawler in brawlers:
            description += f"{get_status(profile, brawler)}\n"

        fields.append({"name": category, "value": description, "inline": True})

    first_fields = fields[:6]
    second_fields = fields[6:]

    return {
        "embeds": [
            {
                "title": "Power Points",
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


def get_status(profile, brawler_name):
    skin = get_skin(profile, brawler_name)
    emoji = constants.brawlers.emoji[skin]

    if not (
        profile["brawlers"]
        .get(brawler_name, {"unlocked": False})
        .get("unlocked", True)
    ):
        return f"{emoji} — Locked"

    brawler = profile["brawlers"][brawler_name]

    if brawler["powerpoints"] == 1410:
        return f"{emoji} — **Maxed**"

    current_pp = brawler["powerpoints"] - sum(
        constants.brawlers.powerpoint_costs[: brawler["level"]]
    )
    required_pp = constants.brawlers.powerpoint_costs[brawler["level"]]

    if current_pp >= required_pp:
        return (
            f"{emoji} — **{current_pp} / {required_pp}** "
            "<:pp:563001978079150102>"
        )

    return f"{emoji} — {current_pp} / {required_pp} <:pp:563001978079150102>"
