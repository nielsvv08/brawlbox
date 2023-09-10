import discourtesy

from core.constants import Constants as constants
from core.utils import get_username, r


@discourtesy.command("profile", followup=True)
async def profile_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        username = get_username(user)
        return constants.errors.profile_not_found.format(username)

    try:
        profile_skin = profile["profile_skins"][0]
    except IndexError:
        profile_skin = "default"

    if (
        profile_skin == "default"
        and int(user["id"]) in constants.profile.staff_members
    ):
        profile_skin = "staff"

    colour, thumbnail, footer = constants.profile.skins[profile_skin]

    embed = {
        "title": "Profile Inventory",
        "color": colour,
        "author": {
            "name": user["username"],
            "icon_url": discourtesy.utils.avatar_url(user),
        },
        "thumbnail": {"url": thumbnail},
        "fields": [
            {
                "name": "Coins",
                "value": f"{r(profile['coins'])} {constants.emoji.coins}",
                "inline": True,
            },
            {
                "name": "Gems",
                "value": f"{r(profile['gems'])} {constants.emoji.gems}",
                "inline": True,
            },
            {
                "name": "Star Points",
                "value": (
                    f"{r(int(profile['starpoints']))}"
                    f" {constants.emoji.star_points}"
                ),
                "inline": True,
            },
            {
                "name": "Big Boxes",
                "value": (
                    f"{r(profile['bigboxes'])}" f" {constants.emoji.big_box}"
                ),
                "inline": True,
            },
            {
                "name": "Mega Boxes",
                "value": (
                    f"{r(profile['megaboxes'])}" f" {constants.emoji.mega_box}"
                ),
                "inline": True,
            },
        ],
        "footer": {"icon_url": thumbnail, "text": footer},
    }

    if profile["tier"] > 1:
        embed["fields"].append(
            {
                "name": "Prestige",
                "value": (f"Tier {profile['tier']} <:c:796281532196716544>"),
                "inline": True,
            }
        )

    return discourtesy.utils.embed(embed)
