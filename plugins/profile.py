# from typing import Optional

# import discord
# from discord.ext import commands

# from utils.decorators import trigger_typing
# from utils.emojis import BIG_BOX, COINS, GEMS, MEGA_BOX, STAR_POINTS
# from utils.format import r

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import r


@discourtesy.command("profile", followup=True)
async def profile_command(application, interaction):
    # self.guild_roles = (
    #     (
    #         536985593251364875,
    #         0xFFFF00,
    #         "https://papier.dis.tf/static/brawlbox/icons/vip.png",
    #         "Brawl Box VIP",
    #     ),
    #     (
    #         537357589751660544,
    #         0x07D61D,
    #         "https://papier.dis.tf/static/brawlbox/icons/vip+.png",
    #         "Brawl Box VIP+",
    #     ),
    #     (
    #         568847798716334100,
    #         0xB4FF00,
    #         "https://papier.dis.tf/static/brawlbox/icons/vip++.png",
    #         "Brawl Box VIP++",
    #     ),
    #     (
    #         536984102004326402,
    #         0xFA3C3C,
    #         "https://papier.dis.tf/static/brawlbox/icons/staff.png",
    #         "Brawl Box Staff Member",
    #     ),
    # )

    # self.tier_emojis = (
    #     "<:tier1:569816898649325578>",
    #     "<:tier2:569816898666233856>",
    #     "<:tier3:569816899140059136>",
    #     "<:tier4:569816898527559700>",
    #     "<:tier5:569816898599124992>",
    #     "<:tier6:569816898708176896>",
    #     "<:tier7:569816898888400926>",
    #     "<:tier8:569816899236659210>",
    # )

    # self.tournament_participants = (
    #     306809153748467722,
    #     358724434036785152,
    #     369848495546433537,
    #     355514130737922048,
    #     375331472736780289,
    #     294438945578811393,
    #     325267410984763414,
    #     355790471219511297,
    #     498832580796481536,
    #     431626512383606786,
    #     383630403317268480,
    #     292311529213132800,
    #     485867333173116958,
    #     438417214727782402,
    #     367342166185345035,
    #     402417477717458945,
    #     424597406236278784,
    #     431221652022624257,
    #     381858316969836544,
    #     490589740719013910,
    #     329285285823250434,
    #     245901907854491649,
    #     330735992317411329,
    #     441509661846536193,
    #     315854506879352832,
    #     573548974636793876,
    #     443851546829258753,
    #     509065589596356639,
    #     350723921693376513,
    #     608752433539317790,
    #     421524239083110401,
    #     207174976330137601,
    #     367678216850112513,
    #     315210840506892288,
    #     301350669833469954,
    #     589190638923415571,
    #     382256366129119232,
    # )

    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    is_in_brawl_box_community = await application.mongo.is_user_in_guild(
        user["id"], 336163712417136640
    )

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


# description = f"**Coins:** {r(player['coins'])} {COINS}\n"
# description += f"**Gems:** {r(player['gems'])} {GEMS}\n"
# description += (
#     f"**Star Points:** {r(int(player['starpoints']))} {STAR_POINTS}\n\n"
# )
# description += f"**Big Boxes:** {r(int(player['bigboxes']))} {BIG_BOX}\n"
# description += (
#     f"**Mega Boxes:** {r(int(player['megaboxes']))} {MEGA_BOX}\n\n"
# )

# badges = ""

# box_count = (
#     player["boxcounter"] + player["bigcounter"] + player["megacounter"]
# )

# # TODO: structural pattern matching in Python 3.10

# if box_count < 100:
#     pass
# elif box_count > 100 and box_count < 1000:
#     badges += "<:1OO:569858643923566596> "
# elif box_count > 1000 and box_count < 10000:
#     badges += "<:1000:569858643810451466> "
# elif box_count > 10000 and box_count < 50000:
#     badges += "<:10000:569858644003520522> "
# elif box_count > 50000 and box_count < 100000:
#     badges += "<:50000:569858643995131914> "
# else:
#     badges += "<:100000:569858643772702743> "

# if member is not None:
#     badges += "<:box:563003560233533440> "

#     if "585540533376647171" in member["roles"]:  # nitro booster
#         badges += "<:N:836655327684460576> "

# if player["id"] in self.tournament_participants:
#     badges += "<:To:609428420438523934> "

# tier = int(player["tier"])
# tier_emoji_amount = 8 if tier > 8 else tier

# if badges:
#     badges += " • "  # en space on both sides

# for i in range(0, tier_emoji_amount):
#     badges += f"{self.tier_emojis[i]} "

# if tier > 8:
#     badges += f"({tier})"

# description += f"**Badges:** {badges}"

# embed = discord.Embed(
#     description=description,
#     color=color,
# )

# embed.set_author(name=user.name, icon_url=user.avatar_url)

# if thumb_url is not None:
#     embed.set_thumbnail(url=thumb_url),

# if footer is not None:
#     embed.set_footer(text=footer, icon_url=thumb_url)

# await ctx.send(embed=embed)
