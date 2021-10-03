import discourtesy

from .config import Config
from .constants import Constants
from .http import HTTPClient
from .mongo import MongoClient


class Application(discourtesy.Application):
    def __init__(self):
        super().__init__()

        self.http = HTTPClient()
        self.mongo = MongoClient()

        self.version = "2.0.0-alpha"

    @property
    def config(self):
        return Config

    @property
    def constants(self):
        return Constants
