from copy import deepcopy

import discourtesy

from core.config import Config as config
from core.paginate import Paginate

base_embed = discourtesy.utils.embed(
    {
        "title": "Badges",
        "color": config.colour,
    }
)

first_embed = deepcopy(base_embed)
first_embed["embeds"][0]["description"] = (
    "<:box:563003560233533440> a member of the Brawl Box server\n"
    "<:Nitro:836655327684460576> the Nitro Booster role on the Brawl Box server\n"
    "<:vip:569080708153212938> the VIP role on the Brawl Box server\n"
    "<:support:569587383683776553> the VIP+ role on the Brawl Box server\n"
    "<:splus:569599349361868850> the VIP++ role on the Brawl Box server\n"
    "<:staff:569854669543702539> a staff member of the Brawl Box server\n"
    "<:To:609428420438523934> participated in the 1k server members tournament"
)


second_embed = deepcopy(base_embed)
second_embed["embeds"][0]["description"] = (
    "<:1OO:569858643923566596> a box count of at least 100\n"
    "<:1000:569858643810451466> a box count of at least 1,000\n"
    "<:10000:569858644003520522> a box count of at least 10,000\n"
    "<:50000:569858643995131914> a box count of at least 50,000\n"
    "<:100000:569858643772702743> a box count of at least 100,000"
)

third_embed = deepcopy(base_embed)
third_embed["embeds"][0]["description"] = (
    "<:tier1:569816898649325578> tier 1\n"
    "<:tier2:569816898666233856> tier 2\n"
    "<:tier3:569816899140059136> tier 3\n"
    "<:tier4:569816898527559700> tier 4\n"
    "<:tier5:569816898599124992> tier 5\n"
    "<:tier6:569816898708176896> tier 6\n"
    "<:tier7:569816898888400926> tier 7\n"
    "<:tier8:569816899236659210> tier 8"
)


embeds = (first_embed, second_embed, third_embed)


@discourtesy.command("badges")
async def badges_command(application, interaction):
    paginate = Paginate("badges", application, interaction, *embeds)
    await paginate.start()

    return paginate.embeds[0]
