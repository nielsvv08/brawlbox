import discourtesy

from core.config import Config as config

field_1 = (
    "Brawl Box is a loot box simulator for Brawl Stars, designed for "
    "entertainment purposes.\n\n"
    "Please note that this content is not affiliated with, endorsed, "
    "sponsored, or specifically approved by Supercell and Supercell is not "
    "responsible for it. For more information see Supercell's Fan Content "
    "Policy: https://supercell.com/fan-content-policy."
)

field_2 = (
    "Discord: https://discord.gg/bXQaeFM\n"
    "GitHub: https://github.com/nielsvv08/brawlbox"
)


@discourtesy.command("help")
async def help_command(application, _):
    return discourtesy.utils.embed(
        {
            "title": f"This is Brawl Box version {application.version}!",
            "color": config.colour,
            "fields": [
                {"name": "Brawl-who?", "value": field_1},
                {"name": "Links", "value": field_2},
            ],
        }
    )
