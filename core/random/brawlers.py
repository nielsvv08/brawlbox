import random


def random_unlocked_brawler(profile):
    return random.choice(
        [
            brawler_name
            for brawler_name, brawler_data in profile["brawlers"].items()
            if brawler_data.get("unlocked", True)
        ]
    )
