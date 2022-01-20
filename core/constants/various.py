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
