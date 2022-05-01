import copy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants

message = (
    "Unlock brawlers by opening boxes.\n\n"
    f"{constants.brawlers.emoji['Shelly']} **Shelly**\n"
    f"{constants.brawlers.emoji['Nita']} **Nita** — 10 boxes\n"
    f"{constants.brawlers.emoji['Colt']} **Colt** — 30 boxes\n"
    f"{constants.brawlers.emoji['Bull']} **Bull** — 60 boxes\n"
    f"{constants.brawlers.emoji['Jessie']} **Jessie** — 100 boxes\n"
    f"{constants.brawlers.emoji['Brock']} **Brock** — 150 boxes\n"
    f"{constants.brawlers.emoji['Dynamike']} **Dynamike** — 210 boxes\n"
    f"{constants.brawlers.emoji['Bo']} **Bo** — 280 boxes\n"
    f"{constants.brawlers.emoji['Tick']} **Tick** — 360 boxes\n"
    f"{constants.brawlers.emoji['8-Bit']} **8-Bit** — 450 boxes\n"
    f"{constants.brawlers.emoji['Emz']} **Emz** — 550 boxes\n"
    f"{constants.brawlers.emoji['Stu']} **Stu ** — 660 boxes\n\n"
    "Every box will also include some star points.\n"
    "The exact amount is based on your current tier.\n\n"
)

tier_lines = (
    f"{constants.emoji.tier_1} — 100 star points = 166 boxes",
    f"{constants.emoji.tier_2} — 100 star points = 156 boxes",
    f"{constants.emoji.tier_3} — 100 star points = 149 boxes",
    f"{constants.emoji.tier_4} — 100 star points = 143 boxes",
    f"{constants.emoji.tier_5} — 100 star points = 138 boxes",
    f"{constants.emoji.tier_6} — 100 star points = 134 boxes",
    f"{constants.emoji.tier_7} — 100 star points = 131 boxes",
    f"{constants.emoji.tier_8} — 100 star points = 128 boxes",
)


@discourtesy.command("trophyroad")
async def trophyroad_command(application, interaction):
    user = interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])
    tier = profile["tier"] if profile else 1

    if tier > 8:
        tier = 8

    description = copy.deepcopy(message)

    for index, line in enumerate(tier_lines, start=1):
        if index == tier:
            description += f"**{line}**\n"
        else:
            description += f"{line}\n"

    return discourtesy.utils.embed(
        {
            "title": "Trophy Road",
            "color": config.colour,
            "description": description,
        }
    )
