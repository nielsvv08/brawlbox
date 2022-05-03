import asyncio
import time
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

        self.box_cooldown = dict()

        self.version = "2.1.3"

        self.production = sys.platform == "linux"

        if self.production:
            logger.remove()
            logger.add(sys.stderr, level="WARNING")

        asyncio.create_task(clean_box_cooldown(self))


async def clean_box_cooldown(application):
    while True:
        for user_id, timestamp in application.box_cooldown.values():
            if timestamp + 60 < time.time():
                del application.box_cooldown[user_id]

        await asyncio.sleep(600)
