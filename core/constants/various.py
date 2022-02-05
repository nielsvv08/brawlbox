from core.config import Config as config


class VariousConstants:
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

    leaderboard_readable = {
        "boxcounter": "boxes",
        "coins": "coins",
        "gems": "gems",
        "starpoints": "star points",
    }

    prestige_congrats = (
        "Congratulations! You prestiged to tier {}.\n"
        "Your reward: 200 gems{}!"
    )

    prestige_base_message = (
        "By using the `/prestige` command, you can reset your Brawl Box "
        "progress. It is going to remove every brawler — including their "
        "level, power points, star powers and gadgets.\n\n"
        "You are still going to keep all of the skins, coins, gems, star "
        "ponts, big boxes and mega boxes that you collected.\n\n"
    )

    prestige_explanation = prestige_base_message + (
        "**Prestiging is not possible right now, because your account isn't "
        "maxed out yet.**"
    )

    prestige_confirm_message = prestige_base_message + (
        "**You can prestige right now!** To do so, click the check mark "
        "button below to confirm."
    )

    vote_thumbnail = (
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/"
        "thumbs/120/twitter/259/ballot-box-with-ballot_1f5f3.png"
    )

    top_gg_check_link = (
        "https://top.gg/api/bots/531858459512012811/check?userId={}"
    )
    top_gg_link = "https://top.gg/bot/531858459512012811/vote"
    top_gg_headers = {
        "Authorization": config.top_gg_token,
        "Content-Type": "application/json",
        "User-Agent": "Brawl Box",
    }
