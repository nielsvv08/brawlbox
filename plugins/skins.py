from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate
from core.utils import split_in_three, split_in_two


base_embed = discourtesy.utils.embed(
    {
        "title": "Brawler Skins",
        "color": config.colour,
    }
)

second_embed = deepcopy(base_embed)
third_embed = deepcopy(base_embed)
fourth_embed = deepcopy(base_embed)

special_skins = split_in_three(
    [
        f"{emoji} {name}"
        for name, emoji in constants.brawlers.special_skins.items()
    ]
)

second_embed["embeds"][0]["fields"] = [
    {
        "name": "Special Skins",
        "value": "\n".join(special_skins[0]),
        "inline": True,
    },
    {
        "name": "‎",  # empty space
        "value": "\n".join(special_skins[1]),
        "inline": True,
    },
    {
        "name": "‎",  # empty space
        "value": "\n".join(special_skins[2]),
        "inline": True,
    },
]

gem_skins = split_in_three(
    [
        f"{emoji} {name}"
        for name, (_, emoji, __) in dict(
            **constants.brawlers.shop_gem_skins,
            **constants.brawlers.new_shop_gem_skins,
        ).items()
    ]
)

third_embed["embeds"][0]["fields"] = [
    {
        "name": "Gem Skins",
        "value": "\n".join(gem_skins[0]),
        "inline": True,
    },
    {
        "name": "‎",  # empty space
        "value": "\n".join(gem_skins[1]),
        "inline": True,
    },
    {
        "name": "‎",  # empty space
        "value": "\n".join(gem_skins[2]),
        "inline": True,
    },
]

star_skins = [
    f"{emoji} {name}"
    for name, (_, emoji, _) in constants.brawlers.shop_star_skins.items()
]

fourth_embed["embeds"][0]["fields"] = [
    {
        "name": "Star Skins",
        "value": "\n".join(star_skins),
    }
]


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

    if int(user["id"]) in application.cache.member_ids:
        all_skins.add("Star Shelly")

    first_embed["embeds"][0]["author"] = {
        "name": user["username"],
        "icon_url": discourtesy.utils.avatar_url(user),
    }

    sorted_skins = sorted(all_skins, key=lambda name: name.split()[-1])

    formatted_skins = [
        f"{constants.brawlers.emoji.get(skin)} {skin}" for skin in sorted_skins
    ]

    match len(sorted_skins):
        case length if length == 0:
            fields = [
                {
                    "name": "Unlocked Skins",
                    "value": "‎",  # empty space
                }
            ]
        case length if length < 10:
            fields = [
                {
                    "name": "Unlocked Skins",
                    "value": "\n".join(formatted_skins),
                }
            ]
        case length if length < 21:
            skins = split_in_two(formatted_skins)

            fields = [
                {
                    "name": "Unlocked Skins",
                    "value": "\n".join(skins[0]),
                    "inline": True,
                },
                {
                    "name": "‎",  # empty space
                    "value": "\n".join(skins[1]),
                    "inline": True,
                },
            ]

        case _:
            skins = split_in_three(formatted_skins)

            fields = [
                {
                    "name": "Unlocked Skins",
                    "value": "\n".join(skins[0]),
                    "inline": True,
                },
                {
                    "name": "‎",  # empty space
                    "value": "\n".join(skins[1]),
                    "inline": True,
                },
                {
                    "name": "‎",  # empty space
                    "value": "\n".join(skins[2]),
                    "inline": True,
                },
            ]

    first_embed["embeds"][0]["fields"] = fields

    embeds = (first_embed, second_embed, third_embed, fourth_embed)

    paginate = Paginate("skins", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]
