from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate
from core.utils import r

emoji = constants.emoji


base_embed = discourtesy.utils.embed(
    {
        "title": "Shop",
        "description": "Use the `/buy` command to purchase one of the items.",
        "color": config.colour,
    }
)

first_embed = deepcopy(base_embed)

fields = (
    f"1. {emoji.big_box} **big box** = 2,000 coins {emoji.coins}",
    f"2. {emoji.big_box} **big box** = 30 gems {emoji.gems}",
    "",
    f"3. {emoji.mega_box} **mega box** = 3,000 coins {emoji.coins}",
    f"4. {emoji.mega_box} **mega box** = 45 gems {emoji.gems}",
)

first_embed["embeds"][0]["fields"] = [
    {"name": "Special Boxes", "value": "\n".join(fields)},
]


second_embed = deepcopy(base_embed)

fields = [
    f"{i}. {_emoji} **{skin}** — {price} gems {emoji.gems}"
    for i, (skin, (_, _emoji, price)) in enumerate(
        constants.brawlers.shop_gem_skins.items(), start=5
    )
]

second_embed["embeds"][0]["fields"] = [
    {"name": "Gem Skins", "value": "\n".join(fields[:11]), "inline": True},
    {"name": "\u200e", "value": "\n".join(fields[11:]), "inline": True},
]

third_embed = deepcopy(base_embed)
fields = [
    f"{i}. {_emoji} **{skin}** — {r(price)} star points {emoji.star_points}"
    for i, (skin, (_, _emoji, price)) in enumerate(
        constants.brawlers.shop_star_skins.items(), start=26
    )
]

third_embed["embeds"][0]["fields"] = [
    {"name": "Star Skins", "value": "\n".join(fields), "inline": True},
]

embeds = (first_embed, second_embed, third_embed)


@discourtesy.command("shop")
async def shop_command(application, interaction):
    paginate = Paginate("shop", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]
