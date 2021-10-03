import asyncio


class Paginate:
    def __init__(self, command_name, application, interaction, *embeds):
        self.command_name = command_name

        self.application = application
        self.interaction = interaction

        self.embeds = list(embeds)

        self.author_id = self.interaction["member"]["user"]["id"]
        self.id = self.interaction["id"]
        self.token = self.interaction["token"]

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
                                    "label": "⬅️",
                                    "style": 1,
                                    "custom_id": f"{self.command_name}_{i}_previous",
                                },
                                {
                                    "type": 2,
                                    "label": "➡️",
                                    "style": 1,
                                    "custom_id": f"{self.command_name}_{i}_next",
                                },
                            ],
                        }
                    ],
                }
            )

            embed["embeds"][0]["footer"] = {
                "text": f"Use the buttons below to navigate!  •  page {i} of {len(self.embeds)}"
            }

            if i == 1:
                embed["components"][0]["components"][0]["disabled"] = True

            if i == len(self.embeds):
                embed["components"][0]["components"][1]["disabled"] = True

            self.embeds[i - 1] = embed

    async def start(self):
        for i, _ in enumerate(self.embeds, start=1):
            component_name = f"{self.command_name}_{i}_previous"

            try:
                self.application.dispatch.component_callbacks[
                    component_name
                ].append(self.display_previous_embed)
            except KeyError:
                self.application.dispatch.component_callbacks[
                    component_name
                ] = [self.display_previous_embed]

            component_name = f"{self.command_name}_{i}_next"

            try:
                self.application.dispatch.component_callbacks[
                    component_name
                ].append(self.display_next_embed)
            except KeyError:
                self.application.dispatch.component_callbacks[
                    component_name
                ] = [self.display_next_embed]

        asyncio.create_task(self.stop())

    async def stop(self):
        await asyncio.sleep(20)

        for i, _ in enumerate(self.embeds, start=1):
            self.application.dispatch.component_callbacks[
                f"{self.command_name}_{i}_previous"
            ].remove(self.display_previous_embed)

            self.application.dispatch.component_callbacks[
                f"{self.command_name}_{i}_next"
            ].remove(self.display_next_embed)

        await self.application.http.edit_original_interaction_response(
            self.token,
            self.application.constants.paginate.stop_embed,
        )

    async def display_previous_embed(self, _, interaction):
        if interaction["member"]["user"]["id"] != self.author_id:
            return

        if interaction["message"]["interaction"]["id"] != self.id:
            return

        current_index = int(interaction["data"]["custom_id"].split("_")[1])
        previous_index = current_index - 1

        if previous_index <= 0:
            return

        await self.application.http.edit_original_interaction_response(
            self.token,
            self.embeds[previous_index - 1],
        )

    async def display_next_embed(self, _, interaction):
        if interaction["member"]["user"]["id"] != self.author_id:
            return

        if interaction["message"]["interaction"]["id"] != self.id:
            return

        current_index = int(interaction["data"]["custom_id"].split("_")[1])
        next_index = current_index + 1

        if next_index > len(self.embeds):
            return

        await self.application.http.edit_original_interaction_response(
            self.token,
            self.embeds[next_index - 1],
        )
