import httpx

from core.config import Config as config


class HTTPClient(httpx.AsyncClient):
    def __init__(self):
        super().__init__()

        self.base_url = "https://discord.com/api/v8"
        self.headers = {"Authorization": f"Bot {config.token}"}

    async def edit_original_interaction_response(self, token, json):
        endpoint = (
            f"/webhooks/{config.application_id}/{token}/messages/@original"
        )

        return await self.patch(endpoint, json=json)
