import discourtesy

from core.config import Config as config


@discourtesy.command("version")
async def version_command(application, _):
    return discourtesy.utils.embed(
        {
            "title": "Version",
            "color": config.colour,
            "fields": [
                {
                    "name": "Discourtesy",
                    "value": discourtesy.version,
                },
                {
                    "name": "Brawl Box",
                    "value": application.version,
                },
            ],
        }
    )
