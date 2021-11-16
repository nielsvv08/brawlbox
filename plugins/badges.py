from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.paginate import Paginate

emoji = constants.emoji


base_embed = discourtesy.utils.embed(
    {
        "title": "Profile Badges",
        "color": config.colour,
    }
)

first_embed = deepcopy(base_embed)
first_embed["embeds"][0]["description"] = (
    f"{emoji.box} a member in the Brawl Box server\n"
    f"{emoji.nitro} a Nitro Booster in the Brawl Box server\n"
    f"{emoji.vip} a VIP in the Brawl Box server\n"
    f"{emoji.vip_p} a VIP+ in the Brawl Box server\n"
    f"{emoji.vip_pp} a VIP++ in the Brawl Box server\n"
    f"{emoji.staff} a staff member in the Brawl Box server\n"
    f"{emoji.tournament} a participant of a Brawl Box server tournament"
)


second_embed = deepcopy(base_embed)
second_embed["embeds"][0]["description"] = (
    f"{emoji.b_100} a box count of at least 100\n"
    f"{emoji.b_1k} a box count of at least 1 000\n"
    f"{emoji.b_10k} a box count of at least 10 000\n"
    f"{emoji.b_50k} a box count of at least 50 000\n"
    f"{emoji.b_100k} a box count of at least 100 000"
)

third_embed = deepcopy(base_embed)
third_embed["embeds"][0]["description"] = (
    f"{emoji.tier_1} prestige tier 1\n"
    f"{emoji.tier_2} prestige tier 2\n"
    f"{emoji.tier_3} prestige tier 3\n"
    f"{emoji.tier_4} prestige tier 4\n"
    f"{emoji.tier_5} prestige tier 5\n"
    f"{emoji.tier_6} prestige tier 6\n"
    f"{emoji.tier_7} prestige tier 7\n"
    f"{emoji.tier_8} prestige tier 8"
)

embeds = (first_embed, second_embed, third_embed)


@discourtesy.command("badges")
async def badges_command(application, interaction):
    paginate = Paginate("badges", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]
