# Brawl Box

This repository contains the source code for Brawl Box — the loot box simulator for Brawl Stars.

The bot is designed with Discord's latest features in mind, like [slash commands][discord-slash-commands] and [message components][discord-message-components].

## Tech Stack

Brawl Box is written in Python. The bot benefits from the custom-designed [Discourtesy][discourtesy] framework to handle interactions, which utilises a minimal [Starlette][starlette] web server internally. The various data storage happens on an external database, by using one or more [MongoDB][mongodb] clusters.

## Environment Setup

Brawl Box requires a modern version of Python. Currently, [Python 3.10][python-3.10] is used in production.

Firstly, clone the source code and install the [uv][uv] dependency manager.

```sh
# using the customary way with HTTP
git clone https://github.com/nielsvv08/brawlbox.git

# or using the more secure SSH option
git clone git@github.com:nielsvv08/brawlbox.git


pip install uv
```

Then, move to the correct directory in order to create a virtual environment and synchronise the dependencies by running these two commands.

```sh
cd brawlbox

uv sync
```

## Configuration

The bot can be configured by a few environment variables. Rename the `.env.example` file to `.env` and fill out the values accordingly. This file includes two example configurations with randomised or invalidated values.

### Required

- `application_id`, `token`, `public_key`: the respective information found in [Discord's developer portal][discord-developer-portal].
- `mongo_uris`: the URI or URIs for the MongoDB cluster. When mulitple URIs are provided here, they should be separated by a comma and a space.

### Optional

- `colour`: the main colour theme throughout the bot as an integer.

## Command Registry

In order for commands to show up in the selection menu, they should be registred first. This is accomplished by sending a `PUT` request with the command objects as JSON data to the `https://discord.com/api/v10/applications/{application_id}/commands` endpoint. The specific configuration for Brawl Box can be found in the [`commands.json`][commands.json] file.

## Startup

Finally, start the bot by running this command.

```sh
uv run uvicorn app:app
```

The production version is managed by [`pm2`][pm2], whose configuration values are collected in the `pm2.yml` file.

## Contributing

Before contributing to Brawl Box, make sure to read through the [contribution guidelines][contribution-guidelines].

There is a `#development` channel in the support server at [https://discord.gg/bXQaeFM][discord-support-server] dedicated to communication about the development process.

This project is licensed under the terms of the [AGPL-3.0][agpl-3.0-license] license.

[agpl-3.0-license]: <https://github.com/nielsvv08/brawlbox/blob/main/LICENSE>
[commands.json]: <https://github.com/nielsvv08/brawlbox/blob/main/commands.json>
[contribution-guidelines]: <https://github.com/nielsvv08/brawlbox/blob/main/CONTRIBUTING.md>
[discord-developer-portal]: <https://discord.com/developers/applications>
[discord-message-components]: <https://discord.com/developers/docs/interactions/message-components>
[discord-slash-commands]: <https://discord.com/developers/docs/interactions/application-commands>
[discord-support-server]: <https://discord.gg/bXQaeFM>
[discourtesy]: <https://github.com/robinmahieu/discourtesy>
[mongodb]: <https://www.mongodb.com/>
[pm2]: <https://pm2.keymetrics.io/>
[python-3.10]: <https://www.python.org/downloads/>
[starlette]: <https://github.com/encode/starlette>
[uv]: <https://github.com/astral-sh/uv>
