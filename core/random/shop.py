from random import choice


def choose_skins(skins, amount):
    if len(skins) <= amount:
        return skins

    chosen_skins = list()

    for _ in range(amount):
        skin = choice(skins)

        chosen_skins.append(skin)
        skins.remove(skin)

    return chosen_skins
