import discourtesy

from core.config import Config as config


@discourtesy.command("invite")
async def invite_command(_, __):
    return discourtesy.utils.embed(
        {
            "title": "Invite",
            "color": config.colour,
            "fields": [
                {
                    "name": "Join our support server.",
                    "value": ">> https://discord.gg/bXQaeFM",
                },
                {
                    "name": "Add the bot to another server.",
                    "value": ">> https://discord.com/api/oauth2/authorize?client_id=531858459512012811&permissions=388176&scope=bot",
                },
            ],
        }
    )
