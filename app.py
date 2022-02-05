import pathlib
from core import Application

app = Application()

for path in pathlib.Path("plugins").glob("*.py"):
    plugin = f"{path.parent}.{path.stem}"

    app.add_plugin(plugin)
