# Brawl Box

This is the repository for version 2.0.0-alpha of Brawl Box — the loot box simulator for Brawl Stars.

The bot is being rewritten to support Discord's latest features regarding interactions, like [slash commands][discord-slash-commands] and [message components][discord-message-components].

## Tech Stack

Brawl Box is written in Python. The bot makes use of the [Discourtesy][discourtesy] framework to handle interactions, which utilises a minimal [Starlette][starlette] server internally.

The different types of data are being stored on three separate [MongoDB][mongodb] clusters.

## Environment Setup

Brawl Box requires [Python 3.9][python-3.9] or higher.

Firstly, clone the source code and install the [Poetry][poetry] dependency manager.

```sh
# using the traditional method
git clone https://github.com/nielsvv08/brawlbox.git

# or using SSH
git clone git@github.com:nielsvv08/brawlbox.git
```

```sh
pip install poetry
```

Then, move to the correct directory to create a virtual environment and install the dependencies by running these commands.

```sh
cd brawlbox
```

```sh
poetry install
```

The bot requires a few environment variables to be set up. Rename the `.env.example` file to `.env` and fill out the values accordingly.

The `colour` field defines the main colour theme used throughout the bot as an integer, e.g. 26367.

The `application_id`, `token` and `public_key` fields require the respective information found in [Discord's developer portal][discord-developer-portal].

The `mongo_one`, `mongo_two` and `mongo_three` fields specify the three MongoDB clusters.

Finally, start the bot by running this command.

```sh
poetry run uvicorn run:application
```

## Contributing

This project is licensed under the terms of the [AGPL-3.0][agpl-3.0-license] license.

[agpl-3.0-license]: <https://github.com/nielsvv08/brawlbox/blob/main/LICENSE>
[discord-developer-portal]: <https://discord.com/developers/applications>
[discord-message-components]: <https://discord.com/developers/docs/interactions/message-components>
[discord-slash-commands]: <https://discord.com/developers/docs/interactions/application-commands>
[discourtesy]: <https://github.com/robinmahieu/discourtesy>
[mongodb]: <https://www.mongodb.com/>
[poetry]: <https://github.com/python-poetry/poetry>
[python-3.9]: <https://www.python.org/downloads/>
[starlette]: <https://github.com/encode/starlette>
