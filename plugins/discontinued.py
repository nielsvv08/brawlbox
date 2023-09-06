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


###


@discourtesy.command("upgrade")
async def upgrade_command(application, interaction):
    return (
        message
        + " Your brawlers are now being **upgraded automatically**!"
        + " <:q:723206473181823056>"
    )


@discourtesy.command("powerpoints")
async def powerpoints_command(application, interaction):
    return (
        message
        + " The **`/brawlers`** command now summarises the progress of all "
        "brawlers in one location. 🪄🪷"  # :magic_wand: and :lotus:
    )


@discourtesy.command("levels")
async def levels_command(application, interaction):
    return (
        message
        + " The **`/brawlers`** command now summarises the progress of all "
        "brawlers in one location. 🪄🪷"
    )
