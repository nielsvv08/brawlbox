import os

import dotenv

dotenv.load_dotenv()


class Config:
    application_id = os.getenv("application_id")
    token = os.getenv("token")
    public_key = os.getenv("public_key")

    mongo_one = os.getenv("mongo_one")
    mongo_two = os.getenv("mongo_two")
    mongo_three = os.getenv("mongo_three")

    colour = int(os.getenv("colour", 0))
    top_gg_token = os.getenv("top_gg_token", "")
