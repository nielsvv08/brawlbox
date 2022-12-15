import discourtesy

from core.config import Config as config


@discourtesy.command("trophyroad")
async def trophyroad_command(application, interaction):
    description = (
        "The trophy road has been removed from Brawl Box in the latest "
        "update. All of the brawlers have received a new rarity. Check the "
        "`/brawlers` command for a general overview."
    )

    return discourtesy.utils.embed(
        {
            "title": "Trophy Road (deprecated)",
            "color": config.colour,
            "description": description,
        }
    )
