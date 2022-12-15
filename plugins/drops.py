import discourtesy

from core import random
from core.config import Config as config
from core.constants import Constants as constants
from core.split import split_in_two


@discourtesy.command("drops")
async def drops_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    droprates = random.get_droprates(profile)[1]

    fields = list()

    for name, emoji, key in constants.various.drops_field_info:
        rate = droprates.get(key, 0.0)

        value = emoji + (" **{:0.3f}%**".format(rate) if rate else " 0.000%")

        fields.append({"name": name, "value": value, "inline": True})

    return discourtesy.utils.embed(
        {
            "title": "Drops",
            "color": config.colour,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "fields": fields,
        }
    )
