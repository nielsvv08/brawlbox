from motor.motor_asyncio import AsyncIOMotorClient

from .config import Config as config


class MongoClient:
    def __init__(self):
        self.mongo_one = AsyncIOMotorClient(config.mongo_one)
        self.mongo_two = AsyncIOMotorClient(config.mongo_two)
        self.mongo_three = AsyncIOMotorClient(config.mongo_three)

    async def get_guild(self, guild_id):
        query = {"guild_id": int(guild_id)}

        guild = await self.mongo_three.data.servers.find_one(query)
        db = self.mongo_three

        if guild is None:
            guild = await self.mongo_two.data.servers.find_one(query)
            db = self.mongo_two

        if guild is None:
            guild = await self.mongo_one.data.servers.find_one(query)
            db = self.mongo_one

        return guild, db

    async def get_profile(self, user_id):
        query = {"id": int(user_id)}

        player = await self.mongo_three.data.players.find_one(query)
        db = self.mongo_three

        if player is None:
            player = await self.mongo_two.data.players.find_one(query)
            db = self.mongo_two

        if player is None:
            player = await self.mongo_one.data.players.find_one(query)
            db = self.mongo_one

        return player, db

    async def insert_guild(self, guild_id, guild_name):
        struct = {
            "guild_id": int(guild_id),
            "guild_name": guild_name,
            "language": "english",
            "prefix": "-",
            "channel_blacklist": [],
        }

        await self.mongo_three.data.servers.insert_one(struct)

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

        await self.mongo_three.data.players.insert_one(struct)


async def update_profile(user_id, db, set_query=None, inc_query=None):
    struct = dict()

    if set_query:
        struct.update({"$set": set_query})

    if inc_query:
        struct.update({"$inc": inc_query})

    await db.data.players.update_one({"id": int(user_id)}, struct)
