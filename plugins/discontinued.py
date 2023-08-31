import discourtesy

message = "This command has been discontinued and is going to be removed soon."


@discourtesy.command("badges")
async def badges_command(application, interaction):
    return message


@discourtesy.command("claim")
async def claim_command(application, interaction):
    return message


@discourtesy.command("leaderboard")
async def leaderboard_command(application, interaction):
    return message


@discourtesy.command("vote")
async def vote_command(application, interaction):
    return message
