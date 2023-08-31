import os

import dotenv

dotenv.load_dotenv()


class Config:
    application_id = os.getenv("application_id")
    token = os.getenv("token")
    public_key = os.getenv("public_key")

    mongo_uris = os.getenv("mongo_uris").split(", ")

    colour = int(os.getenv("colour", 0))
