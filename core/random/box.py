import copy
import math
import random

from core.constants import Constants as constants
from .normal import normal_distribution


def generate_coins(tries):
    multiplier = math.sqrt(tries)  # 1 --> 1, 4 --> 2, 8 --> ≈2.8

    return normal_distribution(240 * multiplier, 24 * multiplier)


def generate_starpoints(tries):
    multiplier = math.sqrt(tries)  # 1 --> 1, 4 --> 2, 8 --> ≈2.8

    for _ in range(tries):
        if random.randint(1, 100) == 1:  # 1% chance
            return normal_distribution(100 * multiplier, 3 * multiplier)

    return 0


def generate_gems(tries):
    multiplier = math.sqrt(tries)  # 1 --> 1, 4 --> 2, 8 --> ≈2.8

    for _ in range(tries):
        if random.randint(1, 4) == 1:  # 25% chance
            return normal_distribution(5 * multiplier, 1.3 * multiplier)

    return 0


def get_droprates(profile):
    def remove_drop(drop, rates):
        dropped_percent = rates.pop(drop)

        index = 0

        for item in rates:
            index += 1

            if len(rates) == index:
                rates[item] = 0.0
                rates[item] = 100.0 - sum(rates.values())
                break

            rates[item] += dropped_percent * (
                rates[item] / (100.0 - dropped_percent)
            )

    droprates = copy.deepcopy(constants.brawlers.droprates)
    rarities = constants.brawlers.rarities

    for rarity in rarities:
        if all(
            profile["brawlers"]
            .get(brawler, {"unlocked": False})
            .get("unlocked", True)
            for brawler in rarities[rarity]
        ):
            remove_drop(rarity, droprates)

    if any(
        profile["brawlers"].get(brawler, {"level": 1})["level"] >= 9
        and len(profile["brawlers"].get(brawler, {}).get("starpowers", []))
        != 2
        for brawler in sum(list(rarities.values()), [])
    ):
        droprates["star"] = 3.9
        droprates["pp"] -= droprates["star"]

    if any(
        profile["brawlers"].get(brawler, {"level": 1})["level"] >= 7
        and len(profile["brawlers"].get(brawler, {}).get("gadgets", []))
        < (2 if brawler in constants.brawlers.two_gadget_brawlers else 1)
        for brawler in sum(list(rarities.values()), [])
    ):
        droprates["gadget"] = 5.2
        droprates["pp"] -= droprates["gadget"]

    if all(
        profile["brawlers"].get(brawler, {"powerpoints": 0})["powerpoints"]
        == 3740
        or not profile["brawlers"].get(brawler, {}).get("unlocked", True)
        for brawler in sum(list(rarities.values()), [])
    ):
        droprates["pp"] = 0.0

    return rarities, droprates


def get_random_box_item(profile):
    drops, droprates = get_droprates(profile)

    # profile["tr_exp"] += 1

    out = random.randint(0, 10000)

    for rarity in droprates:
        if out <= int(droprates[rarity] * 100):
            if rarity == "pp":
                # power points

                brawlers = [
                    brawler
                    for brawler in constants.brawlers.brawlers
                    if profile["brawlers"]
                    .get(brawler, {"unlocked": False})
                    .get("unlocked", True)
                    and profile["brawlers"].get(brawler, {"powerpoints": 0})[
                        "powerpoints"
                    ]
                    != 3740
                ]

                if len(brawlers) == 0:
                    break

                brawler = random.choice(brawlers)

                power_points = normal_distribution(50, 5)
                current_pp = profile["brawlers"][brawler]["powerpoints"]

                if current_pp + power_points > 3740:
                    power_points = (
                        3740 - profile["brawlers"][brawler]["powerpoints"]
                    )
                    new_pp = 3740
                else:
                    new_pp = current_pp + power_points

                profile["brawlers"][brawler]["powerpoints"] = new_pp

                message = (
                    f"{power_points} <:pp:563001978079150102> for {brawler}"
                )

                return profile, message

            elif rarity == "gadget":
                # gadget

                possible_gadget_brawlers = [
                    brawler
                    for brawler in profile["brawlers"]
                    if profile["brawlers"][brawler]["level"] >= 7
                    and len(
                        profile["brawlers"].get(brawler, {}).get("gadgets", [])
                    )
                    < (
                        2
                        if brawler in constants.brawlers.two_gadget_brawlers
                        else 1
                    )
                ]

                if len(possible_gadget_brawlers) == 0:
                    break

                brawler = random.choice(possible_gadget_brawlers)

                current_gadgets = profile["brawlers"][brawler].get(
                    "gadgets", []
                )

                gadget = random.choice(
                    [
                        gadget
                        for gadget in constants.brawlers.brawlers[brawler][
                            "gadgets"
                        ]
                        if gadget not in current_gadgets
                    ]
                )

                new_gadgets = current_gadgets + [gadget]

                real_gadget = constants.brawlers.gadgets_overwrite.get(
                    gadget, gadget
                )

                profile["brawlers"][brawler]["gadgets"] = new_gadgets

                message = (
                    f"**{brawler}'s Gadget**: {real_gadget} "
                    "<:ga:689837070264303673>"
                )

                return profile, message

            elif rarity == "star":
                # star power

                possible_starpower_brawlers = [
                    brawler
                    for brawler in profile["brawlers"]
                    if profile["brawlers"][brawler]["level"] >= 9
                    and len(profile["brawlers"][brawler].get("starpowers", []))
                    != 2
                ]

                if len(possible_starpower_brawlers) == 0:
                    break

                brawler = random.choice(possible_starpower_brawlers)

                current_starpowers = profile["brawlers"][brawler].get(
                    "starpowers", []
                )

                starpower = random.choice(
                    [
                        starpower
                        for starpower in constants.brawlers.brawlers[brawler][
                            "starpowers"
                        ]
                        if starpower not in current_starpowers
                    ]
                )

                new_starpowers = current_starpowers + [starpower]

                real_starpower = constants.brawlers.starpowers_overwrite.get(
                    starpower, starpower
                )

                profile["brawlers"][brawler]["starpowers"] = new_starpowers

                message = (
                    f"**{brawler}'s Star Power**: {real_starpower} "
                    + constants.emoji.star_power
                )

                return profile, message

            # no pp, gadget or sp ... new brawler unlock!

            random.shuffle(drops[rarity])

            for brawler in drops[rarity]:
                if (
                    profile["brawlers"]
                    .get(brawler, {"unlocked": False})
                    .get("unlocked", True)
                ):
                    continue

                selected = profile["brawlers"].get(brawler, {}).get("selected")
                skins = profile["brawlers"].get(brawler, {}).get("skins")

                new_brawler = {
                    "level": 1,
                    "powerpoints": 0,
                }

                if selected:
                    new_brawler.update({"selected": selected})

                if skins:
                    new_brawler.update({"skins": skins})

                emoji = constants.brawlers.brawlers[brawler]["emoji"]

                brawler_rarity = constants.brawlers.brawlers[brawler]["rarity"]
                rarity_emoji = constants.brawlers.rarity_emoji[brawler_rarity]

                profile["brawlers"][brawler] = new_brawler

                message = (
                    f"{emoji} {rarity_emoji} **{brawler}** {rarity_emoji} "
                    f"{emoji}"
                )

                return profile, message

        else:
            out -= int(droprates[rarity] * 100)

    return profile, ""
