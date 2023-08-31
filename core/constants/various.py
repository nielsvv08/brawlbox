from core.config import Config as config
from core.constants.brawlers import BrawlersConstants as brawlers_constants
from core.constants.emoji import EmojiConstants as emoji


class VariousConstants:
    # box

    box_thumbnail = "https://papier.dis.tf/static/brawlbox/boxes/box.png"
    bigbox_thumbnail = "https://papier.dis.tf/static/brawlbox/boxes/bigbox.png"
    megabox_thumbnail = (
        "https://papier.dis.tf/static/brawlbox/boxes/megabox.png"
    )

    # drops

    drops_field_info = [
        ("Power Points", "<:pp:563001978079150102>", "pp"),
        ("Rare", "<:rb:625392826062077971>", "rare"),
        ("Super Rare", "<:sr:625392826188038154>", "sr"),
        (
            "Epic (+ Old Chromatic)",
            "<:eb:625392825793511451>",
            "epic",
        ),
        (
            "Mythic (+ "
            + " ".join(
                [
                    brawlers_constants.emoji[x]
                    for x in brawlers_constants.chromatic_mythic_brawlers
                ]
            )
            + ")",
            "<:mb:625392825915408384>",
            "mythic",
        ),
        (
            "Legendary (+ "
            + " ".join(
                [
                    brawlers_constants.emoji[x]
                    for x in brawlers_constants.chromatic_legendary_brawlers
                ]
            )
            + ")",
            "<:lb:625392826053820430>",
            "legen",
        ),
        ("Gadget", emoji.gadget, "gadget"),
        ("Star Power", emoji.star_power, "star"),
    ]

    # invite

    discord_server_invite = "https://discord.gg/bXQaeFM"

    discord_bot_invite = (
        "https://discord.com/api/oauth2/authorize"
        "?client_id=531858459512012811"
        "&permissions=388176"
        "&scope=bot%20applications.commands"
    )

    # invite

    eval_permission = (
        "306809153748467722",  # Niels
        "355790471219511297",  # Papier
        "292311529213132800",  # BLOODWIING
    )

    eval_coroutine = (
        "import asyncio\n\n"
        "import discourtesy\n\n"
        "from core.config import Config as config\n"
        "from core.constants import Constants as constants\n\n"
        "async def eval_coroutine():\n"
    )

    # leaderboard

    leaderboard_readable = {
        "boxcounter": "boxes",
        "coins": "coins",
        "gems": "gems",
        "starpoints": "star points",
    }

    # prestige

    prestige_congrats = (
        "Congratulations! You prestiged to tier {}.\n"
        "Your reward: 200 gems{}!"
    )

    prestige_base_message = (
        "By using the `/prestige` command, you can reset your Brawl Box "
        "progress. It is going to remove every brawler — including their "
        "level, power points, star powers and gadgets.\n\n"
        "You are still going to keep all of the skins, coins, gems, star "
        "points, big boxes and mega boxes that you collected.\n\n"
    )

    prestige_explanation = prestige_base_message + (
        "**Prestiging is not possible right now, because your account isn't "
        "maxed out yet.**"
    )

    prestige_confirm_message = prestige_base_message + (
        "**You can prestige right now!** To do so, click the check mark "
        "button below to confirm."
    )

    # upgrade

    levels = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    levels_reverse = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)

    upgrades = {
        "2": {"powerpoints": 20, "coins": 20},
        "3": {"powerpoints": 50, "coins": 35},
        "4": {"powerpoints": 100, "coins": 75},
        "5": {"powerpoints": 180, "coins": 140},
        "6": {"powerpoints": 310, "coins": 290},
        "7": {"powerpoints": 520, "coins": 480},
        "8": {"powerpoints": 860, "coins": 800},
        "9": {"powerpoints": 1410, "coins": 1250},
        "10": {"powerpoints": 2300, "coins": 1875},
        "11": {"powerpoints": 3740, "coins": 2800},
    }
