import datetime

from motor.motor_asyncio import AsyncIOMotorClient

from core.config import Config as config


class MongoClient:
    def __init__(self):
        self.databases = [
            AsyncIOMotorClient(mongo_uri) for mongo_uri in config.mongo_uris
        ]

        self.databases.reverse()

    async def get_guild(self, guild_id):
        query = {"guild_id": int(guild_id)}

        for db in self.databases:
            guild = await db.data.servers.find_one(query)

            if guild:
                return guild, db

        return None, None

    async def get_profile(self, user_id):
        query = {"id": int(user_id)}

        for db in self.databases:
            profile = await db.data.players.find_one(query)

            if profile:
                return profile, db

        return None, None

    async def get_shop(self, user_id):
        query = {"id": int(user_id)}

        db = self.databases[0]

        return await db.data.shop.find_one(query)

    async def insert_guild(self, guild_id, guild_name):
        struct = {
            "guild_id": int(guild_id),
            "guild_name": guild_name,
            "language": "english",
            "prefix": "-",
            "channel_blacklist": [],
        }

        db = self.databases[0]

        await db.data.servers.insert_one(struct)

    async def insert_profile(self, user_id):
        struct = {
            "id": int(user_id),
            "coins": 0,
            "gems": 0,
            "tickets": 0,
            "starpoints": 0,
            "bigboxes": 0,
            "megaboxes": 0,
            "boxcounter": 0,
            "bigcounter": 0,
            "megacounter": 0,
            "daily": 0,
            "weekly": 0,
            "claim": 0,
            "tier": 1,
            "tr_exp": 0,
            "profile_skins": [],
            "brawlers": {
                "Shelly": {"unlocked": True, "level": 1, "powerpoints": 0}
            },
        }

        db = self.databases[0]

        await db.data.players.insert_one(struct)

    async def insert_shop(self, user_id, set_query):
        struct = {"id": int(user_id)}
        struct.update(set_query)

        struct["expireAt"] = datetime.datetime.utcnow().replace(
            hour=0,
            minute=0,
            second=0,
            tzinfo=datetime.timezone(datetime.timedelta()),
        ) + datetime.timedelta(days=1)  # why is datetime such a pain argh

        db = self.databases[0]

        await db.data.shop.insert_one(struct)

    async def delete_shop(self, user_id):
        query = {"id": int(user_id)}

        db = self.databases[0]

        await db.data.shop.delete_one(query)

    async def get_brawlbox_member_ids(self):
        query = {"id": 336163712417136640}

        db = self.databases[0]

        document = await db.data.partners.find_one(query)

        if not document:
            return list()

        return document["members"]

    async def is_user_in_guild(self, user_id, guild_id):
        query = {"id": guild_id}

        db = self.databases[0]

        document = await db.data.partners.find_one(query)

        if user_id in document["members"]:
            return True

        return False


async def update_profile(user_id, db, set_query=None, inc_query=None):
    struct = dict()

    if set_query:
        struct.update({"$set": set_query})

    if inc_query:
        struct.update({"$inc": inc_query})

    await db.data.players.update_one({"id": int(user_id)}, struct)
