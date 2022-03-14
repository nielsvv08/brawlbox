import datetime

import discourtesy

from core import mongo, random
from core.config import Config as config
from core.constants import Constants as constants


@discourtesy.command("battle")
async def battle_command(application, interaction):
    user = interaction["member"]["user"]

    profile, db = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    try:
        brawler_name = interaction["data"]["options"][0]["value"].title()
    except KeyError:
        brawler_name = None

    brawler_name = constants.brawlers.alternative_brawlers.get(
        brawler_name, brawler_name
    )

    if brawler_name not in constants.brawlers.brawlers:
        brawler_name = random.brawlers.random_unlocked_brawler(profile)

    if isinstance(profile["daily"], int):
        profile["daily"] = ""  # legacy thing

    today = str(datetime.date.today())

    if profile["daily"] == today:
        return "You can only battle once a day. Come back tomorrow!"

    win = random.battle.play_battle()

    game_mode = random.battle.random_game_mode()
    description = random.battle.generate_description(win)
    reward = random.battle.generate_reward(win)

    thumbnail = (
        f"https://papier.dis.tf/static/brawlbox/pins/{brawler_name}.png"
    )

    set_query = {"daily": today}
    inc_query = {reward[1]: reward[0]}

    await mongo.update_profile(user["id"], db, set_query, inc_query)

    return discourtesy.utils.embed(
        {
            "title": game_mode,
            "color": config.colour,
            "fields": [
                {
                    "name": f"You {'won' if win else 'lost'}!",
                    "value": description,
                },
                {
                    "name": "Reward",
                    "value": f"{reward[0]} {reward[2]}",
                },
            ],
            "thumbnail": {"url": thumbnail.replace(" ", "%20")},
        }
    )
