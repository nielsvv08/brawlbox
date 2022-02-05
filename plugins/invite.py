import discourtesy

from core.config import Config as config
from core.constants import Constants as constants


@discourtesy.command("invite")
async def invite_command(_, __):
    return discourtesy.utils.embed(
        {
            "color": config.colour,
            "fields": [
                {
                    "name": "Join our support server.",
                    "value": f">> {constants.various.discord_server_invite}",
                },
                {
                    "name": "Add the bot to another server.",
                    "value": f">> {constants.various.discord_bot_invite}",
                },
            ],
        }
    )
