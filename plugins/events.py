import discourtesy


disabled_message = (
    "This command has been replaced by the `/battle` command, in order to "
    "simplify the event structure — so there's no more guessing which event "
    "command to use when!"
)


@discourtesy.command("roborumble")
async def robormble_command(_, __):
    return disabled_message


@discourtesy.command("biggame")
async def biggame_command(_, __):
    return disabled_message


@discourtesy.command("supercityrampage")
async def supercityrampage_command(_, __):
    return disabled_message
