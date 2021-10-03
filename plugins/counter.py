import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import r


@discourtesy.command("counter")
async def counter_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    description = (
        f"<:box:563003560233533440> **Brawl Boxes** = {r(profile['boxcounter'])}\n"
        f"<:big:563003560124612649> **Big Boxes** = {r(profile['bigcounter'])}\n"
        f"<:megab:563003560325808151> **Mega Boxes** = {r(profile['megacounter'])}"
    )

    return discourtesy.utils.embed(
        {
            "title": "Counter",
            "color": config.colour,
            "description": description,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
        }
    )
