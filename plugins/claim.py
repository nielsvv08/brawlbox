import time

import discourtesy

from core import mongo, random
from core.config import Config as config
from core.constants import Constants as constants


@discourtesy.command("claim")
async def claim_command(application, interaction):
    user = interaction["member"]["user"]

    profile, db = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    link = constants.various.top_gg_check_link.format(user["id"])

    request = await application.http.get(
        link, headers=constants.various.top_gg_headers
    )

    response = request.json()
    has_voted = bool(response["voted"])

    # 41,400 seconds = 11 hours and 30 minutes

    if not has_voted or profile["claim"] > int(time.time()) - 41400:
        return (
            "You can't claim a reward for voting right now, because you "
            "haven't voted yet. Check out the `/vote` command for more "
            "information."
        )

    amount, db_type, fmt_type, emoji = random.claim()

    set_query = {"claim": int(time.time())}
    inc_query = {db_type: amount}

    await mongo.update_profile(user["id"], db, set_query, inc_query)

    description = f"Your reward: **{amount} {fmt_type}** {emoji} — enjoy."

    return discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": "Thanks for voting!",
            "description": description,
        }
    )
