from core.config import Config as config


class ProfileConstants:
    # skins: {key: (colour, thumbnail, footer)}

    skins = {
        "default": (config.colour, None, None),
        "winter_2019": (
            10875635,
            "https://papier.dis.tf/static/brawlbox/icons/winter.png",
            "Brawl Box Winter Skin",
        ),
        "5_robo_wins": (
            15548997,
            "https://papier.dis.tf/static/brawlbox/icons/robo-rumble.png",
            "Robo Rumble Skin",
        ),
        "5_game_wins": (
            15548997,
            "https://papier.dis.tf/static/brawlbox/icons/big-game.png",
            "Big Game Skin",
        ),
        "5_city_wins": (
            15548997,
            "https://papier.dis.tf/static/brawlbox/icons/super-city-rampage.png",
            "Super City Rampage Skin",
        ),
        "staff": (
            16399420,
            "https://papier.dis.tf/static/brawlbox/icons/staff.png",
            "Brawl Box Staff Member",
        ),
    }

    staff_members = (
        306809153748467722,  # Niels
        355790471219511297,  # Papier
        292311529213132800,  # BLOODWIING
        498832580796481536,  # QuestingNight
        139834937120391168,  # Unknown007
    )
