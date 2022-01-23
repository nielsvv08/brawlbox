import discourtesy

from core.constants import Constants as constants
from core.utils import r


@discourtesy.command("profile", followup=True)
async def profile_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

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

    description = "Badges: "

    box_count = (
        profile["boxcounter"] + profile["bigcounter"] + profile["megacounter"]
    )

    if box_count < 1000:
        description += "<:1OO:569858643923566596> "
    elif box_count < 10000:
        description += "<:1000:569858643810451466> "
    elif box_count < 50000:
        description += "<:10000:569858644003520522> "
    elif box_count < 100000:
        description += "<:50000:569858643995131914> "
    else:
        description += "<:100000:569858643772702743> "

    description += " • "  # en space on both sides

    # TODO: badges for members, Nitro and tournament

    tier = int(profile["tier"])
    tier_emoji_amount = 8 if tier > 8 else tier

    for i in range(0, tier_emoji_amount):
        description += f"{constants.emoji.tiers[i]} "

    if tier > 8:
        description += f"({tier})"

    return discourtesy.utils.embed(
        {
            "color": colour,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "thumbnail": {"url": thumbnail},
            "description": description,
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
                        f"{r(profile['bigboxes'])}"
                        f" {constants.emoji.big_box}"
                    ),
                    "inline": True,
                },
                {
                    "name": "Mega Boxes",
                    "value": (
                        f"{r(profile['megaboxes'])}"
                        f" {constants.emoji.mega_box}"
                    ),
                    "inline": True,
                },
            ],
            "footer": {"icon_url": thumbnail, "text": footer},
        }
    )
