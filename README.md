# Brawl Box

This is the repository for version 2.0.0-alpha of Brawl Box — the loot box simulator for Brawl Stars.

The bot is being rewritten to support Discord's latest features regarding interactions, like [slash commands][discord-slash-commands] and [message components][discord-message-components].

## Tech Stack

Brawl Box is written in Python. The bot makes use of the [Discourtesy][discourtesy] framework to handle interactions, which utilises a minimal [Starlette][starlette] server internally.

The different types of data are being stored on one or more [MongoDB][mongodb] clusters.

## Environment Setup

Brawl Box requires [Python 3.10][python-3.10] or higher.

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

poetry install
```

## Configuration

The bot can be configured by a few environment variables. Rename the `.env.example` file to `.env` and fill out the values accordingly.

### Required

- `application_id`, `token`, `public_key`: the respective information found in [Discord's developer portal][discord-developer-portal].
- `mongo_uris`: the URI for the MongoDB cluster. When mulitple URIs are provided here, they should be separated by a comma and a space.

### Optional

- `colour`: the main colour theme used throughout the bot as an integer, e.g. 26367.
- `top_gg_token`: the authentication key used to interact with the top.gg API.

## Command Registry

In order for commands to show up in the selection menu, they should be registred first. This is accomplished by sending a `PUT` request to `https://discord.com/api/v8/applications/{application_id}/commands` containing the command objects as JSON data. The specific configuration for Brawl Box can be found in the [`commands.json`][commands-file] file.

## Startup

Finally, start the bot by running this command.

```sh
poetry run uvicorn run:application
```

## Contributing

This project is licensed under the terms of the [AGPL-3.0][agpl-3.0-license] license.

[agpl-3.0-license]: <https://github.com/nielsvv08/brawlbox/blob/main/LICENSE>
[commands-file]: <https://github.com/nielsvv08/brawlbox/blob/main/commands.json>
[discord-developer-portal]: <https://discord.com/developers/applications>
[discord-message-components]: <https://discord.com/developers/docs/interactions/message-components>
[discord-slash-commands]: <https://discord.com/developers/docs/interactions/application-commands>
[discourtesy]: <https://github.com/robinmahieu/discourtesy>
[mongodb]: <https://www.mongodb.com/>
[poetry]: <https://github.com/python-poetry/poetry>
[python-3.10]: <https://www.python.org/downloads/>
[starlette]: <https://github.com/encode/starlette>
