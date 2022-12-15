import asyncio
import copy
import sys
import time

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

        self.version = "2.5.0"

        self.production = sys.platform == "linux"

        if self.production:
            logger.remove()
            logger.add(sys.stderr, level="WARNING")

        asyncio.create_task(clean_box_cooldown(self))


async def clean_box_cooldown(application):
    while True:
        box_cooldown_copy = copy.deepcopy(application.box_cooldown)

        counter = 0

        for user_id, timestamp in box_cooldown_copy.items():
            if timestamp + 60 < time.time():
                del application.box_cooldown[user_id]
                counter += 1

        logger.info(f"removed {counter} afk users from box_cooldown")

        await asyncio.sleep(600)
