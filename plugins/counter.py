import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import r

emoji = constants.emoji


@discourtesy.command("counter")
async def counter_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    description = (
        f"{emoji.box} **Brawl Boxes** = {r(profile['boxcounter'])}\n"
        f"{emoji.big_box} **Big Boxes** = {r(profile['bigcounter'])}\n"
        f"{emoji.mega_box} **Mega Boxes** = {r(profile['megacounter'])}"
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
