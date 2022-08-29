import datetime
from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate
from core.random import choose_skins
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

first_embed["embeds"][0]["description"] += (
    "\n\nYou can buy multiple boxes at the same time by filling out the "
    "optional `amount` argument when executing the slash command."
)

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

second_embed_new_fields = [
    f"{i}. {_emoji} **{skin}** = {price} gems {emoji.gems}"
    for i, (skin, (_, _emoji, price)) in enumerate(
        constants.brawlers.new_shop_gem_skins.items(), start=5
    )
]


@discourtesy.command("shop")
async def shop_command(application, interaction):
    user = interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    shop = await application.mongo.get_shop(user["id"])

    if shop:
        available_skins = shop["skins"]
    else:
        unlocked_skins = set()

        for brawler in constants.brawlers.brawlers:
            skins = profile["brawlers"].get(brawler, {}).get("skins", [])

            for skin in skins:
                unlocked_skins.add(skin)

        locked_gem_skins = list(
            set(constants.brawlers.shop_gem_skins.keys()).difference(
                unlocked_skins
            )
        )

        locked_star_skins = list(
            set(constants.brawlers.shop_star_skins.keys()).difference(
                unlocked_skins
            )
        )

        available_gem_skins = choose_skins(locked_gem_skins, 3)
        available_star_skins = choose_skins(locked_star_skins, 1)

        available_skins = available_gem_skins + available_star_skins

        set_query = {"skins": available_skins}
        await application.mongo.insert_shop(user["id"], set_query)

    daily_skins = list()

    for i, skin in enumerate(
        available_skins, start=5 + len(constants.brawlers.new_shop_gem_skins)
    ):
        try:
            _, _emoji, price = constants.brawlers.shop_gem_skins[skin]

            daily_skins.append(
                f"{i}. {_emoji} **{skin}** = {price} gems {emoji.gems}"
            )
        except KeyError:
            _, _emoji, price = constants.brawlers.shop_star_skins[skin]

            daily_skins.append(
                f"{i}. {_emoji} **{skin}** = {r(price)} star points "
                f"{emoji.star_points}"
            )

    if daily_skins:
        midnight = datetime.datetime.utcnow().replace(
            hour=0,
            minute=0,
            second=0,
            tzinfo=datetime.timezone(datetime.timedelta()),
        ) + datetime.timedelta(
            days=1
        )  # why is datetime such a pain argh

        timestamp = f"<t:{int(datetime.datetime.timestamp(midnight))}:t>"

        daily_skins.append(
            "\nThe daily deals reset at midnight UTC, which should be at "
            f"{timestamp} local time."
        )
    else:
        daily_skins.append("You already purchased every skin available.")

    second_embed = deepcopy(base_embed)

    second_embed["embeds"][0]["fields"] = [
        {
            "name": "✨ New Skins!",
            "value": "\n".join(second_embed_new_fields),
        },
        {
            "name": "Daily Deals",
            "value": "\n".join(daily_skins),
        },
    ]

    embeds = (first_embed, second_embed)

    paginate = Paginate("shop", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]
