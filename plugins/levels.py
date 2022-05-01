import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate
from core.utils import get_skin, max_gadgets


@discourtesy.command("levels")
async def levels_command(application, interaction):
    user = discourtesy.utils.first_option_user_or_author(interaction)

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        complete_username = user["username"] + "#" + user["discriminator"]
        return constants.errors.profile_not_found.format(complete_username)

    fields = []

    for category, brawlers in constants.brawlers.brawler_categories.items():
        description = ""

        for brawler in brawlers:
            description += f"{get_status(application, profile, brawler)}\n"

        fields.append({"name": category, "value": description, "inline": True})

    embeds = [
        discourtesy.utils.embed(
            {
                "title": "Levels",
                "color": config.colour,
                "author": {
                    "name": user["username"],
                    "icon_url": discourtesy.utils.avatar_url(user),
                },
                "fields": fields[:6],
            }
        ),
        discourtesy.utils.embed(
            {
                "title": "Levels",
                "color": config.colour,
                "author": {
                    "name": user["username"],
                    "icon_url": discourtesy.utils.avatar_url(user),
                },
                "fields": fields[6:],
            }
        ),
    ]

    paginate = Paginate("levels", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]


def get_status(application, profile, brawler_name):
    skin = get_skin(application, profile, brawler_name)
    emoji = constants.brawlers.emoji[skin]

    if not (
        profile["brawlers"]
        .get(brawler_name, {"unlocked": False})
        .get("unlocked", True)
    ):
        return f"{emoji} Locked"

    brawler = profile["brawlers"][brawler_name]

    message = f"{emoji} Level {brawler['level']}"

    maxed_out = True

    if brawler["level"] >= 7:
        if max_gadgets(brawler_name) == 1:
            if len(brawler.get("gadgets", [])) == 1:
                message += " <:g:689837070264303673> <:b:771135048237580298> "
            else:
                message += " <:g:689843668345290844> <:b:771135048237580298>"
                maxed_out = False
        else:
            if len(brawler.get("gadgets", [])) == 1:
                message += " <:g:689837070264303673> <:g:689843668345290844>"
                maxed_out = False
            elif len(brawler.get("gadgets", [])) == 2:
                message += " <:g:689837070264303673> <:g:689837070264303673>"
            else:
                message += " <:g:689843668345290844> <:g:689843668345290844>"
                maxed_out = False

    if brawler["level"] >= 9:
        if len(brawler.get("starpowers", [])) == 1:
            message += " <:l:563001977328369692> <:s:563001977877954590>"
            maxed_out = False
        elif len(brawler.get("starpowers", [])) == 2:
            message += " <:s:563001977877954590> <:s:563001977877954590>"
        else:
            message += "<:l:563001977328369692> <:l:563001977328369692>"
            maxed_out = False

    if brawler["level"] != 11:
        maxed_out = False

    if maxed_out:
        return f"**{message}**"

    return message
