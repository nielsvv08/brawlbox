import pathlib
from core import Application

application = Application()

for path in pathlib.Path("plugins").glob("*.py"):
    plugin = f"{path.parent}.{path.stem}"

    application.add_plugin(plugin)
