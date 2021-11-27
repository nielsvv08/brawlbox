import discourtesy

from core.config import Config as config
from core.constants import Constants as constants


@discourtesy.command("vote")
async def vote_command(_, __):
    return discourtesy.utils.embed(
        {
            "color": config.colour,
            "description": (
                "Click the link below to vote for Brawl Box on top.gg.\n"
                f">> {constants.various.top_gg_link}"
            ),
            "fields": [
                {
                    "name": "Voted already?",
                    "value": "Claim a reward by using the `/claim` command!",
                },
            ],
            "thumbnail": {"url": constants.various.vote_thumbnail},
        }
    )
