import asyncio


class Cache:
    def __init__(self, application):
        self.application = application

        self.member_ids = list()

        asyncio.create_task(self.get_member_ids())

    async def get_member_ids(self):
        while True:
            self.member_ids = (
                await self.application.mongo.get_brawlbox_member_ids()
            )

            await asyncio.sleep(300)  # five minutes
