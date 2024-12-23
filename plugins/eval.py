import contextlib
import io
import textwrap
import traceback

import discourtesy

from core.constants import Constants as constants


@discourtesy.command("eval")
async def eval_command(application, interaction):
    if (
        interaction["member"]["user"]["id"]
        not in constants.various.eval_permission
    ):
        return "You cannot use this command."

    code = interaction["data"]["options"][0]["value"]
    coroutine = constants.various.eval_coroutine + textwrap.indent(
        code, "    "
    )

    variables = {"application": application, "interaction": interaction}

    variables.update(globals())

    stdout = io.StringIO()

    try:
        exec(coroutine, variables)

        with contextlib.redirect_stdout(stdout):
            returned = await variables["eval_coroutine"]()
    except Exception:
        return f"```py\n{traceback.format_exc()}```"

    if returned is None and "return" not in coroutine.lower():
        return

    message = f"```py\n{stdout.getvalue()}{repr(returned)}```"

    if len(message) >= 2000:
        return "The output is too long to be returned."

    return message
