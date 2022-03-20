import discourtesy


@discourtesy.command("beep")
async def beep_command(_, __):
    return (
        "Boop! Slash commands are enabled in this channel.\n"
        "Want do disable them? Follow the guide at https://papier.dis.tf/brawlbox/guides/disable-slash-commands."
    )
