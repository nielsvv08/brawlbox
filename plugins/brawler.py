import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import get_skin, max_gadgets


@discourtesy.command("brawler")
async def brawler_command(application, interaction):
    brawler_name = interaction["data"]["options"][0]["value"].title()

    brawler_name = constants.brawlers.alternative_brawlers.get(
        brawler_name, brawler_name
    )

    if brawler_name not in constants.brawlers.brawlers:
        return f"`{brawler_name}` is not a valid brawler."

    user = interaction["member"]["user"]

    profile, _ = await application.mongo.get_profile(user["id"])

    if profile is None:
        return constants.errors.profile_not_found_self

    brawler = profile["brawlers"].get(brawler_name)

    skin = get_skin(profile, brawler_name)

    if skin == brawler_name:
        thumbnail = constants.brawlers.icon_url.format(brawler_name)
    else:
        thumbnail = constants.brawlers.skin_icon_url.format(brawler_name, skin)

    if brawler is None:
        description = "Status: Locked 🔒"
    else:
        gadgets = [
            constants.brawlers.gadgets_overwrite.get(gadget, gadget)
            for gadget in brawler.get("gadgets", [])
        ]

        starpowers = [
            constants.brawlers.starpowers_overwrite.get(starpower, starpower)
            for starpower in brawler.get("starpowers", [])
        ]

        description = (
            "Status: Unlocked 🔓\n\n"
            f"Level {brawler['level']}\n"
            f"Power Points: {brawler['powerpoints']} / 1400\n\n"
        )

        description += (
            f"Gadgets: {len(gadgets)} / {max_gadgets(brawler_name)}\n"
        )

        if gadgets:
            description += f">> {' & '.join(gadgets)}\n\n"

        description += f"Star Powers: {len(starpowers)} / 2\n"

        if starpowers:
            description += f">> {' & '.join(starpowers)}\n\n"

        skins = brawler.get("skins", [])

        if skins:
            if skin != brawler_name:
                skins[skins.index(skin)] = f"**{skin}**\n"

            description += f"Skins: {', '.join(skins)}"

    return discourtesy.utils.embed(
        {
            "title": brawler_name,
            "color": config.colour,
            "description": description,
            "author": {
                "name": user["username"],
                "icon_url": discourtesy.utils.avatar_url(user),
            },
            "thumbnail": {"url": thumbnail.replace(" ", "%20")},
        }
    )
