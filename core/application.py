import discourtesy

from .config import Config
from .constants import Constants
from .mongo import MongoClient


class Application(discourtesy.Application):
    def __init__(self):
        super().__init__(
            self.config.application_id,
            self.config.public_key,
            self.config.token,
        )

        self.mongo = MongoClient()

        self.version = "2.0.0-alpha"

    @property
    def config(self):
        return Config

    @property
    def constants(self):
        return Constants
