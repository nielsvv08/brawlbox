import datetime
import random
import time

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants

emoji = constants.emoji


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

    if not has_voted:
        return "You can't claim a voting reward, since you didn't vote yet."

    if profile["claim"] > int(time.time()) - 41400:  # 11 hours 30 minutes
        return "You can't claim a voting reward, since you didn't vote yet!"

    is_weekend = datetime.datetime.utcnow().weekday in (4, 5, 6)

    if is_weekend:
        amount, db_type, fmt_type, reward_emoji = random.choice(
            [
                (20, "gems", "gems", emoji.gems),
                (100, "starpoints", "star points", emoji.star_points),
                (3, "megaboxes", "mega boxes", emoji.mega_box),
            ]
        )
    else:
        amount, db_type, fmt_type, reward_emoji = random.choice(
            [
                (15, "gems", "gems", emoji.gems),
                (75, "starpoints", "star points", emoji.star_points),
                (2, "megaboxes", "mega boxes", emoji.mega_box),
            ]
        )

    await db.data.players.find_one_and_update(
        {"id": user["id"]},
        {
            "$set": {
                "claim": int(time.time()),
                db_type: profile[db_type] + amount,
            }
        },
    )

    description = (
        f"Your reward: **{amount} {fmt_type}** {reward_emoji} — enjoy."
    )

    return discourtesy.utils.embed(
        {
            "color": config.colour,
            "title": "Thanks for voting!",
            "description": description,
        }
    )
