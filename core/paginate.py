import asyncio

from discourtesy.component import Component

from core.constants import Constants as constants


class Paginate:
    def __init__(self, command_name, application, interaction, *embeds):
        self.command_name = command_name

        self.application = application
        self.interaction = interaction

        self.embeds = list(embeds)

        self.token = self.interaction["token"]
        self.id = self.interaction["id"]

        self.prepare_embeds()

    def prepare_embeds(self):
        for i, embed in enumerate(self.embeds, start=1):
            embed.update(
                {
                    "components": [
                        {
                            "type": 1,
                            "components": [
                                {
                                    "type": 2,
                                    "emoji": {"name": "⬅"},
                                    "style": 1,
                                    "custom_id": (
                                        f"{self.command_name}_{i}_{self.id}_previous"
                                    ),
                                },
                                {
                                    "type": 2,
                                    "emoji": {"name": "➡"},
                                    "style": 1,
                                    "custom_id": (
                                        f"{self.command_name}_{i}_{self.id}_next"
                                    ),
                                },
                            ],
                        }
                    ],
                }
            )

            embed["embeds"][0]["footer"] = {
                "text": (
                    "Use the buttons below to navigate!  •  "
                    f"page {i} of {len(self.embeds)}"
                )
            }

            if i == 1:
                embed["components"][0]["components"][0]["disabled"] = True

            if i == len(self.embeds):
                embed["components"][0]["components"][1]["disabled"] = True

            self.embeds[i - 1] = embed

    async def start(self):
        for i, _ in enumerate(self.embeds, start=1):
            previous_component = Component(
                name=f"{self.command_name}_{i}_{self.id}_previous",
                coroutine=self.display_previous_embed,
                timeout=0,
            )

            self.application.dispatch.add_component(previous_component)

            next_component = Component(
                name=f"{self.command_name}_{i}_{self.id}_next",
                coroutine=self.display_next_embed,
                timeout=0,
            )

            self.application.dispatch.add_component(next_component)

        asyncio.create_task(self.stop())

    async def stop(self):
        await asyncio.sleep(60)

        for i, _ in enumerate(self.embeds, start=1):
            del self.application.dispatch.components[
                f"{self.command_name}_{i}_{self.id}_previous"
            ]

            del self.application.dispatch.components[
                f"{self.command_name}_{i}_{self.id}_next"
            ]

        await self.application.http.edit_original_interaction_response(
            self.token,
            constants.buttons.paginate_stop,
        )

    async def display_previous_embed(self, _, interaction):
        if (
            interaction["member"]["user"]["id"]
            != interaction["message"]["interaction"]["user"]["id"]
        ):
            return

        current_index = int(interaction["data"]["custom_id"].split("_")[1])
        previous_index = current_index - 1

        if previous_index <= 0:
            return

        return self.embeds[previous_index - 1]

    async def display_next_embed(self, _, interaction):
        if (
            interaction["member"]["user"]["id"]
            != interaction["message"]["interaction"]["user"]["id"]
        ):
            return

        current_index = int(interaction["data"]["custom_id"].split("_")[1])
        next_index = current_index + 1

        if next_index > len(self.embeds):
            return

        return self.embeds[next_index - 1]
