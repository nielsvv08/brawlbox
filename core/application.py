import sys

import discourtesy
from loguru import logger

from core.cache import Cache
from core.config import Config as config
from core.mongo import MongoClient


class Application(discourtesy.Application):
    def __init__(self):
        super().__init__(
            config.application_id,
            config.public_key,
            config.token,
        )

        self.mongo = MongoClient()
        self.cache = Cache(self)

        self.version = "2.0.0-alpha"

        self.production = sys.platform == "linux"

        if self.production:
            logger.remove()
            logger.add(sys.stderr, level="WARNING")
