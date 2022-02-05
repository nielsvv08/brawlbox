import discourtesy

from core.config import Config as config
from core.constants import Constants as constants
from core.utils import r


@discourtesy.command("leaderboard", followup=True)
async def leaderboard_command(application, interaction):
    try:
        category = interaction["data"]["options"][0]["value"]
    except KeyError:
        category = "boxcounter"

    request = await application.http.get(
        f"/guilds/{interaction['guild_id']}/members?limit=1000"
    )

    response = request.json()

    if len(response) == 1000:
        return (
            "This command is currently disabled for servers with more than "
            "1,000 members."
        )

    member_ids = [int(member["user"]["id"]) for member in response]

    cursors = (
        database.data.players.find({"id": {"$in": member_ids}})
        .sort(category, -1)
        .limit(12)
        for database in application.mongo.databases
    )

    leaders = list()

    for cursor in cursors:
        async for document in cursor:
            leaders.append((document["id"], int(document[category])))

    leaders = sorted(leaders, key=lambda x: x[1], reverse=True)[:12]

    fields = []

    category = constants.various.leaderboard_readable[category]

    for i, leader in enumerate(leaders, start=1):
        name = [
            member["user"]["username"] + "#" + member["user"]["discriminator"]
            for member in response
            if int(member["user"]["id"]) == leader[0]
        ][0]

        fields.append(
            {
                "name": f"{i}. {name}",
                "value": f"<@{leader[0]}>\n>> {r(leader[1])} {category}",
                "inline": True,
            }
        )

    return discourtesy.utils.embed(
        {"color": config.colour, "title": "Leaderboard", "fields": fields}
    )
