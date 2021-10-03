import discourtesy


@discourtesy.command("beep")
async def beep_command(_, __):
    return "boop"
