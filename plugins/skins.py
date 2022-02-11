from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate


base_embed = discourtesy.utils.embed(
    {
        "title": "Brawler Skins  •  ",
        "color": config.colour,
    }
)

second_embed = deepcopy(base_embed)
third_embed = deepcopy(base_embed)
fourth_embed = deepcopy(base_embed)

second_embed["embeds"][0]["title"] += "Special"
second_embed["embeds"][0]["description"] = "\n".join(
    f"{emoji} {name}"
    for name, emoji in constants.brawlers.special_skins.items()
)

third_embed["embeds"][0]["title"] += "Gems"
third_embed["embeds"][0]["description"] = "\n".join(
    f"{emoji} {name}"
    for name, emoji in constants.brawlers.shop_gem_skins.items()
)

fourth_embed["embeds"][0]["title"] += "Star Points"
fourth_embed["embeds"][0]["description"] = "\n".join(
    f"{emoji} {name}"
    for name, emoji in constants.brawlers.shop_star_skins.items()
)


@discourtesy.command("skins")
async def skins_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    first_embed = deepcopy(base_embed)
    all_skins = set()

    for brawler in constants.brawlers.brawlers:
        skins = profile["brawlers"].get(brawler, {}).get("skins", [])

        for skin in skins:
            all_skins.add(skin)

    # TODO: add Star Shelly skin for server members.

    first_embed["embeds"][0]["title"] += "Unlocked"

    first_embed["embeds"][0]["author"] = {
        "name": user["username"],
        "icon_url": discourtesy.utils.avatar_url(user),
    }

    first_embed["embeds"][0]["description"] = "\n".join(
        f"{constants.brawlers.emoji.get(skin)} {skin}" for skin in all_skins
    )

    embeds = (first_embed, second_embed, third_embed, fourth_embed)

    paginate = Paginate("skins", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]
