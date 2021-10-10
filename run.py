from core import Application
from core.config import Config as config

application = Application()
application.set_public_key(config.public_key)

application.add_plugin("plugins.badges")
application.add_plugin("plugins.beep")
application.add_plugin("plugins.brawler")
application.add_plugin("plugins.brawlers")
application.add_plugin("plugins.counter")
application.add_plugin("plugins.eval")
application.add_plugin("plugins.help")
application.add_plugin("plugins.invite")
application.add_plugin("plugins.leaderboard")
application.add_plugin("plugins.levels")
application.add_plugin("plugins.powerpoints")
application.add_plugin("plugins.version")
