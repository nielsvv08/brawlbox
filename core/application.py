import discourtesy

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

        self.version = "2.0.0-alpha"
